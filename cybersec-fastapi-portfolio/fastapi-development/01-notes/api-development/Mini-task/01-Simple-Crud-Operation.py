from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference


# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title="Simple CRUD API",
    description="An API for performing basic CRUD operations on items.",
    version="1.0.0",
)


# ==========================================================
# In-Memory Data
# ==========================================================

items = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Smartphone", "price": 499.99},
    3: {"name": "Headphones", "price": 199.99},
    4: {"name": "Smartwatch", "price": 299.99},
    5: {"name": "Tablet", "price": 399.99},
}


# ==========================================================
# READ Operations
# ==========================================================

# Retrieve all items
@app.get("/shipments")
def get_all_item() -> dict[str | int, Any]:
    return items


# Retrieve an item by ID
@app.get("/shipment/{id}")
def get_item_by_id(id: int) -> dict[str, Any]:
    if id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not Found",
        )

    return items[id]


# ==========================================================
# CREATE Operation
# ==========================================================

# Create a new item
@app.post("/shipment")
def create_item(name: str, price: float) -> dict[str, Any]:
    new_id = max(items.keys()) + 1

    items[new_id] = {
        "name": name,
        "price": price,
    }

    print(f"new id is {new_id}")

    return items[new_id]


# ==========================================================
# UPDATE Operation (Complete)
# ==========================================================

# Replace an existing item
@app.put("/shipment")
def update_item(id: int, name: str, price: float) -> dict[str, Any]:
    if id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not Found",
        )

    items[id] = {
        "name": name,
        "price": price,
    }

    return items[id]


# ==========================================================
# PARTIAL UPDATE Operation
# ==========================================================

# Update selected fields of an item
@app.patch("/shipment")
def partially_updated(id: int, body: dict[str, Any]) -> dict[str, Any]:
    if id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not Found",
        )

    items[id].update(body)

    return items[id]


# ==========================================================
# DELETE Operation
# ==========================================================

# Delete an item by ID
@app.delete("/shipment")
def delete_by_id(id: int):
    if id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not Found",
        )

    items.pop(id)

    return {
        "Detail": f"item with id #{id} is successfully deleted"
    }


# ==========================================================
# Scalar API Documentation
# ==========================================================

@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Doc",
    )