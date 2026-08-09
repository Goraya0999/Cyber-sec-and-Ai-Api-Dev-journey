import pytest

from tests.conftest import STRONG_PASSWORD


async def _register(client, email="alice@example.com", password=STRONG_PASSWORD):
    return await client.post("/api/v1/auth/register", json={"email": email, "password": password})


async def _login(client, email="alice@example.com", password=STRONG_PASSWORD):
    return await client.post("/api/v1/auth/login", json={"email": email, "password": password})


async def test_register_creates_user_with_default_role(client):
    resp = await _register(client)
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "alice@example.com"
    assert body["roles"] == ["user"]
    assert "hashed_password" not in body


async def test_register_rejects_weak_password(client):
    resp = await client.post(
        "/api/v1/auth/register", json={"email": "weak@example.com", "password": "short"}
    )
    assert resp.status_code == 422


async def test_register_rejects_duplicate_email(client):
    await _register(client)
    resp = await _register(client)
    assert resp.status_code == 409


async def test_login_success_returns_token_pair(client):
    await _register(client)
    resp = await _login(client)
    assert resp.status_code == 200
    body = resp.json()
    assert "access_token" in body
    assert "refresh_token" in body
    assert body["token_type"] == "bearer"


async def test_login_wrong_password_is_generic_error(client):
    await _register(client)
    resp = await _login(client, password="WrongPassword1!")
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid credentials"


async def test_login_unknown_email_is_same_generic_error(client):
    resp = await _login(client, email="ghost@example.com")
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid credentials"


async def test_refresh_rotates_token_and_old_one_becomes_invalid(client):
    await _register(client)
    login_resp = await _login(client)
    old_refresh = login_resp.json()["refresh_token"]

    refresh_resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert refresh_resp.status_code == 200
    new_refresh = refresh_resp.json()["refresh_token"]
    assert new_refresh != old_refresh

    # Reusing the OLD (now revoked) token must fail and burn the whole family.
    reuse_resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": old_refresh})
    assert reuse_resp.status_code == 401

    # Because reuse revokes the family, even the freshly rotated token is dead now.
    new_refresh_resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": new_refresh})
    assert new_refresh_resp.status_code == 401


async def test_logout_revokes_refresh_token(client):
    await _register(client)
    login_resp = await _login(client)
    refresh_token = login_resp.json()["refresh_token"]

    logout_resp = await client.post("/api/v1/auth/logout", json={"refresh_token": refresh_token})
    assert logout_resp.status_code == 204

    refresh_resp = await client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert refresh_resp.status_code == 401


async def test_protected_endpoint_requires_token(client):
    resp = await client.get("/api/v1/users/me")
    assert resp.status_code == 401


async def test_protected_endpoint_works_with_valid_token(client):
    await _register(client)
    login_resp = await _login(client)
    access_token = login_resp.json()["access_token"]

    resp = await client.get(
        "/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"}
    )
    assert resp.status_code == 200
    assert resp.json()["email"] == "alice@example.com"


async def test_protected_endpoint_rejects_tampered_token(client):
    await _register(client)
    login_resp = await _login(client)
    access_token = login_resp.json()["access_token"]
    tampered = access_token[:-1] + ("A" if access_token[-1] != "A" else "B")

    resp = await client.get(
        "/api/v1/users/me", headers={"Authorization": f"Bearer {tampered}"}
    )
    assert resp.status_code == 401


async def test_public_endpoint_needs_no_auth(client):
    resp = await client.get("/api/v1/public/ping")
    assert resp.status_code == 200
    assert resp.json()["auth_required"] is False


async def test_health_endpoint(client):
    resp = await client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
