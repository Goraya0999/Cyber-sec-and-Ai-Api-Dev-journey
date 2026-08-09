#010 How do you add extra body parameters using Body()?

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create(
    item: Item,                                  # main request body (Pydantic model)
    importance: int = Body(..., ge=1, le=5)       # extra body parameter with validation
):
    """
    Body() is used to:
        ✔ Add additional fields to request body
        ✔ Apply validation (range, default, metadata)
        ✔ Control how FastAPI reads the data
    """

    return {
        "item": item,
        "importance": importance
    }


# Example Request JSON:
"""
{
    "item": {
        "name": "Laptop",
        "price": 1200
    },
    "importance": 3
}
"""


# Professional Comment:
# ✔ Body() is powerful for validation without creating separate models
# ✔ Use it for small extra fields (flags, priority, metadata)
# ✔ For complex structures, prefer separate Pydantic models for clarity
# ✔ Always validate ranges (ge, le) to prevent invalid data in production

#---------------------
#011 How do you embed a single body parameter?

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create(item: Item = Body(embed=True)):
    """
    By default:
        FastAPI expects raw JSON like:
            { "name": "Laptop", "price": 1200 }

    With embed=True:
        FastAPI expects:
            { "item": { "name": "Laptop", "price": 1200 } }
    """

    return item


# Example Request (with embed=True):
"""
{
    "item": {
        "name": "Laptop",
        "price": 1200
    }
}
"""


# Professional Comment:
# ✔ Use embed=True when:
#     - You want consistent request structure
#     - You plan to add more body fields later
# ✔ Common in enterprise APIs for better scalability & versioning
# ✔ Avoid if unnecessary — adds extra nesting for clients



#012 How do you read cookies from a request?

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/me")
def me(session_id: str = Cookie(None)):
    """
    Reads cookie value sent by client.

    If cookie does not exist:
        session_id will be None
    """

    return {
        "session_id": session_id
    }


# Example Request Headers:
"""
Cookie: session_id=abc123xyz
"""


# Professional Comment:
# ✔ Cookies are commonly used for session management
# ✔ Always secure cookies in production:
#     - HttpOnly (prevent JS access)
#     - Secure (HTTPS only)
#     - SameSite (CSRF protection)
# ✔ Never store sensitive data directly in cookies (use tokens instead)