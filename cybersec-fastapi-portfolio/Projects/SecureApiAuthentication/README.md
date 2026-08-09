# Secure Authentication API

A production-shaped, intermediate-level FastAPI authentication & authorization
service: JWT access + rotating refresh tokens, RBAC, Redis-backed rate
limiting, and account lockout — built to be dropped into other projects as a
reusable auth layer.

## Stack

FastAPI · PostgreSQL · SQLAlchemy 2.0 (async) · Alembic · Redis · Argon2id ·
PyJWT · slowapi · Docker Compose · Pytest

## What's implemented

- **Register / Login / Refresh / Logout / Logout-all**
- **Password security** — Argon2id hashing, server-side strength policy
  (10+ chars, upper/lower/digit/symbol, common-password rejection)
- **JWT access tokens** (15 min default) + **rotating refresh tokens**
  (7 day default, stored only as a SHA-256 hash — the raw value never
  touches the DB). Reusing a revoked refresh token revokes its entire
  token family (replay/theft defense).
- **RBAC** — `admin` / `moderator` / `user` roles seeded via migration;
  `require_role()` dependency enforces access, deny-by-default
- **Account lockout** — N failed logins (default 5) locks the account for
  a cooldown window (default 15 min), tracked in Redis
- **Rate limiting** — per-IP limits on `/register` and `/login` via slowapi
  + Redis
- **Generic error messages** on login failure so responses don't leak
  whether an email exists (OWASP API2)
- **Security headers** (HSTS, X-Frame-Options, nosniff, CSP) + locked-down
  CORS
- **Non-root Docker runtime user**

### Three endpoint patterns, ready to copy into other projects

| Endpoint | Access |
|---|---|
| `GET /api/v1/public/ping` | Public — no token required |
| `GET /api/v1/users/me` | Protected — any authenticated user |
| `GET /api/v1/admin/users` | Role-protected — `admin` only |

To reuse this auth layer in another FastAPI project, copy:
`App/core/security.py`, `App/core/config.py`, `App/core/redis_client.py`,
`App/api/deps.py`, `App/services/auth_service.py`,
`App/services/lockout_service.py`, and the `App/models/` + `App/schemas/`
packages. Then wire `get_current_user` / `require_role()` into your own
routes exactly like `App/api/v1/routes_users.py` does.

## Project layout

```
App/
  main.py                 # app factory: middleware, routers, rate limiter
  core/
    config.py              # pydantic-settings, loads .env
    security.py            # password hashing + JWT helpers
    redis_client.py         # shared async Redis client
    rate_limit.py           # slowapi Limiter
  api/
    deps.py                 # get_current_user, require_role()
    v1/
      routes_auth.py        # /auth/register /login /refresh /logout
      routes_users.py       # public / protected / admin-only examples
      router.py
  models/                   # User, Role, RefreshToken (SQLAlchemy 2.0)
  schemas/                  # Pydantic request/response models
  services/
    auth_service.py         # register/login/refresh/logout business logic
    lockout_service.py       # Redis-backed failed-attempt tracking
  middleware/
    security_headers.py
  db/
    session.py               # async engine + session factory
alembic/                    # migrations (schema + role seeding)
tests/                      # pytest suite (18 tests)
```

## Running it

### 1. With Docker (recommended)

```bash
docker compose up --build
```

This starts Postgres + Redis, waits for both to be healthy, runs
`alembic upgrade head`, then starts the API on `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`.

### 2. Locally without Docker

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Point .env at a Postgres + Redis you have running, or use SQLite for a
# quick local check:
#   DATABASE_URL=sqlite+aiosqlite:///./local.db
#   REDIS_URL=redis://localhost:6379/0

alembic upgrade head
uvicorn App.main:app --reload
```

## Running the tests

```bash
pip install -r requirements.txt   # includes pytest, httpx, aiosqlite, fakeredis
pytest -v
```

The suite runs against an in-memory SQLite DB and a fake in-memory Redis
(`fakeredis`) — no external services required. Covers: registration
(including weak-password and duplicate-email rejection), login (including
the generic-error behavior for wrong password vs. unknown email), refresh
rotation + replay detection, logout, protected/public/admin-only route
access, account lockout, and rate limiting.

## Configuration

All settings load from `.env` (see `.env.example`). Notable ones:

| Variable | Default | Notes |
|---|---|---|
| `ACCESS_TOKEN_EXPIRE_MINUTES` | 15 | Keep short — limits blast radius of a stolen token |
| `REFRESH_TOKEN_EXPIRE_DAYS` | 7 | |
| `MAX_FAILED_LOGIN_ATTEMPTS` | 5 | Account lockout threshold |
| `LOCKOUT_DURATION_MINUTES` | 15 | |
| `LOGIN_RATE_LIMIT` | 10/minute | Kept above the lockout threshold so a locked-account check isn't masked by a 429 |
| `REGISTER_RATE_LIMIT` | 3/hour | |

## Known simplifications (documented, not hidden)

This is an intermediate-level reference build, not a hardened production
deployment. Before shipping to real users you'd still want to:

- Add an email-verification flow (the `is_verified` column exists but isn't
  wired to anything yet)
- Swap the tiny in-code common-password list (`App/schemas/user.py`) for a
  real top-10k list
- Add structured audit logging for auth events
- Add CI (`pytest --cov`, `pip-audit`) and pin dependency versions
- Put TLS termination in front of this (Nginx/Traefik) — the app itself
  speaks plain HTTP
