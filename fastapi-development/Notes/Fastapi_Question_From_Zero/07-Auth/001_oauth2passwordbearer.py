"""

What is OAuth2PasswordBearer in FastAPI?

Definition:
OAuth2PasswordBearer is a FastAPI security utility that:

1. Reads Bearer tokens from the Authorization header.
2. Automatically validates the format.
3. Provides integration with Swagger UI (/docs).
4. Passes the token value to your route function.

Example Header:

Authorization: Bearer abc123xyz

FastAPI extracts:
abc123xyz

and provides it as a parameter.
"""

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# ---------------------------------------------------------
# OAuth2PasswordBearer
# ---------------------------------------------------------
#
# tokenUrl:
# This tells Swagger/OpenAPI where users can obtain a token.
#
# IMPORTANT:
# It DOES NOT create the endpoint automatically.
#
# You must create the "/token" endpoint yourself.
#
# When using Swagger UI:
# 1. Click "Authorize"
# 2. Enter username/password
# 3. Swagger calls /token
# 4. Receives token
# 5. Uses token in future requests
#
# ---------------------------------------------------------

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/profile")
async def get_profile(token: str = Depends(oauth2_scheme)):
    """
    OAuth2PasswordBearer extracts the token from:

    Authorization: Bearer my_secret_token

    token becomes:
    "my_secret_token"
    """

    return {
        "message": "Authenticated user",
        "received_token": token
    }


"""
Request:

GET /profile

Headers:
Authorization: Bearer abc123

Response:
{
    "message": "Authenticated user",
    "received_token": "abc123"
}

Without Header:

401 Unauthorized
"""

