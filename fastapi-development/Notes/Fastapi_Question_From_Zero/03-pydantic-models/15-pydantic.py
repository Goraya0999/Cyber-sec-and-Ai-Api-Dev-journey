#043 How do you make a Pydantic field immutable?

# Use ConfigDict(frozen=True)
# to make the entire model immutable after creation.
# Fields become read-only and cannot be modified.

from pydantic import BaseModel, ConfigDict


class ImmutableItem(BaseModel):
    """
    Fields:
        name → required string

    Rules:
        - Model is immutable after instantiation
        - Field values cannot be changed
    """
    model_config = ConfigDict(frozen=True)

    name: str


# Example
item = ImmutableItem(name="Laptop")

print(item)

# Output:
# name='Laptop'


# Attempt to modify
# item.name = "Phone"
#
# ValidationError:
# Instance is frozen


# Professional Note:
# - frozen=True makes all fields read-only.
# - Similar to immutable objects in other languages.
# - Useful for:
#     • Configuration objects
#     • Domain entities
#     • Data that should never change
# - Helps prevent accidental modifications.
# - If only some fields need protection,
#   custom validation may be required.


#-------------------------


#044 What is model_validate() in Pydantic v2?

# model_validate() creates and validates a model
# instance from a dictionary, object, or other input.
# It replaces parse_obj() from Pydantic v1.

from pydantic import BaseModel


class Item(BaseModel):
    """
    Fields:
        name  → required string
        price → required float
    """
    name: str
    price: float


# Create model from dictionary
item = Item.model_validate(
    {
        "name": "Widget",
        "price": 5.0
    }
)

print(item)

# Output:
# name='Widget' price=5.0


# Automatic type conversion
item2 = Item.model_validate(
    {
        "name": "Phone",
        "price": "1000"
    }
)

print(item2)

# Output:
# name='Phone' price=1000.0


# Professional Note:
# - model_validate() is the recommended method
#   for creating models from external data.
# - Replaces:
#       parse_obj()
#   from Pydantic v1.
# - Performs:
#     • Validation
#     • Type conversion
#     • Error reporting
# - Commonly used with:
#     • API payloads
#     • Database records
#     • External JSON data


#-------------------------


#045 How do you create a TypeAlias for complex nested types?

# Use a type alias to give a meaningful name
# to complex type definitions.

from typing import List
from pydantic import BaseModel


# Type Alias
Matrix = List[List[float]]


class Transform(BaseModel):
    """
    Fields:
        matrix → 2D list of floating-point values

    Notes:
        - Matrix is a custom type alias
        - Improves readability
    """
    matrix: Matrix


# Example
transform = Transform(
    matrix=[
        [1.0, 0.0],
        [0.0, 1.0]
    ]
)

print(transform)

# Output:
# matrix=[[1.0, 0.0], [0.0, 1.0]]


# Professional Note:
# - Type aliases improve code readability.
# - Useful for:
#     • Matrices
#     • Nested JSON structures
#     • API response formats
#     • Configuration schemas
# - Instead of repeating complex types everywhere,
#   define them once and reuse them.
# - Makes large projects easier to maintain.


#-------------------------