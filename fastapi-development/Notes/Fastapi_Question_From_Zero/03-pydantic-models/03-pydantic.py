#007 What is a response model and how do you use it?

# response_model is used to:
# ✔ Validate output data
# ✔ Filter sensitive/internal fields
# ✔ Control what API returns to client

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class UserOut(BaseModel):
    id: int
    username: str
    # password is intentionally NOT included


@app.get("/users/{id}", response_model=UserOut)
def get_user(id: int):
    """
    Even if the returned data contains extra fields (like password),
    FastAPI will:
        - Remove unwanted fields
        - Return only fields defined in UserOut
    """
    return {
        "id": id,
        "username": "admin",
        "password": "secret123"   # ❌ Will be hidden automatically
    }


#-------------------------


#008 How do you nest Pydantic models?

# You can use one Pydantic model inside another

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    name: str
    address: Address   # Nested model


# Example input:
"""
{
  "name": "Ali",
  "address": {
    "street": "Main Road",
    "city": "Faisalabad"
  }
}
"""


#-------------------------


#009 How do you define a list field in a Pydantic model?

# Use List from typing

from typing import List


class Order(BaseModel):
    """
    items:
        - List of strings

    quantities:
        - List of integers
        - Default is empty list
    """
    items: List[str]
    quantities: List[int] = []


# Example input:
"""
{
  "items": ["apple", "banana"],
  "quantities": [2, 5]
}
"""