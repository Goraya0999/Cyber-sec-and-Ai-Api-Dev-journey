# FastAPI Notes (#030)

## Q1. What is the lifespan parameter in newer versions of FastAPI?

In newer versions of FastAPI, the `lifespan` parameter is used as a modern alternative to the older `@app.on_event("startup")` and `@app.on_event("shutdown")` decorators. It allows you to manage both startup and shutdown logic in a single place using an asynchronous context manager. This approach is cleaner and more structured, especially for complex applications. The code before the `yield` runs at startup, while the code after the `yield` runs during shutdown. It is useful for tasks like opening and closing database connections, initializing resources, or cleaning up. Using lifespan improves readability and follows modern async patterns in Python.

**Example:**

```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print("App starting")
    yield
    # shutdown
    print("App stopping")

app = FastAPI(lifespan=lifespan)
```
