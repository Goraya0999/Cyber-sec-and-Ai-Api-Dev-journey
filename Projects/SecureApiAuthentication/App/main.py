from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from scalar_fastapi import get_scalar_api_reference
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from App.api.v1.router import api_router
from App.core.config import settings
from App.core.rate_limit import limiter
from App.core.redis_client import close_redis_client, get_redis_client
from App.middleware.security_headers import SecurityHeadersMiddleware

# Ensures every model is registered on Base.metadata before anything else
# (routes, Alembic) touches the ORM.
import App.models  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await close_redis_client()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Secure Authentication API",
        description=(
            "Reusable auth service: register/login/refresh/logout with JWT "
            "access + rotating refresh tokens, RBAC, rate limiting, and "
            "account lockout. Drop the App/core + App/services layer into "
            "any other FastAPI project to reuse the same auth."
        ),
        version="1.0.0",
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        lifespan=lifespan,
    )

    # --- Rate limiting ---
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    # --- CORS: explicit allow-list, never "*" with credentials ---
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # --- Security headers on every response ---
    app.add_middleware(SecurityHeadersMiddleware)

    # --- Routers ---
    app.include_router(api_router)

    @app.get("/health", tags=["meta"])
    async def health_check():
        redis_ok = True
        try:
            redis = get_redis_client()
            await redis.ping()
        except Exception:
            redis_ok = False
        return {"status": "ok", "redis": redis_ok}

    @app.get("/scalar", include_in_schema=False)
    def get_scalar_docs():
        return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")

    return app


app = create_app()
