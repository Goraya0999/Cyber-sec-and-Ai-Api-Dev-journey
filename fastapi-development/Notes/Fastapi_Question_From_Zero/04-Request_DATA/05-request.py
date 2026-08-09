#013 How do you set a cookie in a response?

from fastapi import FastAPI, Response

app = FastAPI()


@app.post("/login")
def login(response: Response):
    """
    Sets a cookie in the response.
    """

    response.set_cookie(
        key="session_id",          # cookie name
        value="abc123",            # cookie value
        httponly=True,             # prevents JS access (security)
        secure=False,              # set True in production (HTTPS only)
        samesite="Lax"             # CSRF protection
    )

    return {"status": "logged in"}


# Professional Comment:
# ✔ Always use httponly=True to prevent XSS attacks
# ✔ Use secure=True in production (HTTPS)
# ✔ Avoid storing sensitive data directly — prefer session/token IDs
# ✔ Configure expiration (max_age / expires) for session control



#014 How do you delete a cookie?

from fastapi import FastAPI, Response

app = FastAPI()


@app.post("/logout")
def logout(response: Response):
    """
    Deletes a cookie by instructing browser to remove it.
    """

    response.delete_cookie(
        key="session_id"   # must match the cookie name exactly
    )

    return {"status": "logged out"}


# Professional Comment:
# ✔ delete_cookie() sets expiration in the past (browser removes it)
# ✔ Ensure same path/domain as when cookie was created
# ✔ Common in logout endpoints for session invalidation
# ✔ Always combine with backend session/token invalidation for security


#-------------------------
#015 How do you read a specific header from the request?

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items")
def read_header(user_agent: str = Header(None)):
    """
    Reads a specific HTTP header from the request.

    FastAPI automatically:
        - Converts header names (User-Agent → user_agent)
        - Handles case-insensitivity
    """

    return {
        "user_agent": user_agent
    }


# Example Request Headers:
"""
User-Agent: Mozilla/5.0
"""


# Professional Comment:
# ✔ Header() is used for metadata like auth tokens, client info, tracing IDs
# ✔ Use alias if header name is complex (e.g., X-API-KEY)
# ✔ Always validate critical headers (auth, API keys)
# ✔ Headers are case-insensitive but use standard naming conventions