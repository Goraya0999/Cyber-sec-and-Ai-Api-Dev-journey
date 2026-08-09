#001 What is a Pydantic model and how do you define one?

# A Pydantic model is used for data validation and serialization.
# You define it by inheriting from BaseModel and using type annotations.

from pydantic import BaseModel


class Item(BaseModel):
    """
    Fields:
        name      → required string
        price     → required float
        in_stock  → optional boolean (default = True)

    Notes:
        - Automatically validates input data
        - Converts types if possible (e.g., "10" → 10)
        - Raises validation error if data is invalid
    """
    name: str
    price: float
    in_stock: bool = True


#-------------------------


#002 How do you use a Pydantic model as a request body in FastAPI?

# When you use a Pydantic model as a function parameter,
# FastAPI automatically treats it as a request body.

from fastapi import FastAPI

app = FastAPI()


@app.post("/items")
def create_item(item: Item):
    """
    Behavior:
        - Expects JSON body matching Item model
        - Automatically validates incoming data

    Example Request:
        POST /items
        {
            "name": "Laptop",
            "price": 1200.5,
            "in_stock": true
        }

    Response:
        Returns the same validated data
    """
    return item


#-------------------------


#003 How does FastAPI know a parameter is a request body vs a query parameter?

# FastAPI determines parameter type based on its annotation

@app.get("/example")
def example(name: str, item: Item):
    """
    Rules:
        - Simple types (str, int, bool) → Query or Path parameters
        - Pydantic models (BaseModel) → Request Body

    Example Request:
        GET /example?name=Ali
        Body:
        {
            "name": "Phone",
            "price": 500
        }

    Notes:
        - FastAPI uses type hints to decide automatically
        - No need to explicitly specify body/query in most cases
    """
    return {"query_name": name, "body_item": item}