from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from App.api.deps import get_current_user, require_role
from App.db.session import get_db
from App.models.role import ADMIN
from App.models.user import User
from App.schemas.user import UserOut

router = APIRouter(tags=["users"])


# --- Public endpoint: no auth required ----------------------------------
@router.get("/public/ping")
async def public_ping():
    """Anyone can call this — useful as a smoke test / uptime check."""
    return {"message": "pong", "auth_required": False}


# --- Protected endpoint: any authenticated user --------------------------
@router.get("/users/me", response_model=UserOut)
async def read_current_user(current_user: User = Depends(get_current_user)):
    return UserOut.from_user(current_user)


# --- Role-protected endpoint: admin only ----------------------------------
@router.get("/admin/users", response_model=list[UserOut])
async def list_all_users(
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(require_role(ADMIN)),
):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return [UserOut.from_user(u) for u in users]
