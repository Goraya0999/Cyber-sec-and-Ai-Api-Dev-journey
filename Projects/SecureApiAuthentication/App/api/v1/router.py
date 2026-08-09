from fastapi import APIRouter

from App.api.v1.routes_auth import router as auth_router
from App.api.v1.routes_users import router as users_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth_router)
api_router.include_router(users_router)
