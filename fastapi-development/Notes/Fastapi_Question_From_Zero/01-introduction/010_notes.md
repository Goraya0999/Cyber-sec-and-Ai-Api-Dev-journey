# FastAPI Notes (#021 - #023)

## Q1. Can a FastAPI app have multiple route handlers for the same path but different HTTP methods?

Yes, FastAPI allows multiple route handlers for the same path as long as they use different HTTP methods. Each HTTP method (GET, POST, PUT, DELETE, etc.) represents a different type of operation. This means you can define separate functions for the same URL but handle different actions. FastAPI uses decorators like `@app.get()` and `@app.post()` to distinguish between them. This approach follows REST API design principles. It helps keep your code organized and clear. Each function processes requests based on the HTTP method used.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"message": "Get items"}

@app.post("/items")
def create_item():
    return {"message": "Item created"}
```

---

## Q2. What happens when you return None from a route handler?

When you return `None` in a FastAPI route handler, FastAPI converts it into a JSON response with a value of `null`. By default, the HTTP status code will still be `200 OK`. This means the request is considered successful even though no actual data is returned. However, in some cases, you may want to return an empty response with no body. For that, you should explicitly use a `204 No Content` status code. This makes your API behavior more accurate and aligned with HTTP standards.

**Example:**

```python
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/empty")
def empty_response():
    return None

@app.get("/no-content")
def no_content():
    return Response(status_code=204)
```

---

## Q3. What is the difference between synchronous and asynchronous route handlers in FastAPI?

FastAPI supports both synchronous (`def`) and asynchronous (`async def`) route handlers. Synchronous functions run in a thread pool, which prevents blocking the main event loop. Asynchronous functions run directly on the event loop and can use `await` for non-blocking operations. Async handlers are more efficient when dealing with I/O tasks like database queries or API calls. Sync handlers are easier to write and suitable for CPU-bound tasks. Choosing between them depends on your use case. Using async properly can significantly improve performance in high-load applications.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/sync")
def sync_handler():
    return {"message": "This is sync"}

@app.get("/async")
async def async_handler():
    return {"message": "This is async"}
```
