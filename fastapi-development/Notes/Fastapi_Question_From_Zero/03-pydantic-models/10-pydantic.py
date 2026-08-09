#028 How do you define a Union field in a Pydantic model?

# Union allows a field to accept multiple possible types

from pydantic import BaseModel
from typing import Union


class Result(BaseModel):
    """
    value:
        - Can be either int OR str
        - Pydantic will validate against allowed types
    """
    value: Union[int, str]


# Example:
res1 = Result(value=10)       # ✅ int
res2 = Result(value="ten")    # ✅ str
# res3 = Result(value=10.5)   # ❌ Validation error (not int/str)


# Professional Note:
# Use Union when:
# ✔ API accepts flexible input types
# ✔ Backward compatibility is needed


#-------------------------


#029 How do you validate model data after creation with @model_validator?

# @model_validator is used for cross-field validation (whole model)

from pydantic import model_validator


class Range(BaseModel):
    """
    Ensures:
        min < max
    """
    min: int
    max: int

    @model_validator(mode="after")
    def check_range(self):
        """
        Runs AFTER all fields are validated

        Useful for:
            ✔ Comparing multiple fields
            ✔ Complex business rules
        """
        if self.min >= self.max:
            raise ValueError("min must be less than max")
        return self


# Example:
valid_range = Range(min=1, max=10)   # ✅ Valid
# invalid_range = Range(min=10, max=5)  # ❌ Raises validation error


#-------------------------


#030 What is the purpose of the alias parameter in Field()?

# alias allows different external (JSON) name and internal (Python) name

from pydantic import Field, ConfigDict


class Item(BaseModel):
    """
    item_name:
        - Internal Python attribute
        - Accepts 'itemName' from JSON input
    """
    model_config = ConfigDict(populate_by_name=True)

    item_name: str = Field(..., alias="itemName")


# Example inputs:
item1 = Item(itemName="Laptop")   # ✅ Using alias
item2 = Item(item_name="Phone")   # ✅ Using Python name


# Output:
print(item1.item_name)  # Laptop


# Professional Insight:
# ✔ Useful for frontend-backend naming differences (camelCase vs snake_case)
# ✔ Keeps Python code clean while supporting external API formats