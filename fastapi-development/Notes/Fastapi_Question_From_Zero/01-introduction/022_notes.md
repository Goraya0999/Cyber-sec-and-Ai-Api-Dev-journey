# 🔹 #048 — What is the Purpose of the `openapi_url` Parameter?

---

## 📖 Overview

In **FastAPI**, the `openapi_url` parameter is used to **customize or disable the OpenAPI schema endpoint**.

> 📌 The OpenAPI schema is what powers:
> - Swagger UI (`/docs`) 📄  
> - ReDoc (`/redoc`) 📘  

---

## 🧠 What is OpenAPI?

**OpenAPI** is a standard format that describes your API structure:
- Endpoints
- Request/Response formats
- Authentication methods

FastAPI automatically generates this schema for you.

---

## 🚀 Default Behavior

By default, FastAPI exposes the OpenAPI schema at:


---

# 🔹 #049 — How to Add Contact or License to OpenAPI Metadata?

---

## 📖 Overview

FastAPI allows you to **customize your OpenAPI documentation metadata**, including:

- 📞 Contact information  
- 📄 License details  

> 📌 This information appears in:
> - Swagger UI (`/docs`)  
> - ReDoc (`/redoc`)  

---

## 🚀 Basic Implementation

You can pass `contact` and `license_info` directly when creating the FastAPI app.

### 🔧 Example

```python
from fastapi import FastAPI

app = FastAPI(
    contact={
        "name": "Dev Team",
        "email": "dev@example.com"
    },
    license_info={
        "name": "MIT"
    }
)