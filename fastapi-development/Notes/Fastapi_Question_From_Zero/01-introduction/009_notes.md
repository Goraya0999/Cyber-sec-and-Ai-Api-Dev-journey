## Q1. How do you return a list from a FastAPI route?

In FastAPI, returning a list is very simple because it automatically converts Python data into JSON format. When you return a list of dictionaries, FastAPI sends it as a JSON array in the response. This is commonly used when you want to return multiple items such as users, products, or records from a database. You don’t need to manually convert the data into JSON. FastAPI internally uses serialization tools to handle this efficiently. You can also combine lists with response models for better validation and structure. This makes API development faster and cleaner.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return [{"id": 1}, {"id": 2}]
```

---

## Q2. How do you access the auto-generated docs in a browser?

FastAPI automatically generates interactive API documentation for your application. These docs are based on the OpenAPI schema and require no additional setup. You can access them through your browser once the server is running. The Swagger UI is available at `/docs`, where you can test endpoints interactively. Another interface, ReDoc, is available at `/redoc` and provides a cleaner, more structured view. These tools help developers understand API endpoints, parameters, and responses easily. It is one of the most powerful beginner-friendly features of FastAPI.

**Example:**
Open your browser and visit:

* [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
* [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)
