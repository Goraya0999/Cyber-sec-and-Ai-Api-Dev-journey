import re
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator

# Deliberately small embedded list — swap for a proper top-10k common
# password list file in a real deployment (see services/auth_service.py).
_COMMON_PASSWORDS = {
    "password", "password1", "123456789", "qwertyuiop", "letmein123",
    "admin12345", "welcome123", "iloveyou1", "123456780", "password123",
}

_PASSWORD_RULES = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{10,}$"
)


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=10, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        if value.lower() in _COMMON_PASSWORDS:
            raise ValueError("This password is too common. Choose a stronger one.")
        if not _PASSWORD_RULES.match(value):
            raise ValueError(
                "Password must be at least 10 characters and include an "
                "uppercase letter, a lowercase letter, a digit, and a symbol."
            )
        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool
    is_verified: bool
    roles: list[str]

    model_config = {"from_attributes": True}

    @classmethod
    def from_user(cls, user) -> "UserOut":
        return cls(
            id=user.id,
            email=user.email,
            is_active=user.is_active,
            is_verified=user.is_verified,
            roles=user.role_names,
        )
