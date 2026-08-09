#016 What does response_model_exclude_unset=True do?

# It removes fields that were NOT explicitly provided by the user
# (i.e., fields still holding default values)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float = 0.0
    description: str | None = None


@app.get("/items", response_model=Item, response_model_exclude_unset=True)
def get_item():
    """
    Only fields that were explicitly set will be returned.

    Useful in:
        ✔ PATCH APIs (partial updates)
        ✔ Clean responses without default noise
    """
    return {
        "name": "Laptop"
        # price and description not included → will be excluded in response
    }


#-------------------------


#017 How do you define a model with a list of nested models?

# You can combine List + nested BaseModel

from typing import List
from pydantic import BaseModel


class Tag(BaseModel):
    name: str


class Post(BaseModel):
    """
    tags:
        - List of Tag objects
        - Default is empty list
    """
    title: str
    tags: List[Tag] = []


# Example input:
"""
{
  "title": "FastAPI Guide",
  "tags": [
    {"name": "python"},
    {"name": "api"}
  ]
}
"""


#-------------------------


#018 What is the difference between BaseModel and dataclasses in FastAPI?

# Comparison:

from dataclasses import dataclass


@dataclass
class UserDC:
    name: str
    age: int


class UserModel(BaseModel):
    name: str
    age: int


"""
BaseModel (Pydantic):
    ✔ Automatic validation (type checking, constraints)
    ✔ Serialization (model_dump → dict)
    ✔ JSON schema generation (Swagger docs)
    ✔ Error handling (422 responses)

dataclasses:
    ✔ Lightweight and faster
    ❌ No built-in validation
    ❌ No automatic API docs support
    ❌ Needs Pydantic integration for validation

Professional Insight:
    - Use BaseModel for APIs (recommended)
    - Use dataclasses for internal logic or simple structures
"""