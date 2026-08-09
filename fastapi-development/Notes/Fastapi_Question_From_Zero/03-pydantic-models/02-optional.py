#004 How do you make a field optional in a Pydantic model?

# You can use Optional from typing and assign a default value (usually None)

from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    """
    description:
        - Optional field
        - Can be omitted in request

    Behavior:
        - If not provided → defaults to None
        - If provided → must match type (str)
    """
    name: str
    description: Optional[str] = None


#-------------------------


#005 How do you add field validation using Field() in Pydantic?

# Field() allows adding constraints and metadata to model fields

from pydantic import Field


class Product(BaseModel):
    """
    name:
        - Required
        - Length must be between 1 and 100

    price:
        - Required
        - Must be greater than 0

    quantity:
        - Default = 0
        - Must be ≥ 0
    """
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)


#-------------------------


#006 How do you add an example to a Pydantic model for the docs?

# You can use model_config to add example data for Swagger UI

class ExampleItem(BaseModel):
    """
    Adds example in API docs (Swagger UI)

    Useful for:
        ✔ Better API documentation
        ✔ Helping frontend developers understand request format
    """
    name: str
    price: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Widget",
                "price": 9.99
            }
        }
    }