#037 How do you define a route that only accepts specific string values?

# You can restrict allowed values using Enum (string-based).
# FastAPI will automatically validate input against these values.

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Status(str, Enum):
    pending = "pending"
    success = "success"
    failed = "failed"


@app.get("/orders/{status}")
def get_orders(status: Status):
    """
    Only allowed values:
        - pending
        - success
        - failed

    Behavior:
        - If user sends any other value → FastAPI returns 422 error
        - Validation is automatic

    Example:
        /orders/pending   ✔
        /orders/invalid   ❌ (422 error)
    """

    return {"status": status}


#-------------------------


#038 How do you access raw query string parameters?

# FastAPI provides Request object to access raw query params

from fastapi import Request


@app.get("/raw")
def raw(request: Request):
    """
    request.query_params:
        - gives all query parameters
        - works like a dictionary-like object

    dict(request.query_params):
        - converts it into a standard dictionary

    Example:
        /raw?name=ali&age=20

    Output:
        {
            "name": "ali",
            "age": "20"
        }
    """

    return dict(request.query_params)
#------------------------------------------
#039 What is the difference between response_class and response_model?

# response_model:
#   - Used for data validation, serialization, and filtering
#   - Based on Pydantic models
#   - Controls what data is returned to the client

# response_class:
#   - Controls HOW the response is returned (format/type)
#   - Example: JSONResponse, HTMLResponse, PlainTextResponse

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.get("/user", response_model=User)
def get_user():
    """
    response_model:
        - Ensures response follows User schema
        - Extra fields will be removed automatically
        - Missing fields will raise validation error

    Example Output:
        {
            "name": "Ali",
            "age": 25
        }
    """
    return {"name": "Ali", "age": 25, "password": "hidden"}  # password will be filtered out


@app.get("/html", response_class=HTMLResponse)
def get_html():
    """
    response_class:
        - Changes response type (here → HTML instead of JSON)

    Example:
        Returns raw HTML instead of JSON
    """
    return "<h1>Hello World</h1>"


#-------------------------


#040 How do you use regex validation on a query parameter?

# FastAPI allows regex (pattern) validation using Query()

from fastapi import Query


@app.get("/items")
def get_items(code: str = Query(pattern=r'^[A-Z]{3}$')):
    """
    pattern explanation:
        ^        → start of string
        [A-Z]{3} → exactly 3 uppercase letters
        $        → end of string

    Valid Examples:
        /items?code=ABC   ✔
        /items?code=XYZ   ✔

    Invalid Examples:
        /items?code=abC   ❌
        /items?code=ABCD  ❌
        /items?code=12A   ❌

    Behavior:
        - Invalid input → FastAPI returns 422 validation error automatically
    """
    return {"code": code}