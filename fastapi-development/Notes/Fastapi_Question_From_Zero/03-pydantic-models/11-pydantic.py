#031 How do you compute a field's value dynamically?

# Use @computed_field in Pydantic v2.
# A computed field is not provided by the user.
# Instead, its value is calculated dynamically from other fields.

from pydantic import BaseModel, computed_field


class Rectangle(BaseModel):
    """
    Fields:
        width   → required float
        height  → required float
        area    → computed automatically

    Notes:
        - area is calculated from width and height
        - User does not need to provide area
        - Included in model serialization/output
    """
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height


# Example
rect = Rectangle(width=5, height=4)

print(rect.area)
# Output:
# 20.0

print(rect.model_dump())
# Output:
# {
#     'width': 5.0,
#     'height': 4.0,
#     'area': 20.0
# }


# Professional Note:
# - @computed_field is available in Pydantic v2.
# - Useful for derived values such as:
#     • area of a rectangle
#     • total price
#     • full name
#     • age calculated from date of birth
# - The value is generated dynamically whenever accessed.
# - Reduces data duplication because derived values
#   do not need to be stored separately.


#-------------------------
#032 How do you define a model with a datetime field?

# Use Python's datetime type as a field.
# Pydantic automatically parses and validates
# datetime values from strings or datetime objects.

from datetime import datetime
from pydantic import BaseModel, Field


class Event(BaseModel):
    """
    Fields:
        name        → required string
        created_at  → automatically set current UTC time

    Notes:
        - Uses default_factory to generate a value
        - Timestamp is created when the model instance is created
        - User can still provide a custom datetime if needed
    """
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Example
event = Event(name="FastAPI Workshop")

print(event)
# Output:
# name='FastAPI Workshop'
# created_at=datetime(...)


print(event.model_dump())
# Output:
# {
#     'name': 'FastAPI Workshop',
#     'created_at': datetime(...)
# }


# Professional Note:
# - datetime fields are commonly used for:
#     • created_at
#     • updated_at
#     • login_time
#     • event timestamps
# - Pydantic automatically converts valid ISO datetime strings
#   into Python datetime objects.
# - default_factory is preferred when generating dynamic values
#   such as timestamps.


#-------------------------


#033 How do you use model inheritance in Pydantic?

# Pydantic models support inheritance just like normal Python classes.
# Child models automatically inherit fields from parent models.

from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    Shared fields used by multiple models.
    """
    name: str
    price: float


class ItemCreate(ItemBase):
    """
    Used when creating a new item.

    Notes:
        - Inherits all fields from ItemBase
        - No additional fields required
    """
    pass


class ItemOut(ItemBase):
    """
    Used for API responses.

    Notes:
        - Inherits fields from ItemBase
        - Adds database-generated id
    """
    id: int


# Example
item_create = ItemCreate(
    name="Laptop",
    price=1200.0
)

item_response = ItemOut(
    id=1,
    name="Laptop",
    price=1200.0
)

print(item_create)
# Output:
# name='Laptop' price=1200.0

print(item_response)
# Output:
# id=1 name='Laptop' price=1200.0


# Professional Note:
# - Inheritance avoids repeating common fields.
# - Very common in FastAPI projects:
#
#     Base Model      → shared fields
#     Create Model    → request body (POST)
#     Update Model    → request body (PUT/PATCH)
#     Response Model  → API output
#
# - Improves maintainability and reduces duplicate code.
# - Changes made in the base model automatically apply
#   to all child models.


#-------------------------