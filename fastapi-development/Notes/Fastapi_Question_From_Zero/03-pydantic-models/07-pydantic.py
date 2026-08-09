#019 How do you handle multiple request bodies (multiple models)?

# FastAPI allows multiple body parameters directly in function signature

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class User(BaseModel):
    username: str


@app.post("/items")
def create(item: Item, user: User):
    """
    FastAPI will:
        ✔ Expect BOTH objects in request body
        ✔ Validate each model separately
        ✔ Combine them into function arguments

    Request body structure:
    {
        "item": {...},
        "user": {...}
    }
    """
    return {"item": item, "user": user}


#-------------------------


#020 How do you create an update schema that makes all fields optional?

# Common pattern for PATCH / update APIs

from typing import Optional


class ItemUpdate(BaseModel):
    """
    All fields optional:
        ✔ Allows partial updates
        ✔ Only provided fields will be updated
    """
    name: Optional[str] = None
    price: Optional[float] = None


# Example:
"""
{
  "price": 100.0
}
"""
# Only price will be updated


#-------------------------


#021 How do you define a model with a dict field?

# Use Dict[key_type, value_type]

from typing import Dict


class Config(BaseModel):
    """
    settings:
        - Dictionary with string keys and string values
        - Default is empty dict
    """
    settings: Dict[str, str] = {}


# Example input:
"""
{
  "settings": {
    "theme": "dark",
    "language": "en"
  }
}
"""


# Professional Note:
# Avoid using mutable defaults like {} directly in production.
# Better approach:
# settings: Dict[str, str] = Field(default_factory=dict)