"""


Topic:
How do you protect a route so it requires authentication?

Definition:
A protected route is an endpoint that can only be accessed
by authenticated users.

Authentication Flow:

1. User logs in.
2. Server returns an access token.
3. User sends token in Authorization header.
4. FastAPI extracts token using OAuth2PasswordBearer.
5. Token is validated.
6. User is allowed to access the route.

Without a valid token:
401 Unauthorized

With a valid token:
Access Granted
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# ---------------------------------------------------------
# OAuth2 Security Scheme
# ---------------------------------------------------------
#
# FastAPI expects:
#
# Authorization: Bearer <token>
#
# Example:
#
# Authorization: Bearer token_for_admin
#
# OAuth2PasswordBearer extracts:
# token_for_admin
#
# and passes it to the route function.
# ---------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# ---------------------------------------------------------
# Fake User Database
# ---------------------------------------------------------

fake_users_db = {
    "admin": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com"
    },
    "john": {
        "id": 2,
        "username": "john",
        "email": "john@example.com"
    }
}


# ---------------------------------------------------------
# Decode Token Function
# ---------------------------------------------------------
#
# Real Applications:
# - Verify JWT signature
# - Verify expiration time
# - Verify secret key
#
# Example JWT Payload:
#
# {
#   "sub": "admin",
#   "exp": 1712345678
# }
#
# For learning purposes:
# We use simple fake tokens.
#
# token_for_admin
# token_for_john
#
# ---------------------------------------------------------

def decode_token(token: str):

    # Token format validation
    if not token.startswith("token_for_"):
        return None

    # Extract username
    username = token.replace("token_for_", "")

    # Find user
    user = fake_users_db.get(username)

    return user


# ---------------------------------------------------------
# Public Route
# ---------------------------------------------------------
#
# Anyone can access this endpoint.
# No token required.
#
# ---------------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Public Endpoint"
    }


# ---------------------------------------------------------
# Protected Route
# ---------------------------------------------------------
#
# Depends(oauth2_scheme):
# 1. Reads Authorization header
# 2. Extracts Bearer token
# 3. Passes token to variable
#
# Example:
#
# Authorization: Bearer token_for_admin
#
# token = "token_for_admin"
#
# ---------------------------------------------------------

@app.get("/me")
def me(token: str = Depends(oauth2_scheme)):

    # Validate token
    user = decode_token(token)

    # Invalid token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    # Return authenticated user
    return {
        "message": "Authentication successful",
        "user": user
    }


"""
===========================================================
Example 1: Valid Request
===========================================================

GET /me

Headers:
Authorization: Bearer token_for_admin


Response:

{
    "message": "Authentication successful",
    "user": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com"
    }
}


===========================================================
Example 2: Missing Token
===========================================================

GET /me


Response:

401 Unauthorized


{
    "detail": "Not authenticated"
}


===========================================================
Example 3: Invalid Token
===========================================================

GET /me

Headers:
Authorization: Bearer wrong_token


Response:

401 Unauthorized


{
    "detail": "Invalid or expired token"
}


===========================================================
Key Concept
===========================================================

Public Route:

@app.get("/")
def home():
    return {"message": "Anyone can access"}

Protected Route:

@app.get("/me")
def me(token: str = Depends(oauth2_scheme)):
    ...

Depends(oauth2_scheme)

means:

"Before executing this route,
extract the Bearer token from the request."

Without token:
Access Denied

With valid token:
Access Granted
"""