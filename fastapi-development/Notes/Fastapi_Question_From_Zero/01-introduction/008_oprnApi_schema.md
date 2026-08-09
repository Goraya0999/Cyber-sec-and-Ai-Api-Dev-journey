# FastAPI Beginner Notes (Q&A)

## Q1. What is the OpenAPI schema and where does FastAPI expose it?

OpenAPI schema is a standardized way to describe REST APIs in a machine-readable format (usually JSON). It defines endpoints, request/response models, parameters, authentication, and more. FastAPI automatically generates this schema based on your code, including type hints and route definitions. This makes API documentation accurate and always up to date. Developers can use this schema to test APIs or integrate them with other services. FastAPI exposes the OpenAPI schema at the `/openapi.json` endpoint by default. It also provides interactive documentation using Swagger UI and ReDoc. This automation saves time and reduces human errors in documentation.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

Now visit: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## Q2. What library does FastAPI use for data validation by default?

FastAPI uses Pydantic as its default library for data validation and parsing. Pydantic allows you to define data models using Python classes and type annotations. It ensures that incoming request data matches the expected format and types. If invalid data is sent, FastAPI automatically returns a clear error response. Pydantic also handles data serialization, converting Python objects into JSON. It improves code readability and reduces manual validation logic. Additionally, it supports advanced features like default values, optional fields, and nested models. This makes FastAPI robust and developer-friendly.

**Example:**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {"name": user.name, "age": user.age}
```

If you send invalid data (e.g., age as string), FastAPI will return a validation error automatically.

---

## Q3. What does 'path operation' mean in FastAPI terminology?

In FastAPI, a **path operation** refers to the combination of a specific URL path and an HTTP method (like GET, POST, PUT, DELETE). It defines what action should be performed when a client sends a request to a particular endpoint. Each path operation is linked to a Python function (called a path operation function) that handles the request and returns a response. FastAPI uses decorators such as `@app.get()` or `@app.post()` to declare these operations. Path operations also include metadata like parameters, request bodies, and response models. They are automatically documented in the OpenAPI schema and interactive docs. This structure makes APIs clean, readable, and easy to maintain.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items")
def create_item(item: dict):
    return {"message": "Item created", "item": item}
```

Here, `POST /items` is a path operation that creates a new item.
