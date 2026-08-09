#025 How do you parse JSON into a Pydantic model?

# Use model_validate_json() to directly parse JSON string into a model

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float


# JSON → Model
item = Item.model_validate_json('{"name": "Widget", "price": 5.0}')

print(item)
# Item(name='Widget', price=5.0)


# Professional Insight:
# - Validates JSON while parsing
# - Raises error if structure/types are incorrect
# - Cleaner than manual json.loads() + model init


#-------------------------


#026 What is orm_mode (or from_attributes) in Pydantic?

# In Pydantic v2 → use from_attributes=True
# Allows model to read data from object attributes instead of dict

from pydantic import ConfigDict


class ItemOut(BaseModel):
    """
    Enables compatibility with:
        ✔ ORM models (SQLAlchemy, Django ORM)
        ✔ Any object with attributes
    """
    model_config = ConfigDict(from_attributes=True)

    name: str
    price: float


# Example ORM-like object
class DBItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


db_item = DBItem("Laptop", 1200.0)

# Convert ORM → Pydantic model
item = ItemOut.model_validate(db_item)

print(item)
# ItemOut(name='Laptop', price=1200.0)


#-------------------------


#027 How do you use a Literal type in a Pydantic model?

# Literal restricts a field to specific allowed values

from typing import Literal


class Event(BaseModel):
    """
    type:
        - Must be one of predefined values
        - Prevents invalid inputs
    """
    type: Literal["click", "scroll", "submit"]


# Example:
event1 = Event(type="click")   # ✅ Valid
# event2 = Event(type="hover") # ❌ Validation error


# Professional Note:
# Use Literal when:
# ✔ You have fixed set of allowed values
# ✔ You want strict validation (better than plain str)