#019 How do you add the same route for multiple HTTP methods?

# FastAPI provides `@app.api_route()` to handle multiple HTTP methods 
# for a single path.

from fastapi import FastAPI

app = FastAPI()

@app.api_route("/items", methods=["GET", "HEAD"])
def get_items():
    """
    This route will respond to:
        - GET  /items
        - HEAD /items

    Notes:
        - Useful when multiple methods share the same logic
        - HEAD usually returns headers only (no body), but FastAPI handles it automatically
    """
    return []


#020 What is the include_in_schema parameter?

# `include_in_schema=False` hides the endpoint from the auto-generated
# API documentation (Swagger UI / OpenAPI), but the route still works.

@app.get("/health", include_in_schema=False)
def health():
    """
    Example:
        /health → {"status": "ok"}

    Notes:
        - Endpoint is accessible but NOT visible in docs
        - Useful for:
            ✔ internal APIs
            ✔ health checks
            ✔ admin/debug routes
    """
    return {"status": "ok"}
#---------------------------------------------
#021 How do you use APIRouter to organize routes into separate files?

# APIRouter helps you split your FastAPI app into multiple files/modules
# for better structure and scalability.

# 📁 Project Structure Example:
# ├── main.py
# └── items.py


# ---------------------------
# items.py (separate module)
# ---------------------------
from fastapi import APIRouter

router = APIRouter()

@router.get("/{item_id}")
def get_item(item_id: int):
    """
    Handles:
        GET /items/{item_id}
    """
    return {"id": item_id}


# ---------------------------
# main.py (entry point)
# ---------------------------
from fastapi import FastAPI
from items import router as items_router

app = FastAPI()

# Include router with prefix and tags
app.include_router(
    items_router,
    prefix="/items",   # all routes will start with /items
    tags=["items"]     # group name in Swagger UI
)

"""
Result:
    GET /items/10 → handled by items.py

Benefits:
    ✔ Clean code organization
    ✔ Easy to scale large projects
    ✔ Reusable route modules
"""