from sqlalchemy import select

from App.models.role import Role
from tests.conftest import STRONG_PASSWORD


async def _register_and_login(client, email, password=STRONG_PASSWORD):
    await client.post("/api/v1/auth/register", json={"email": email, "password": password})
    resp = await client.post("/api/v1/auth/login", json={"email": email, "password": password})
    return resp.json()["access_token"]


async def _promote_to_admin(db_session, email: str) -> None:
    """Test helper: grant the admin role directly via the DB, bypassing the API
    (in a real deployment this would be an internal/ops-only action)."""
    async with db_session() as session:
        from App.models.user import User

        user = (await session.execute(select(User).where(User.email == email))).scalar_one()
        admin_role = (await session.execute(select(Role).where(Role.name == "admin"))).scalar_one()
        user.roles.append(admin_role)
        session.add(user)
        await session.commit()


async def test_regular_user_gets_403_on_admin_route(client):
    token = await _register_and_login(client, "user@example.com")
    resp = await client.get(
        "/api/v1/admin/users", headers={"Authorization": f"Bearer {token}"}
    )
    assert resp.status_code == 403


async def test_admin_user_can_access_admin_route(client, db_session):
    await _register_and_login(client, "admin@example.com")
    await _promote_to_admin(db_session, "admin@example.com")

    # Re-login so the new access token carries the updated roles claim.
    login_resp = await client.post(
        "/api/v1/auth/login",
        json={"email": "admin@example.com", "password": STRONG_PASSWORD},
    )
    token = login_resp.json()["access_token"]

    resp = await client.get(
        "/api/v1/admin/users", headers={"Authorization": f"Bearer {token}"}
    )
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
