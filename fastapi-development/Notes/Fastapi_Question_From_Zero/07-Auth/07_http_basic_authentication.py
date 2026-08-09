# 009_http_basic_authentication.py

```python
"""
File: 009_http_basic_authentication.py

Topic:
How do you use HTTP Basic Authentication in FastAPI?

Definition:

HTTP Basic Authentication is one of the simplest
authentication methods.

The client sends:

username + password

encoded using Base64 inside the Authorization header.

Example Header:

Authorization: Basic YWRtaW46MTIzNDU=

The encoded value contains:

admin:12345

IMPORTANT:

HTTP Basic Authentication is NOT encrypted.
Always use HTTPS in production.
"""

from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

# ---------------------------------------------------------
# Create HTTP Basic Security Object
# ---------------------------------------------------------
#
# This tells FastAPI:
# "Extract username and password from
# Authorization: Basic <credentials>"
#
# ---------------------------------------------------------

security = HTTPBasic()


@app.get("/basic")
def basic_login(
    credentials: HTTPBasicCredentials = Depends(security)
):
    """
    FastAPI automatically extracts:

    username
    password

    from the Authorization header.
    """

    return {
        "username": credentials.username,
        "password": credentials.password
    }


"""
===========================================================
Example Request
===========================================================

Username: admin
Password: 12345

Header:

Authorization: Basic YWRtaW46MTIzNDU=

===========================================================
Response
===========================================================

{
    "username": "admin",
    "password": "12345"
}

===========================================================
Authentication Flow
===========================================================

Client
    │
    ▼
Username + Password
    │
    ▼
Base64 Encode
    │
    ▼
Authorization Header
    │
    ▼
HTTPBasic
    │
    ▼
HTTPBasicCredentials
    │
    ▼
Extract Username & Password
    │
    ▼
Access Granted

===========================================================
Interview Answer
===========================================================

from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials
)

security = HTTPBasic()

@app.get("/basic")
def basic(
    creds: HTTPBasicCredentials =
    Depends(security)
):
    return {
        "user": creds.username
    }
"""
```

# 010_api_key_header_authentication.py

```python
"""
File: 010_api_key_header_authentication.py

Topic:
How do you use API Key Authentication via Header?

Definition:

API Key Authentication is commonly used for:

- Internal APIs
- Microservices
- Third-party integrations
- Service-to-Service communication

Instead of sending username/password,
the client sends an API key.

Example:

X-API-Key: secret123
"""

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader

app = FastAPI()

# ---------------------------------------------------------
# Create API Key Header Security Scheme
# ---------------------------------------------------------
#
# FastAPI will look for:
#
# X-API-Key: some_key
#
# ---------------------------------------------------------

api_key_header = APIKeyHeader(
    name="X-API-Key"
)

# Valid API Key
VALID_API_KEY = "secret"


@app.get("/secure")
def secure(
    key: str = Depends(api_key_header)
):
    """
    FastAPI extracts the value from:

    X-API-Key header
    """

    if key != VALID_API_KEY:

        raise HTTPException(
            status_code=403,
            detail="Bad API Key"
        )

    return {
        "ok": True,
        "message": "Access Granted"
    }


"""
===========================================================
Valid Request
===========================================================

GET /secure

Headers:

X-API-Key: secret

===========================================================
Response
===========================================================

{
    "ok": true,
    "message": "Access Granted"
}

===========================================================
Invalid Request
===========================================================

GET /secure

Headers:

X-API-Key: wrong_key

===========================================================
Response
===========================================================

403 Forbidden

{
    "detail": "Bad API Key"
}

===========================================================
Authentication Flow
===========================================================

Client
    │
    ▼
Send API Key
    │
    ▼
X-API-Key Header
    │
    ▼
APIKeyHeader
    │
    ▼
Extract Key
    │
    ▼
Validate Key
    │
 ┌──┴──┐
 │     │
Valid Invalid
 │     │
 ▼     ▼
Allow 403

===========================================================
Interview Answer
===========================================================

from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(
    name="X-API-Key"
)

@app.get("/secure")
def secure(
    key: str = Depends(api_key_header)
):

    if key != "secret":
        raise HTTPException(
            403,
            "Bad key"
        )

    return {
        "ok": True
    }
"""
```
