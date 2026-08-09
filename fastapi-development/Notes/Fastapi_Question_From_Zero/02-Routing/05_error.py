#016 What happens if you access /items/foo when the item_id is typed as int?

# FastAPI performs automatic type validation.
# If a value cannot be converted to the declared type, it raises a validation error.

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Example:
        /items/10  → valid (item_id = 10)
        /items/foo → ❌ invalid (cannot convert "foo" to int)

    Result:
        FastAPI returns:
        - Status Code: 422 Unprocessable Entity
        - Detailed error message explaining the type mismatch
    """
    return {"item_id": item_id}


#017 How do you define a UUID path parameter?

# FastAPI supports UUID type for path parameters.
# It automatically validates and converts the string into a UUID object.

from uuid import UUID

@app.get("/items/{item_id}")
def get_item(item_id: UUID):
    """
    Example:
        /items/550e8400-e29b-41d4-a716-446655440000 → valid UUID
        /items/12345 → ❌ invalid UUID → 422 error

    Notes:
        - Ensures only valid UUID format is accepted
        - Useful for secure and unique identifiers

    Returns:
        dict: UUID value
    """
    return {"id": item_id}

#--------------------------------------------------------------
#018 What is the difference between @app.put and @app.patch?

# Both PUT and PATCH are HTTP methods used for updating resources,
# but they differ in *how* the update is intended to be performed.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


# 🔵 PUT → Full Update (Replace entire resource)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    PUT expects the FULL resource.
    Missing fields may overwrite existing data.

    Example:
        If original = {name: "A", price: 10, description: "old"}

        PUT with:
        {name: "B", price: 20}

        Result:
        description → LOST (replaced)
    """
    return {"item_id": item_id, "item": item}


# 🟡 PATCH → Partial Update (Modify only provided fields)
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

@app.patch("/items/{item_id}")
def partial_update_item(item_id: int, item: ItemUpdate):
    """
    PATCH updates ONLY provided fields.

    Example:
        Original = {name: "A", price: 10, description: "old"}

        PATCH with:
        {price: 20}

        Result:
        {name: "A", price: 20, description: "old"}
    """
    return {"item_id": item_id, "updated_fields": item}


# Key Difference:
# ✔ PUT   → Replace entire resource (send full data)
# ✔ PATCH → Update partial fields (send only what changes)