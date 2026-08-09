# 🔹 #043 — Difference Between `add_middleware` and `@app.middleware`

---

## 📖 Overview

In **FastAPI**, middleware is used to **intercept every request and response**.

> 📌 Middleware works like a pipeline layer where you can:
> - Log requests
> - Modify responses
> - Handle authentication
> - Measure performance

There are **two main ways** to implement middleware:

1. ⚡ **Decorator-based (`@app.middleware`)**
2. 🚀 **Class-based (`add_middleware`)**

---

## ⚡ 1. `@app.middleware("http")` (Function / Decorator Style)

This is the **simplest way** to create middleware in FastAPI.

---

### 🔧 Example

```python
@app.middleware("http")
async def simple_middleware(request, call_next):
    print("Before request")

    response = await call_next(request)

    print("After request")
    return response

## 🚀 2. `app.add_middleware()` (Class-Based Middleware)

This approach is **more structured, powerful, and production-ready**. It allows you to build **reusable and configurable middleware components**.

---

### 🔧 Example

```python
from starlette.middleware.base import BaseHTTPMiddleware

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print("Before request")

        response = await call_next(request)

        print("After request")
        return response

app.add_middleware(CustomMiddleware)