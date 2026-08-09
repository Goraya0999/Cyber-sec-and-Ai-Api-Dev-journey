"""


Topic:
What packages are required for JWT Authentication in FastAPI?

JWT Authentication usually requires two major components:

1. Password Hashing
2. JWT Token Generation & Verification

Required Packages:

pip install python-jose[cryptography]
pip install passlib[bcrypt]

Or install together:

pip install python-jose[cryptography] passlib[bcrypt]

---------------------------------------------------------
Package 1: python-jose
---------------------------------------------------------

Used for:

- Creating JWT tokens
- Verifying JWT tokens
- Decoding JWT tokens
- Checking expiration time
- Checking token signature

Import:

from jose import jwt

Example:

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

---------------------------------------------------------
Package 2: passlib
---------------------------------------------------------

Used for:

- Password hashing
- Password verification

Never store plain passwords in database.

BAD:

password = "admin123"

GOOD:

password = "$2b$12$abcxyz...."

Import:

from passlib.context import CryptContext

Example:

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

hashed = pwd_context.hash("admin123")

verified = pwd_context.verify(
    "admin123",
    hashed
)

---------------------------------------------------------
Why Both Packages?
---------------------------------------------------------

User Registration:

Password
    ↓
Hash Password
    ↓
Store in Database

User Login:

Entered Password
    ↓
Verify Hash
    ↓
Generate JWT Token
    ↓
Return Token

Future Requests:

Bearer Token
    ↓
Verify JWT
    ↓
Allow Access

---------------------------------------------------------
Interview Answer
---------------------------------------------------------

Q: What packages are required for JWT authentication?

A:

python-jose[cryptography]
    → JWT creation and validation

passlib[bcrypt]
    → Password hashing and verification
"""