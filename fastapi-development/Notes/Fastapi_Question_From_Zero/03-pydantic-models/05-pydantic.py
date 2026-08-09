#013 How do you use Pydantic's @field_validator decorator?

# @field_validator is used to add custom validation logic to specific fields

from pydantic import BaseModel, field_validator


class User(BaseModel):
    """
    username:
        - Must not contain spaces
        - Custom validation enforced using @field_validator
    """
    username: str

    @field_validator("username")
    @classmethod
    def no_spaces(cls, value: str) -> str:
        """
        Custom validation logic:
            - Reject usernames with spaces
        """
        if " " in value:
            raise ValueError("No spaces allowed in username")
        return value


# Example:
user = User(username="admin")       # ✅ Valid
# user = User(username="admin user")  # ❌ Raises validation error


#-------------------------


#014 How do you exclude fields from the response using response_model?

# response_model_exclude allows hiding specific fields from API response

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    internal_id: int


@app.get("/items", response_model=Item, response_model_exclude={"internal_id"})
def get_item():
    """
    Even though internal_id exists in returned data,
    it will NOT be included in the API response.
    """
    return {
        "name": "Laptop",
        "price": 1200.0,
        "internal_id": 999   # ❌ Hidden in response
    }


#-------------------------


#015 How do you include only specific fields in the response?

# response_model_include ensures only selected fields are returned

@app.get("/filtered-items", response_model=Item, response_model_include={"name", "price"})
def get_filtered_item():
    """
    Only 'name' and 'price' will be returned.
    All other fields will be excluded automatically.
    """
    return {
        "name": "Phone",
        "price": 800.0,
        "internal_id": 123   # ❌ Excluded from response
    }