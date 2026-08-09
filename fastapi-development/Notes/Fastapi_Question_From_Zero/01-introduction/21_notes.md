# 🔹 #046 — How to Log Request Processing Time Using Middleware

---

## 📖 Overview

You can use **middleware in FastAPI** to measure how long each request takes to process.

> 📌 This is useful for:
> - Performance monitoring ⚡  
> - Debugging slow APIs 🐢  
> - Adding custom metrics 📊  

---

## 🚀 Implementation (Class-Based Middleware)

### 🔧 Example

```python
import time
from starlette.middleware.base import BaseHTTPMiddleware

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()

        response = await call_next(request)

        duration = time.time() - start
        response.headers["X-Process-Time"] = str(duration)

        return response
----

```
# 🔹 #047 — Can You Use Regular (Non-Async) Functions in FastAPI?

---

## 📖 Answer

✅ **Yes, you can use regular (`def`) functions as route handlers in FastAPI.**

---

## 🧠 How It Works

FastAPI automatically handles **synchronous (non-async) functions** by:

- 🧵 Running them in a **thread pool**
- ⚡ Preventing them from blocking the **async event loop**

> 📌 This means your app remains performant even if you use normal functions.

---

## 🔧 Example (Sync Route)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sync_route():
    return {"message": "This is a sync route"}