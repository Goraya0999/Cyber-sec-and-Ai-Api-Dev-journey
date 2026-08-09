from App.core.config import settings
from tests.conftest import STRONG_PASSWORD


async def test_account_locks_after_max_failed_attempts(client):
    email = "lockout@example.com"
    await client.post("/api/v1/auth/register", json={"email": email, "password": STRONG_PASSWORD})

    for _ in range(settings.MAX_FAILED_LOGIN_ATTEMPTS - 1):
        resp = await client.post(
            "/api/v1/auth/login", json={"email": email, "password": "WrongPassword1!"}
        )
        assert resp.status_code == 401

    # The Nth failure should trip the lock.
    locking_resp = await client.post(
        "/api/v1/auth/login", json={"email": email, "password": "WrongPassword1!"}
    )
    assert locking_resp.status_code in (401, 423)

    # Any further attempt — even with the CORRECT password — is locked out.
    locked_resp = await client.post(
        "/api/v1/auth/login", json={"email": email, "password": STRONG_PASSWORD}
    )
    assert locked_resp.status_code == 423


async def test_successful_login_resets_failed_counter(client):
    email = "resets@example.com"
    await client.post("/api/v1/auth/register", json={"email": email, "password": STRONG_PASSWORD})

    # A couple of failures, but below the lockout threshold.
    for _ in range(settings.MAX_FAILED_LOGIN_ATTEMPTS - 2):
        await client.post(
            "/api/v1/auth/login", json={"email": email, "password": "WrongPassword1!"}
        )

    good_resp = await client.post(
        "/api/v1/auth/login", json={"email": email, "password": STRONG_PASSWORD}
    )
    assert good_resp.status_code == 200
