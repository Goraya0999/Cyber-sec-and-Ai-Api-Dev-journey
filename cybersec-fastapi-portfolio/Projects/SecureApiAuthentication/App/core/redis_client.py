from redis.asyncio import Redis, from_url

from App.core.config import settings

_redis: Redis | None = None


def get_redis_client() -> Redis:
    """
    Lazily creates a single shared async Redis client.

    A module-level singleton is fine here because redis-py's async client is
    connection-pooled and safe to share across requests/tasks.
    """
    global _redis
    if _redis is None:
        _redis = from_url(settings.REDIS_URL, decode_responses=True)
    return _redis


async def close_redis_client() -> None:
    global _redis
    if _redis is not None:
        await _redis.close()
        _redis = None
