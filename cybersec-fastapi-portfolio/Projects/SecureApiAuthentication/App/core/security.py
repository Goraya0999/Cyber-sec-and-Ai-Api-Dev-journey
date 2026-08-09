"""
Security primitives: password hashing and JWT handling.

Kept deliberately separate from route handlers and services so it can be
unit-tested in isolation and reused by any other project that needs the
same auth logic (see README for how to lift this whole App/core + App/services
layer into another FastAPI service).
"""
from __future__ import annotations

import hashlib
import secrets
import uuid
from datetime import datetime, timedelta, timezone
from enum import StrEnum

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError

from App.core.config import settings

# --- Password hashing (Argon2id) ---------------------------------------
# time_cost/memory_cost/parallelism are OWASP-recommended baseline values.
_password_hasher = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)


def hash_password(raw_password: str) -> str:
    return _password_hasher.hash(raw_password)


def verify_password(raw_password: str, hashed_password: str) -> bool:
    try:
        return _password_hasher.verify(hashed_password, raw_password)
    except (VerifyMismatchError, InvalidHashError):
        return False


def needs_rehash(hashed_password: str) -> bool:
    """True if the hash was made with outdated parameters and should be refreshed."""
    return _password_hasher.check_needs_rehash(hashed_password)


# --- JWT access tokens (stateless) --------------------------------------
class TokenType(StrEnum):
    ACCESS = "access"
    REFRESH = "refresh"


def create_access_token(user_id: str, roles: list[str]) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "roles": roles,
        "type": TokenType.ACCESS.value,
        "iat": now,
        "exp": now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        "jti": str(uuid.uuid4()),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    """Raises jwt.PyJWTError subclasses on invalid/expired/tampered tokens."""
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])


# --- Refresh tokens (opaque, stored as hash server-side) -----------------
def generate_refresh_token() -> tuple[str, str]:
    """Returns (raw_token_for_client, sha256_hash_for_db)."""
    raw = secrets.token_urlsafe(48)
    token_hash = hash_refresh_token(raw)
    return raw, token_hash


def hash_refresh_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()
