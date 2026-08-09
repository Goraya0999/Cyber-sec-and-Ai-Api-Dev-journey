"""
Account lockout defends against distributed brute-force attempts that a
per-IP rate limit alone would miss (the attacker just uses many IPs).

Counters live in Redis with a TTL so they self-expire — no cleanup job
needed. We key on email (not user id) so we can reject attempts against
emails that don't even exist without leaking that fact to the caller.
"""
from __future__ import annotations

from redis.asyncio import Redis

from App.core.config import settings

_FAILED_KEY = "auth:failed_login:{email}"
_LOCK_KEY = "auth:locked:{email}"


def _norm(email: str) -> str:
    return email.strip().lower()


async def is_locked(redis: Redis, email: str) -> bool:
    return await redis.exists(_LOCK_KEY.format(email=_norm(email))) == 1


async def register_failed_attempt(redis: Redis, email: str) -> int:
    """Increments the failure counter and locks the account if the threshold is hit.

    Returns the current failure count.
    """
    key = _FAILED_KEY.format(email=_norm(email))
    window_seconds = settings.LOCKOUT_DURATION_MINUTES * 60

    count = await redis.incr(key)
    if count == 1:
        await redis.expire(key, window_seconds)

    if count >= settings.MAX_FAILED_LOGIN_ATTEMPTS:
        await redis.set(_LOCK_KEY.format(email=_norm(email)), "1", ex=window_seconds)

    return count


async def reset_failed_attempts(redis: Redis, email: str) -> None:
    email = _norm(email)
    await redis.delete(_FAILED_KEY.format(email=email))
    await redis.delete(_LOCK_KEY.format(email=email))
