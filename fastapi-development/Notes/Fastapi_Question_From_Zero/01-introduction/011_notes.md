# FastAPI Notes (#024 - #026)

## Q1. How do you add metadata like summary and description to a single route?

In FastAPI, you can add metadata such as `summary` and `description` directly inside the route decorator. This metadata is used in the auto-generated documentation (Swagger UI and ReDoc). The summary provides a short title for the endpoint, while the description gives detailed information about what the route does. This helps developers understand the API better. It also improves readability and professionalism of your API docs. Adding metadata is simple and does not affect the functionality of the route.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items", summary="List items", description="Returns all items in the database")
def get_items():
    return []
```

---

## Q2. What is the purpose of the tags parameter in route decorators?

The `tags` parameter in FastAPI is used to group related routes together in the API documentation. This is especially useful when working with large APIs that have many endpoints. Tags make it easier to organize and navigate routes in Swagger UI. Each tag represents a category or feature of your API. You can assign one or multiple tags to a route. This improves the structure and usability of your API documentation.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items", tags=["items"])
def get_items():
    return []
```

---

## Q3. How do you deprecate a route in FastAPI?

FastAPI allows you to mark a route as deprecated using the `deprecated=True` parameter in the route decorator. This indicates that the route should no longer be used and may be removed in the future. Deprecated routes still work but are flagged in the documentation. This helps developers transition to newer endpoints. It is a good practice when updating APIs without breaking existing clients. The deprecated status appears clearly in Swagger UI.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/old-route", deprecated=True)
def old_route():
    return {}
```
