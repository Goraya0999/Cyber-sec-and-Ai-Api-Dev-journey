# 006_decode_jwt_token.py

#```python
"""
File: 006_decode_jwt_token.py

Topic:
How do you verify and decode a JWT token?

Definition:

When a user sends a JWT token to a protected endpoint,
the server must verify:

1. Token signature
2. Secret key
3. Expiration time
4. Token integrity

After verification, the payload can be extracted.

Example JWT Payload:

{
    "sub": "admin",
    "exp": 1750000000
}

sub = username
exp = expiration timestamp
"""

from jose import jwt, JWTError
from fastapi import HTTPException

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def decode_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token payload"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


"""
Example:

token = "eyJhbGciOiJIUzI1NiIs..."

username = decode_token(token)

print(username)

Output:

admin
"""

# Interview Answer

"""
from jose import jwt, JWTError

def decode_token(token: str):

    try:
        data = jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]
        )

        return data.get("sub")

    except JWTError:
        raise HTTPException(
            401,
            "Invalid token"
        )
"""
```

# 007_hash_password_passlib.py

```python
"""
File: 007_hash_password_passlib.py

Topic:
How do you hash a password using passlib?

Definition:

Passwords should NEVER be stored as plain text.

BAD:

password = "admin123"

GOOD:

password = "$2b$12$kjshd78sdh..."

Hashing converts a password into a secure string
that cannot be reversed.
"""

from passlib.context import CryptContext

# Create hashing context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Hash Password
def hash_password(password: str):

    return pwd_context.hash(password)


# Verify Password
def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# Example Usage

hashed_password = hash_password("mypassword")

print("Hashed Password:")
print(hashed_password)

is_valid = verify_password(
    "mypassword",
    hashed_password
)

print("Password Match:", is_valid)

"""
Output:

Hashed Password:
$2b$12$abcxyz123...

Password Match:
True
"""

# Interview Answer

"""
from passlib.context import CryptContext

pwd_ctx = CryptContext(
    schemes=["bcrypt"]
)

hashed = pwd_ctx.hash("mypassword")

valid = pwd_ctx.verify(
    "mypassword",
    hashed
)

# True
"""
```

# 008_get_current_user_dependency.py

```python
"""
File: 008_get_current_user_dependency.py

Topic:
How do you get the current user from a token using a dependency?

Definition:

A dependency is a reusable function that runs
before a route executes.

Common Authentication Flow:

Token
  ↓
Decode Token
  ↓
Extract Username
  ↓
Find User
  ↓
Return User Object
"""

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)


# Fake Database

fake_users_db = {
    "admin": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com"
    }
}


# Fake Token Decoder

def decode_token(token: str):

    if token == "token_for_admin":
        return "admin"

    return None


# Get User From Database

def get_user(username: str):

    return fake_users_db.get(username)


# Authentication Dependency

async def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    username = decode_token(token)

    if not username:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = get_user(username)

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    return user


"""
Usage Example:

@app.get("/profile")
async def profile(
    current_user = Depends(get_current_user)
):
    return current_user
"""

"""
Request:

GET /profile

Authorization:
Bearer token_for_admin

Response:

{
    "id": 1,
    "username": "admin",
    "email": "admin@example.com"
}
"""

# Interview Answer

"""
async def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    username = decode_token(token)

    user = get_user(username)

    if not user:
        raise HTTPException(
            401,
            "Not authenticated"
        )

    return user
"""
```
