from fastapi import APIRouter, Depends, Request, status
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from App.api.deps import get_current_user, get_redis
from App.core.config import settings
from App.core.rate_limit import limiter
from App.db.session import get_db
from App.models.user import User
from App.schemas.token import LogoutRequest, RefreshRequest, TokenPair
from App.schemas.user import UserCreate, UserLogin, UserOut
from App.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
@limiter.limit(settings.REGISTER_RATE_LIMIT)
async def register(request: Request, payload: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await auth_service.register_user(db, payload)
    return UserOut.from_user(user)


@router.post("/login", response_model=TokenPair)
@limiter.limit(settings.LOGIN_RATE_LIMIT)
async def login(
    request: Request,
    payload: UserLogin,
    db: AsyncSession = Depends(get_db),
    redis: Redis = Depends(get_redis),
):
    device_info = request.headers.get("user-agent")
    return await auth_service.login_user(
        db, redis, payload.email, payload.password, device_info
    )


@router.post("/refresh", response_model=TokenPair)
async def refresh(
    request: Request, payload: RefreshRequest, db: AsyncSession = Depends(get_db)
):
    device_info = request.headers.get("user-agent")
    return await auth_service.refresh_tokens(db, payload.refresh_token, device_info)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(payload: LogoutRequest, db: AsyncSession = Depends(get_db)):
    await auth_service.logout(db, payload.refresh_token)


@router.post("/logout-all", status_code=status.HTTP_204_NO_CONTENT)
async def logout_all(
    db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    await auth_service.logout_all(db, current_user.id)
