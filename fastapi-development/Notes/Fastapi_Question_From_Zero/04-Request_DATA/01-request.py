#001 How do you read a JSON request body in FastAPI?

# FastAPI automatically reads and parses JSON body
# when you use a Pydantic model in function parameters

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    """
    Represents incoming JSON structure

    FastAPI will:
        ✔ Parse JSON body
        ✔ Validate data types
        ✔ Convert into Python object
    """
    name: str
    price: float


@app.post("/items")
def create(item: Item):
    """
    'item' is automatically:
        - Parsed from request JSON
        - Validated using Pydantic
        - Converted to Python object

    No need to manually use:
        json.loads()
        request.body()
    """
    return item


# Example Request:
"""
POST /items
Content-Type: application/json

{
  "name": "Laptop",
  "price": 1200.0
}
"""


# Professional Insight:
# ✔ Cleaner and safer than manual parsing
# ✔ Built-in validation prevents invalid data
# ✔ Automatically returns 422 error on invalid input
#------------------------------------------------
#002 How do you read form data in FastAPI?

# Use Form() to receive data from HTML forms (application/x-www-form-urlencoded)

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    """
    FastAPI will:
        ✔ Read form data instead of JSON
        ✔ Validate required fields
        ✔ Inject values into parameters

    Form(...) means:
        - Required field
    """
    return {"username": username}


# Example Request (Form Data):
"""
POST /login
Content-Type: application/x-www-form-urlencoded

username=admin&password=1234
"""


#-------------------------


#003 What package is required to use Form() in FastAPI?

# FastAPI depends on python-multipart to parse form data

# Install it using:
# pip install python-multipart


# Professional Note:
# ✔ Required for handling:
#     - Form data
#     - File uploads (UploadFile, File)
# ✔ Without it → FastAPI will raise runtime error