#034 How do you define a response model for a list of objects?

# Use response_model=List[ModelName]
# to tell FastAPI that the endpoint returns
# a list of objects matching the specified model.

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """
    Fields:
        id     → item identifier
        name   → item name
        price  → item price
    """
    id: int
    name: str
    price: float


@app.get("/items", response_model=List[Item])
def get_items():
    """
    Behavior:
        - Returns a list of Item objects
        - FastAPI validates each object
        - OpenAPI documentation shows an array of Items

    Example Response:
    [
        {
            "id": 1,
            "name": "Laptop",
            "price": 1200.0
        },
        {
            "id": 2,
            "name": "Mouse",
            "price": 25.0
        }
    ]
    """
    return [
        {"id": 1, "name": "Laptop", "price": 1200.0},
        {"id": 2, "name": "Mouse", "price": 25.0}
    ]


# Professional Note:
# - List[Item] means "a list containing Item objects".
# - FastAPI validates every object in the returned list.
# - Automatically generates correct Swagger/OpenAPI docs.
# - Commonly used for GET endpoints that return multiple records.
# - If returned data doesn't match Item structure,
#   FastAPI raises a response validation error.


#-------------------------


#035 What is the difference between model_dump()
# and model_dump(exclude_none=True)?

# model_dump() returns all fields.
# model_dump(exclude_none=True) removes fields
# whose value is None.

from pydantic import BaseModel


class User(BaseModel):
    """
    Fields:
        name   → required string
        email  → optional string
        phone  → optional string
    """
    name: str
    email: str | None = None
    phone: str | None = None


user = User(
    name="Ali",
    email="ali@example.com",
    phone=None
)

# Include all fields
print(user.model_dump())

# Output:
# {
#     'name': 'Ali',
#     'email': 'ali@example.com',
#     'phone': None
# }


# Exclude fields whose value is None
print(user.model_dump(exclude_none=True))

# Output:
# {
#     'name': 'Ali',
#     'email': 'ali@example.com'
# }


# Professional Note:
# - model_dump() includes every field in the model.
# - exclude_none=True removes fields with None values.
# - Useful for:
#     • Partial updates (PATCH requests)
#     • Cleaner API responses
#     • Sending only populated fields
#     • Reducing payload size
# - Frequently used when updating database records
#   so that empty values do not overwrite existing data.


#-------------------------
#036 How do you use Any type in a Pydantic model?

# Use typing.Any when a field can accept
# any valid Python data type.

from typing import Any
from pydantic import BaseModel


class Flexible(BaseModel):
    """
    Fields:
        data → accepts any data type

    Notes:
        - No strict type validation is applied
        - Can store strings, numbers, lists,
          dictionaries, booleans, etc.
    """
    data: Any


# Example 1: String
obj1 = Flexible(data="Hello World")
print(obj1)

# Output:
# data='Hello World'


# Example 2: Integer
obj2 = Flexible(data=100)
print(obj2)

# Output:
# data=100


# Example 3: List
obj3 = Flexible(data=[1, 2, 3])
print(obj3)

# Output:
# data=[1, 2, 3]


# Example 4: Dictionary
obj4 = Flexible(
    data={
        "name": "Ali",
        "age": 22
    }
)
print(obj4)

# Output:
# data={'name': 'Ali', 'age': 22}


# Professional Note:
# - Any disables strict type checking for that field.
# - Useful when:
#     • Accepting dynamic JSON data
#     • Storing metadata
#     • Working with third-party APIs
#     • Handling flexible configurations
# - Use Any carefully because it reduces validation.
# - Prefer specific types (str, int, list, dict, etc.)
#   whenever possible for better data safety and
#   clearer API documentation.


#-------------------------