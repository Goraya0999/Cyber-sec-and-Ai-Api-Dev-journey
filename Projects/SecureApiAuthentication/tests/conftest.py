import os

# Must run before any `App.*` import: pydantic-settings loads Settings()
# at module import time, and real environment variables take precedence
# over values from .env. This keeps the test suite fully self-contained —
# no real Postgres/Redis needed — while leaving the project's own .env
# (used by docker-compose) untouched.
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")
os.environ.setdefault("RATE_LIMIT_STORAGE_URI", "memory://")
os.environ.setdefault("JWT_SECRET", "test-secret-not-for-production-use-only-32bytes")
os.environ.setdefault("DEBUG", "true")

import asyncio
from collections.abc import AsyncGenerator

import fakeredis.aioredis
import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from App.api.deps import get_redis
from App.core.rate_limit import limiter
from App.db.session import Base, get_db
from App.main import app
from App.models.role import ALL_ROLES, Role

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(autouse=True)
def _reset_rate_limiter():
    """Rate-limit storage is process-global; without this, unrelated tests
    would trip each other's login/register limits since they share an IP."""
    limiter.reset()
    yield
    limiter.reset()


@pytest_asyncio.fixture
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Fresh in-memory SQLite DB per test, roles pre-seeded like the real migration does."""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_factory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with session_factory() as session:
        session.add_all([Role(name=name) for name in ALL_ROLES])
        await session.commit()

    yield session_factory

    await engine.dispose()


@pytest_asyncio.fixture
async def fake_redis():
    client = fakeredis.aioredis.FakeRedis(decode_responses=True)
    yield client
    await client.aclose()


@pytest_asyncio.fixture
async def client(db_session, fake_redis) -> AsyncGenerator[AsyncClient, None]:
    async def _get_db_override():
        async with db_session() as session:
            yield session

    async def _get_redis_override():
        return fake_redis

    app.dependency_overrides[get_db] = _get_db_override
    app.dependency_overrides[get_redis] = _get_redis_override

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()


STRONG_PASSWORD = "Str0ng!Passw0rd"
