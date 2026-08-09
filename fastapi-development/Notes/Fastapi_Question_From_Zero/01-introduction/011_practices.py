# Import FastAPI library
from fastapi import FastAPI


# Create FastAPI application instance
# Metadata such as title, description, and version
# is automatically displayed in Swagger UI documentation.
app = FastAPI(
    title="My API",
    description="API for testing FastAPI route tags and documentation",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message":"testing is on"
    }
# -------------------- Route Tags Example -------------------- #
# The 'tags' parameter is used to group related endpoints
# inside the automatically generated Swagger documentation.


# GET endpoint to retrieve item information
@app.get("/item", tags=["Item"])
def get_item():
    return {
        "message": "Item information retrieved successfully"
    }


# POST endpoint to create a new item
@app.post("/item", tags=["Item"])
def create_item():
    return {
        "message": "Item created successfully"
    }


# GET endpoint to retrieve item price information
@app.get("/item/price", tags=["Item"])
def get_item_price():
    return {
        "item": "price"
    }


# Run the application using:
# uvicorn 011_practice:app --reload

# Open Swagger UI documentation in browser:
# http://127.0.0.1:8000/docs

