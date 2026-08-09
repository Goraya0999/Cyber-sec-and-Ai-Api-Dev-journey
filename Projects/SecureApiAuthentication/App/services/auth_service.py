from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

from fastapi import HTTPException, status
from redis.asyncio import Redis
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from App.core.config import settings
from App.core.security import (
    create_access_token,
    generate_refresh_token,
    hash_password,
    hash_refresh_token,
    verify_password,
)
from App.models.refresh_token import RefreshToken
from App.models.role import Role
from App.models.role import USER as DEFAULT_ROLE
from App.models.user import User
from App.schemas.token import TokenPair
from App.schemas.user import UserCreate
from App.services import lockout_service

GENERIC_LOGIN_ERROR = "Invalid credentials"


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(select(User).where(User.email == email.strip().lower()))
    return result.scalar_one_or_none()


async def register_user(db: AsyncSession, payload: UserCreate) -> User:
    existing = await get_user_by_email(db, payload.email)
    if existing is not None:
        # Same status/shape as any other validation error — don't reveal
        # via a different response shape that the email specifically exists.
        raise HTTPException(status.HTTP_409_CONFLICT, "Email is already registered")

    default_role_result = await db.execute(select(Role).where(Role.name == DEFAULT_ROLE))
    default_role = default_role_result.scalar_one_or_none()
    if default_role is None:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Default role missing — run migrations before starting the API",
        )

    user = User(
        email=payload.email.strip().lower(),
        hashed_password=hash_password(payload.password),
        roles=[default_role],
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def _issue_token_pair(
    db: AsyncSession, user: User, device_info: str | None, family_id: UUID | None = None
) -> TokenPair:
    access_token = create_access_token(str(user.id), user.role_names)
    raw_refresh, refresh_hash = generate_refresh_token()

    new_id = uuid4()
    token_row = RefreshToken(
        id=new_id,
        user_id=user.id,
        token_hash=refresh_hash,
        # New login -> starts its own family. Rotation reuses the family
        # id so the whole chain can be revoked together on replay.
        family_id=family_id or new_id,
        device_info=device_info,
        expires_at=datetime.now(timezone.utc)
        + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
    )
    db.add(token_row)
    await db.commit()

    return TokenPair(access_token=access_token, refresh_token=raw_refresh)


async def login_user(
    db: AsyncSession,
    redis: Redis,
    email: str,
    password: str,
    device_info: str | None = None,
) -> TokenPair:
    if await lockout_service.is_locked(redis, email):
        raise HTTPException(
            status.HTTP_423_LOCKED,
            "Account temporarily locked due to repeated failed logins. Try again later.",
        )

    user = await get_user_by_email(db, email)

    # Always run verify_password even on a missing user (against a dummy hash)
    # so response timing doesn't leak whether the email exists.
    if user is None or not verify_password(password, user.hashed_password):
        if user is not None:
            await lockout_service.register_failed_attempt(redis, email)
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, GENERIC_LOGIN_ERROR)

    if not user.is_active:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Account is disabled")

    await lockout_service.reset_failed_attempts(redis, email)
    return await _issue_token_pair(db, user, device_info)


async def refresh_tokens(
    db: AsyncSession, raw_refresh_token: str, device_info: str | None = None
) -> TokenPair:
    token_hash = hash_refresh_token(raw_refresh_token)
    result = await db.execute(
        select(RefreshToken).where(RefreshToken.token_hash == token_hash)
    )
    token_row = result.scalar_one_or_none()

    if token_row is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid refresh token")

    if token_row.revoked:
        # Reuse of a revoked token => possible theft. Kill the whole family.
        await db.execute(
            RefreshToken.__table__.update()
            .where(RefreshToken.family_id == token_row.family_id)
            .values(revoked=True)
        )
        await db.commit()
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Refresh token reuse detected — all sessions in this family were revoked",
        )

    if token_row.expires_at.replace(tzinfo=token_row.expires_at.tzinfo or timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Refresh token expired")

    user_result = await db.execute(select(User).where(User.id == token_row.user_id))
    user = user_result.scalar_one_or_none()
    if user is None or not user.is_active:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid refresh token")

    # Rotate: revoke the old token, issue a new one in the same family.
    token_row.revoked = True
    db.add(token_row)
    await db.commit()

    return await _issue_token_pair(db, user, device_info, family_id=token_row.family_id)


async def logout(db: AsyncSession, raw_refresh_token: str) -> None:
    token_hash = hash_refresh_token(raw_refresh_token)
    result = await db.execute(
        select(RefreshToken).where(RefreshToken.token_hash == token_hash)
    )
    token_row = result.scalar_one_or_none()
    if token_row is not None:
        token_row.revoked = True
        db.add(token_row)
        await db.commit()


async def logout_all(db: AsyncSession, user_id: UUID) -> None:
    await db.execute(
        RefreshToken.__table__.update()
        .where(RefreshToken.user_id == user_id)
        .values(revoked=True)
    )
    await db.commit()
