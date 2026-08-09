from __future__ import annotations

from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from redis.asyncio import Redis
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from App.core.redis_client import get_redis_client
from App.core.security import decode_token
from App.db.session import get_db
from App.models.user import User

_bearer_scheme = HTTPBearer(auto_error=False)


async def get_redis(redis: Redis = Depends(get_redis_client)) -> Redis:
    return redis


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Decodes the bearer access token and loads the corresponding, active user.

    This is the single choke point every protected route depends on — deny
    by default: no token, bad token, expired token, or inactive user all
    result in 401.
    """
    if credentials is None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        payload = decode_token(credentials.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Access token expired")
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid access token")

    if payload.get("type") != "access":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token type")

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid access token")

    result = await db.execute(select(User).where(User.id == UUID(user_id)))
    user = result.scalar_one_or_none()

    if user is None or not user.is_active:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User not found or inactive")

    return user


def require_role(*allowed_roles: str):
    """Dependency factory: 403s unless the current user has at least one of the
    given roles. Use per-route: Depends(require_role("admin"))."""

    async def checker(user: User = Depends(get_current_user)) -> User:
        if not set(user.role_names) & set(allowed_roles):
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Insufficient permissions")
        return user

    return checker
