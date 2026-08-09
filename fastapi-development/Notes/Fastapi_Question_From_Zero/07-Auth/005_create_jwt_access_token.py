"""


Topic:
How do you create a JWT Access Token?

Definition:

JWT (JSON Web Token) is a signed token that contains
information about a user.

A JWT consists of:

HEADER.PAYLOAD.SIGNATURE

Example:

eyJhbGciOiJIUzI1Ni...
eyJzdWIiOiJhZG1pbiJ9...
abcxyz123...

---------------------------------------------------------
JWT Payload
---------------------------------------------------------

Typical Payload:

{
    "sub": "admin",
    "exp": 1712345678
}

sub = Subject (username/user id)

exp = Expiration Time

---------------------------------------------------------
Required Installation
---------------------------------------------------------

pip install python-jose[cryptography]
"""

from jose import jwt
from datetime import datetime, timedelta

# ---------------------------------------------------------
# Secret Key
# ---------------------------------------------------------
#
# Used to sign JWT tokens.
#
# In production:
#
# Store in:
# .env file
#
# Example:
# SECRET_KEY=super-secret-key
#
# Never hardcode secrets in real applications.
# ---------------------------------------------------------

SECRET_KEY = "your-secret-key"

# JWT Signing Algorithm
ALGORITHM = "HS256"

# Token Expiration Time
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ---------------------------------------------------------
# Create JWT Token
# ---------------------------------------------------------
#
# Input:
# username
#
# Output:
# JWT Token String
#
# ---------------------------------------------------------

def create_access_token(username: str) -> str:

    # Expiration time
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Payload data
    payload = {
        "sub": username,
        "exp": expire
    }

    # Generate JWT Token
    access_token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return access_token


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

token = create_access_token("admin")

print("Generated Token:")
print(token)

"""
Sample Output:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcxMjM0NTY3OH0
.
XyzAbc123Signature

Actual token will be one long string.
"""

# ---------------------------------------------------------
# Understanding the Payload
# ---------------------------------------------------------
#
# {
#     "sub": "admin",
#     "exp": "2026-06-14 10:30:00"
# }
#
# sub
# ----
# Subject
# Usually username or user ID
#
# exp
# ----
# Expiration Time
#
# After expiration:
#
# jwt.decode(...)
#
# raises an exception.
#
# ---------------------------------------------------------


"""
===========================================================
Authentication Flow
===========================================================

User Login
    │
    ▼
Username + Password
    │
    ▼
Validate User
    │
    ▼
Create JWT Token
    │
    ▼
Return Token
    │
    ▼
Store Token
    │
    ▼
Authorization:
Bearer <token>
    │
    ▼
Protected Route
    │
    ▼
Verify Token
    │
    ▼
Access Granted

===========================================================
Interview Answer
===========================================================

from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret"

def create_token(username: str):

    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

Explanation:

sub → stores username

exp → token expiration time

jwt.encode() → generates signed JWT token
"""