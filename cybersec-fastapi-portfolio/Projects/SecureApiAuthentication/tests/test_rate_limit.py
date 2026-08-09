from App.core.config import settings
from tests.conftest import STRONG_PASSWORD


async def test_login_endpoint_rate_limits_after_threshold(client):
    """LOGIN_RATE_LIMIT (default 10/minute, see settings) is applied via
    @limiter.limit on the route. One request past the threshold should 429."""
    email = "ratelimit@example.com"
    await client.post("/api/v1/auth/register", json={"email": email, "password": STRONG_PASSWORD})

    limit_count = int(settings.LOGIN_RATE_LIMIT.split("/")[0])
    statuses = []
    for _ in range(limit_count + 1):
        resp = await client.post(
            "/api/v1/auth/login", json={"email": email, "password": "WrongPassword1!"}
        )
        statuses.append(resp.status_code)

    # At least one request should have been throttled with 429.
    assert 429 in statuses
