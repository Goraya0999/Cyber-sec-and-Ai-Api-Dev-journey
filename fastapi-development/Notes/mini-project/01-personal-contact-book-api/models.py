from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from enum import Enum
import re


class ContactCategory(str, Enum):
    family     = "family"
    friend     = "friend"
    colleague  = "colleague"
    other      = "other"


class ContactBase(BaseModel):
    name:     str             = Field(..., min_length=2, max_length=100, example="Ali Hassan")
    email:    Optional[EmailStr] = None
    phone:    Optional[str]   = Field(None, example="+923001234567")
    category: ContactCategory = ContactCategory.other
    notes:    Optional[str]   = Field(None, max_length=500)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v):
        if v and not re.match(r'^\+?[1-9]\d{7,14}$', v):
            raise ValueError("Invalid phone number format")
        return v


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name:     Optional[str]             = Field(None, min_length=2, max_length=100)
    email:    Optional[EmailStr]        = None
    phone:    Optional[str]             = None
    category: Optional[ContactCategory] = None
    notes:    Optional[str]             = None


class ContactResponse(ContactBase):
    id:         int
    created_at: str