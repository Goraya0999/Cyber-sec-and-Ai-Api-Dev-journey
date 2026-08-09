#039 How do you add a custom middleware to FastAPI?

You can add custom middleware in FastAPI by creating a class using `BaseHTTPMiddleware`.  
Middleware runs before and after each request, allowing you to modify requests or responses.  
It is useful for logging, authentication, and performance monitoring.  
Add it to the app using `app.add_middleware()`.

**Example:**
```python
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        return response

app.add_middleware(LogMiddleware)

#040 What does 'operation ID' mean in OpenAPI/FastAPI?

`operationId` is a unique identifier assigned to each API endpoint in the OpenAPI schema.  
FastAPI automatically generates it using the function name, path, and HTTP method.  
It is used by tools like Swagger UI and client generators to reference endpoints.  
You can override it manually to make it more meaningful or consistent.

**Example:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items", operation_id="getAllItems")
def read_items():
    return ["item1", "item2"]