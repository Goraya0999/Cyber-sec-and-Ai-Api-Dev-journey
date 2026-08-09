# 🚀 FastAPI Master Course & Career Guide
### From Zero to Production — Beginner → Expert

> **Built for:** Job Readiness · Freelancing · Real-World Backend Development · API Security & Performance

---

## 📋 Table of Contents

- [🔰 Level 1 — Beginner](#-level-1--beginner)
- [⚙️ Level 2 — Intermediate](#️-level-2--intermediate)
- [🔥 Level 3 — Advanced](#-level-3--advanced)
- [🏭 Level 4 — Expert / Production](#-level-4--expert--production)
- [🤖 AI Integration with FastAPI](#-ai-integration-with-fastapi)
- [🚀 Portfolio-Ready Projects](#-portfolio-ready-projects)
- [💰 Freelancing Guide](#-freelancing-guide)
- [🧑‍💻 Hiring & Career Tips](#-hiring--career-tips)
- [🛣️ Roadmap: What's Next](#️-roadmap-whats-next)

---

# 🔰 Level 1 — Beginner

---

## 📌 Topic 1: What is FastAPI & Why Use It?

### Simple Explanation

Think of FastAPI like a **super-smart waiter** in a restaurant:
- You (the client) make a request: "I want a pizza."
- The waiter (FastAPI) takes your order, validates it, sends it to the kitchen (your logic/database), and brings back the response — all at lightning speed.

FastAPI is a **modern Python web framework** for building APIs. It was created by **Sebastián Ramírez** and is built on top of:
- **Starlette** — for async web handling
- **Pydantic** — for data validation
- **Python type hints** — for automatic documentation

### Why FastAPI Over Django/Flask?

```
Feature              Flask        Django REST    FastAPI
─────────────────────────────────────────────────────────
Speed (requests/s)   ~5,000       ~3,000         ~60,000+
Auto Docs            ❌           ❌             ✅ (Swagger + ReDoc)
Type Validation      ❌           ❌             ✅ (Pydantic)
Async Support        Partial      Partial        ✅ Native
Learning Curve       Easy         Steep          Easy-Medium
Modern Python        Partial      Partial        ✅ Full
```

### Real-World Use Cases

- REST APIs for mobile/web apps
- Microservices in cloud architectures
- AI/ML model serving (OpenAI wrappers, HuggingFace endpoints)
- Real-time apps with WebSockets
- Internal tools and data pipelines

### 🎯 Interview Questions

> **Q: Why would you choose FastAPI over Flask?**
> A: FastAPI offers automatic data validation via Pydantic, built-in OpenAPI documentation, native async support, and is significantly faster. For modern API development, it reduces boilerplate and catches errors at development time.

> **Q: What is the role of Pydantic in FastAPI?**
> A: Pydantic handles data validation and serialization. When a request arrives, FastAPI uses Pydantic models to validate the incoming data types, constraints, and structure — raising 422 errors automatically if validation fails.

---

## 📌 Topic 2: Installation & Setup

### Prerequisites

```bash
# Check Python version (3.8+ required, 3.11+ recommended)
python --version

# Install FastAPI and Uvicorn (ASGI server)
pip install fastapi uvicorn[standard]

# For development (includes auto-reload)
pip install fastapi[all]
```

### Project Initialization

```bash
# Create a clean project
mkdir my_fastapi_project
cd my_fastapi_project
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn[standard] python-dotenv

# Save dependencies
pip freeze > requirements.txt
```

### Your First FastAPI App

```python
# main.py
from fastapi import FastAPI

app = FastAPI(
    title="My First API",
    description="Learning FastAPI step by step",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI World! 🚀"}
```

### Running the App

```bash
# Development (with auto-reload)
uvicorn main:app --reload

# Production
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Explore the Auto-Generated Docs

Once running, visit:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
- **OpenAPI JSON**: `http://127.0.0.1:8000/openapi.json`

### 💡 Pro Tip
Always use a virtual environment per project. Use `.env` files for secrets — never hardcode credentials. Use `python-dotenv` to load them:

```python
# .env
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=mysupersecret

# config.py
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
```

---

## 📌 Topic 3: Path Operations (GET, POST, PUT, DELETE)

### The HTTP Verbs — An Analogy

Think of HTTP methods like **CRUD operations on a database of contacts**:

```
GET    → Read   → "Show me a contact"
POST   → Create → "Add a new contact"
PUT    → Update → "Replace contact info completely"
PATCH  → Update → "Update only the email"
DELETE → Delete → "Remove the contact"
```

### All HTTP Methods in FastAPI

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory "database" for demo
fake_db: dict[int, dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob",   "email": "bob@example.com"},
}


# ─── GET: Retrieve all items ───────────────────────────────────────────────────
@app.get("/users", tags=["Users"])
def get_all_users():
    """Return all users."""
    return list(fake_db.values())


# ─── GET: Retrieve single item ─────────────────────────────────────────────────
@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int):
    """Return a single user by ID."""
    if user_id not in fake_db:
        return {"error": "User not found"}
    return fake_db[user_id]


# ─── POST: Create new item ─────────────────────────────────────────────────────
class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users", status_code=201, tags=["Users"])
def create_user(user: UserCreate):
    """Create a new user."""
    new_id = max(fake_db.keys(), default=0) + 1
    fake_db[new_id] = {"id": new_id, **user.model_dump()}
    return fake_db[new_id]


# ─── PUT: Full update ──────────────────────────────────────────────────────────
@app.put("/users/{user_id}", tags=["Users"])
def update_user(user_id: int, user: UserCreate):
    """Fully replace a user's data."""
    if user_id not in fake_db:
        return {"error": "User not found"}
    fake_db[user_id] = {"id": user_id, **user.model_dump()}
    return fake_db[user_id]


# ─── PATCH: Partial update ─────────────────────────────────────────────────────
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

@app.patch("/users/{user_id}", tags=["Users"])
def partial_update_user(user_id: int, user: UserUpdate):
    """Partially update a user's data."""
    if user_id not in fake_db:
        return {"error": "User not found"}
    existing = fake_db[user_id]
    update_data = user.model_dump(exclude_unset=True)
    fake_db[user_id] = {**existing, **update_data}
    return fake_db[user_id]


# ─── DELETE: Remove item ───────────────────────────────────────────────────────
@app.delete("/users/{user_id}", status_code=204, tags=["Users"])
def delete_user(user_id: int):
    """Delete a user."""
    if user_id not in fake_db:
        return {"error": "User not found"}
    del fake_db[user_id]
```

### ✅ Best Practices

- Always use correct HTTP status codes (`201` for created, `204` for deleted, `404` for not found)
- Use `tags=["Users"]` to group endpoints in Swagger docs
- Use `exclude_unset=True` in PATCH to update only provided fields
- Add docstrings — they appear in Swagger UI automatically

### ❌ Common Mistakes

```python
# ❌ Wrong: Using POST for fetching data
@app.post("/get-user")  # Confusing and breaks REST conventions

# ✅ Correct: Use GET with path parameter
@app.get("/users/{user_id}")

# ❌ Wrong: Returning raw errors as 200 OK
return {"error": "Not found"}  # Client thinks it's a success!

# ✅ Correct: Use HTTPException
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="User not found")
```

---

## 📌 Topic 4: Request & Response Handling

### Request Body

```python
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Product name")
    price: float = Field(..., gt=0, description="Must be greater than 0")
    description: Optional[str] = Field(None, max_length=500)
    in_stock: bool = True


@app.post("/products", status_code=201)
def create_product(product: Product):
    # product is already validated by Pydantic
    return {
        "message": "Product created",
        "data": product.model_dump()
    }
```

### Response Models — Controlling What You Return

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Input model (what client sends)
class UserCreate(BaseModel):
    name: str
    email: str
    password: str            # ⚠️ Sensitive field


# Output model (what we return) — NEVER expose password!
class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    # Simulate DB save
    saved_user = {
        "id": 42,
        "name": user.name,
        "email": user.email,
        "password": user.password  # In DB, but won't be returned
    }
    return saved_user  # FastAPI filters to UserResponse fields only
```

### Custom Response with Status Codes

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response

app = FastAPI()


@app.get("/custom-response")
def custom_response():
    return JSONResponse(
        status_code=200,
        content={"message": "Custom response with headers"},
        headers={"X-Custom-Header": "my-value"}
    )


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # 204 No Content — don't return a body
    return Response(status_code=204)
```

### 💡 Pro Tips

- Use `response_model` to control serialization and auto-generate API docs
- Use `response_model_exclude_unset=True` to skip null/default fields in response
- Use `JSONResponse` when you need custom headers or non-standard responses
- Pydantic v2: use `.model_dump()` instead of `.dict()` (deprecated)

---

## 📌 Topic 5: Query & Path Parameters

### Path Parameters

```python
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(
        ...,
        title="User ID",
        description="The unique identifier of the user",
        ge=1,          # Greater than or equal to 1
        le=1_000_000   # Less than or equal to 1 million
    )
):
    return {"user_id": user_id}


# Multiple path parameters
@app.get("/departments/{dept_id}/employees/{emp_id}")
def get_employee(dept_id: int, emp_id: int):
    return {"department": dept_id, "employee": emp_id}


# Enum path parameter
from enum import Enum

class Category(str, Enum):
    electronics = "electronics"
    clothing     = "clothing"
    books        = "books"

@app.get("/products/{category}")
def get_products_by_category(category: Category):
    return {"category": category, "products": ["item1", "item2"]}
```

### Query Parameters

```python
from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()


# Basic query params: GET /items?skip=0&limit=10
@app.get("/items")
def list_items(
    skip: int   = Query(0,    ge=0,   description="Number of records to skip"),
    limit: int  = Query(10,   le=100, description="Max records to return"),
    search: Optional[str] = Query(None, min_length=1, description="Search keyword")
):
    return {
        "skip": skip,
        "limit": limit,
        "search": search
    }


# Multi-value query param: GET /filter?tags=python&tags=fastapi
@app.get("/filter")
def filter_by_tags(tags: List[str] = Query(default=[])):
    return {"tags": tags}


# Optional with alias: GET /users?user_name=alice
@app.get("/users")
def get_users_by_name(
    name: Optional[str] = Query(None, alias="user_name")
):
    return {"name": name}
```

### Combined Path + Query + Body

```python
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


class ItemUpdate(BaseModel):
    name: str
    price: float


@app.put("/shops/{shop_id}/items/{item_id}")
def update_shop_item(
    shop_id: int     = Path(..., ge=1),
    item_id: int     = Path(..., ge=1),
    notify: bool     = Query(False, description="Send notification email?"),
    item: ItemUpdate = ...
):
    return {
        "shop_id":   shop_id,
        "item_id":   item_id,
        "notify":    notify,
        "updated_to": item.model_dump()
    }
```

### 💡 Pro Tips

- Path params are **required** — they're part of the URL
- Query params are **optional** by default when given a default value
- Use `alias` when your API contract uses names that aren't valid Python identifiers (e.g. `user-name`)
- Add `description` and `example` to all query params for better documentation

### 🎯 Interview Questions

> **Q: What's the difference between a path parameter and a query parameter?**
> A: Path parameters are embedded in the URL path (`/users/{id}`) and are always required. Query parameters follow a `?` in the URL (`/users?limit=10`) and are typically optional. Path params identify a specific resource; query params filter or modify the response.

> **Q: How does FastAPI handle type validation for request parameters?**
> A: FastAPI leverages Python type hints and Pydantic under the hood. When a request arrives, FastAPI attempts to coerce and validate the parameter. If the value can't be converted (e.g., `"abc"` for an `int` path parameter), it automatically returns a `422 Unprocessable Entity` response with a detailed error.

---

## 📌 Topic 6: Pydantic Models

### Why Pydantic?

Pydantic is like a **strict customs officer** at an airport — it checks every bag (data field) against the rules before letting it through.

```python
from pydantic import (
    BaseModel, Field, EmailStr, field_validator,
    model_validator, computed_field
)
from typing import Optional, List
from datetime import datetime
from enum import Enum


# ─── Enums ────────────────────────────────────────────────────────────────────
class UserRole(str, Enum):
    admin  = "admin"
    editor = "editor"
    viewer = "viewer"


# ─── Nested Models ────────────────────────────────────────────────────────────
class Address(BaseModel):
    street:  str
    city:    str
    country: str = "Pakistan"
    zipcode: Optional[str] = None


# ─── Full User Model ──────────────────────────────────────────────────────────
class UserCreate(BaseModel):
    name:     str     = Field(..., min_length=2, max_length=50, example="Alice Khan")
    email:    EmailStr                              # Validates email format
    age:      int     = Field(..., ge=18, le=120)  # Between 18 and 120
    role:     UserRole = UserRole.viewer
    tags:     List[str] = []
    address:  Optional[Address] = None
    password: str     = Field(..., min_length=8)

    # ─── Field-level validator ─────────────────────────────────────────────
    @field_validator("name")
    @classmethod
    def name_must_be_capitalized(cls, v: str) -> str:
        return v.strip().title()

    # ─── Cross-field validator ─────────────────────────────────────────────
    @model_validator(mode="after")
    def check_admin_has_address(self) -> "UserCreate":
        if self.role == UserRole.admin and self.address is None:
            raise ValueError("Admin users must provide an address.")
        return self

    # ─── Computed field (derived, read-only) ──────────────────────────────
    @computed_field
    @property
    def display_name(self) -> str:
        return f"{self.name} ({self.role.value})"


# ─── Separate Response Model (no password) ────────────────────────────────────
class UserResponse(BaseModel):
    id:           int
    name:         str
    email:        EmailStr
    role:         UserRole
    display_name: str
    created_at:   datetime
```

### Model Config & Settings

```python
from pydantic import BaseModel, ConfigDict


class UserORM(BaseModel):
    """Model that can be created from SQLAlchemy ORM objects."""
    model_config = ConfigDict(
        from_attributes=True,          # Allows ORM object → Pydantic
        str_strip_whitespace=True,     # Auto-strip whitespace from strings
        populate_by_name=True,         # Allow both alias and real name
        json_schema_extra={            # Example in Swagger
            "example": {
                "id": 1,
                "name": "Alice Khan",
                "email": "alice@example.com"
            }
        }
    )
    id:    int
    name:  str
    email: str
```

### Schema Inheritance for DRY Code

```python
from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    """Shared fields across all product schemas."""
    name:        str
    description: Optional[str] = None
    price:       float


class ProductCreate(ProductBase):
    """Used when creating — all base fields required."""
    pass


class ProductUpdate(ProductBase):
    """Used when updating — all fields optional."""
    name:        Optional[str]   = None
    description: Optional[str]   = None
    price:       Optional[float] = None


class ProductInDB(ProductBase):
    """Returned from DB — includes server-generated fields."""
    id:         int
    created_at: str
    updated_at: str
```

### ✅ Best Practices

- **Separate models** for Create / Update / Response — never reuse one model for all
- Use `EmailStr` from `pydantic[email]` for email validation
- Use `Field(...)` (Ellipsis) for required fields — it's explicit
- Use `model_config = ConfigDict(from_attributes=True)` when working with ORMs

### ❌ Common Mistakes

```python
# ❌ Don't mutate model fields directly after creation
user = UserCreate(name="alice", ...)
user.name = "bob"  # Works but breaks immutability expectations

# ✅ Use model_copy for updates
updated = user.model_copy(update={"name": "Bob"})

# ❌ Don't use .dict() — deprecated in Pydantic v2
data = user.dict()

# ✅ Use .model_dump()
data = user.model_dump()
data = user.model_dump(exclude={"password"})
data = user.model_dump(include={"name", "email"})
```

---

## 📌 Topic 7: Basic Validation

### FastAPI + Pydantic Validation in Action

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

app = FastAPI()


class RegisterRequest(BaseModel):
    username: str   = Field(..., min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
    email:    str   = Field(..., description="Must be a valid email address")
    password: str   = Field(..., min_length=8)
    age:      int   = Field(..., ge=13, le=120, description="Must be between 13 and 120")
    phone:    Optional[str] = Field(None, description="E.164 format: +923001234567")

    @field_validator("email")
    @classmethod
    def validate_email_format(cls, v: str) -> str:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, v):
            raise ValueError("Invalid email format")
        return v.lower()

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        pattern = r'^\+[1-9]\d{7,14}$'
        if not re.match(pattern, v):
            raise ValueError("Phone must be in E.164 format, e.g. +923001234567")
        return v

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if not re.search(r'[A-Z]', v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r'\d', v):
            raise ValueError("Password must contain at least one digit")
        return v


@app.post("/register", status_code=201)
def register(data: RegisterRequest):
    return {"message": "User registered successfully", "username": data.username}
```

### Validation Error Response (Automatic)

When validation fails, FastAPI automatically returns:
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "username"],
      "msg": "String should have at least 3 characters",
      "input": "ab",
      "ctx": {"min_length": 3}
    }
  ]
}
```

### Custom Validation Errors

```python
from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Custom format for validation errors."""
    errors = []
    for error in exc.errors():
        errors.append({
            "field":   " → ".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type":    error["type"]
        })
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation failed",
            "errors":  errors
        }
    )
```

---

## 🧪 MINI PROJECT #1: Personal Contact Book API

### Problem Statement
Build a RESTful Contact Book API that allows users to create, read, update, and delete contacts. This covers all Beginner-level concepts.

### Features
- ✅ Add a contact (name, email, phone, category)
- ✅ List all contacts with search & pagination
- ✅ Get a single contact by ID
- ✅ Update contact details
- ✅ Delete a contact
- ✅ Input validation with Pydantic
- ✅ Auto-generated Swagger documentation

### Folder Structure

```
contact_book/
├── main.py              # App entry point
├── models.py            # Pydantic models
├── database.py          # In-memory data store
├── routers/
│   └── contacts.py      # Contact endpoints
├── requirements.txt
└── README.md
```

### Step-by-Step Implementation

**Step 1: `requirements.txt`**
```
fastapi==0.111.0
uvicorn[standard]==0.29.0
pydantic[email]==2.7.0
```

**Step 2: `models.py`**
```python
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from enum import Enum
import re


class ContactCategory(str, Enum):
    family     = "family"
    friend     = "friend"
    colleague  = "colleague"
    other      = "other"


class ContactBase(BaseModel):
    name:     str             = Field(..., min_length=2, max_length=100, example="Ali Hassan")
    email:    Optional[EmailStr] = None
    phone:    Optional[str]   = Field(None, example="+923001234567")
    category: ContactCategory = ContactCategory.other
    notes:    Optional[str]   = Field(None, max_length=500)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v):
        if v and not re.match(r'^\+?[1-9]\d{7,14}$', v):
            raise ValueError("Invalid phone number format")
        return v


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    name:     Optional[str]             = Field(None, min_length=2, max_length=100)
    email:    Optional[EmailStr]        = None
    phone:    Optional[str]             = None
    category: Optional[ContactCategory] = None
    notes:    Optional[str]             = None


class ContactResponse(ContactBase):
    id:         int
    created_at: str
```

**Step 3: `database.py`**
```python
from datetime import datetime
from typing import Optional

contacts_db: dict[int, dict] = {}
_counter = 0


def get_all(search: Optional[str] = None, skip: int = 0, limit: int = 10):
    results = list(contacts_db.values())
    if search:
        q = search.lower()
        results = [c for c in results if q in c["name"].lower() or q in (c.get("email") or "").lower()]
    return results[skip : skip + limit]


def get_by_id(contact_id: int):
    return contacts_db.get(contact_id)


def create(data: dict) -> dict:
    global _counter
    _counter += 1
    contact = {
        "id":         _counter,
        "created_at": datetime.utcnow().isoformat(),
        **data
    }
    contacts_db[_counter] = contact
    return contact


def update(contact_id: int, data: dict) -> Optional[dict]:
    if contact_id not in contacts_db:
        return None
    contacts_db[contact_id] = {**contacts_db[contact_id], **data}
    return contacts_db[contact_id]


def delete(contact_id: int) -> bool:
    if contact_id not in contacts_db:
        return False
    del contacts_db[contact_id]
    return True
```

**Step 4: `routers/contacts.py`**
```python
from fastapi import APIRouter, HTTPException, Query, Path, status
from typing import List, Optional
from models import ContactCreate, ContactUpdate, ContactResponse
import database

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/", response_model=List[ContactResponse])
def list_contacts(
    skip:   int           = Query(0, ge=0),
    limit:  int           = Query(10, le=100),
    search: Optional[str] = Query(None, min_length=1)
):
    return database.get_all(search=search, skip=skip, limit=limit)


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int = Path(..., ge=1)):
    contact = database.get_by_id(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail=f"Contact #{contact_id} not found")
    return contact


@router.post("/", response_model=ContactResponse, status_code=201)
def create_contact(data: ContactCreate):
    return database.create(data.model_dump())


@router.patch("/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, data: ContactUpdate):
    updated = database.update(contact_id, data.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail=f"Contact #{contact_id} not found")
    return updated


@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: int = Path(..., ge=1)):
    if not database.delete(contact_id):
        raise HTTPException(status_code=404, detail=f"Contact #{contact_id} not found")
```

**Step 5: `main.py`**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contacts

app = FastAPI(
    title="Contact Book API",
    description="A simple personal contact management API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.router)

@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "docs": "/docs"}
```

### Bonus Improvements (Portfolio)

- 🔐 Add JWT authentication (covered in Intermediate level)
- 🗄️ Replace in-memory DB with SQLite/PostgreSQL using SQLAlchemy
- 📤 Add CSV export endpoint (`/contacts/export`)
- 🔔 Add WebSocket for real-time contact updates
- 🐳 Dockerize the application

---

# ⚙️ Level 2 — Intermediate

---

## 📌 Topic 8: Dependency Injection

### What is DI? (Analogy)

Imagine ordering from a restaurant:
- You don't go to the farm to get ingredients
- You don't cook the food yourself
- The restaurant **injects** the prepared meal to you

In FastAPI, **dependencies are injected automatically** — you declare what you need, FastAPI provides it.

### Basic Dependencies

```python
from fastapi import FastAPI, Depends, HTTPException, Query
from typing import Optional

app = FastAPI()


# ─── Simple dependency ──────────────────────────────────────────────────────
def get_pagination(
    skip:  int = Query(0,  ge=0),
    limit: int = Query(10, le=100)
) -> dict:
    return {"skip": skip, "limit": limit}


@app.get("/items")
def list_items(pagination: dict = Depends(get_pagination)):
    # `pagination` is automatically populated by FastAPI
    return {"pagination": pagination, "items": ["a", "b", "c"]}


@app.get("/products")
def list_products(pagination: dict = Depends(get_pagination)):
    # Reuse the same pagination logic across routes
    return {"pagination": pagination, "products": ["x", "y", "z"]}
```

### Class-Based Dependencies

```python
from fastapi import FastAPI, Depends

app = FastAPI()


class CommonQueryParams:
    """Reusable query parameters as a class."""

    def __init__(
        self,
        skip:   int           = 0,
        limit:  int           = 10,
        search: Optional[str] = None,
        sort:   str           = "created_at"
    ):
        self.skip   = skip
        self.limit  = limit
        self.search = search
        self.sort   = sort


@app.get("/users")
def list_users(params: CommonQueryParams = Depends()):
    return {
        "skip":   params.skip,
        "limit":  params.limit,
        "search": params.search,
        "sort":   params.sort
    }
```

### Database Session Dependency (Production Pattern)

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal  # We'll set this up in the DB topic

app = FastAPI()


def get_db():
    """
    Yields a DB session per request and closes it when the request is done.
    This is the standard pattern for SQLAlchemy + FastAPI.
    """
    db = SessionLocal()
    try:
        yield db           # ← gives the session to the route
    finally:
        db.close()         # ← always runs, even on exception


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```

### Nested Dependencies

```python
from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional

app = FastAPI()


# Level 1 dependency
def get_api_key(x_api_key: Optional[str] = Header(None)) -> str:
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key required")
    return x_api_key


# Level 2 dependency (uses level 1)
def verify_admin(api_key: str = Depends(get_api_key)) -> bool:
    if api_key != "secret-admin-key":
        raise HTTPException(status_code=403, detail="Admin access required")
    return True


# Route uses the highest-level dependency
@app.delete("/users/{user_id}")
def delete_user(user_id: int, _: bool = Depends(verify_admin)):
    return {"message": f"User {user_id} deleted by admin"}
```

### 💡 Pro Tips

- Use `Depends()` without arguments for class-based dependencies (shorthand)
- Dependencies are **cached per request** by default — use `use_cache=False` to disable
- DI is perfect for: DB sessions, auth checks, pagination, rate limiters, logging

---

## 📌 Topic 9: APIRouter & Project Structure

### Why Structure Matters

A flat `main.py` with 50+ routes is unmaintainable. Use `APIRouter` to split routes into logical modules — like a **filing cabinet with labeled drawers**.

### Production-Grade Folder Structure

```
myapp/
├── main.py                    # App factory, middleware, routers
├── config.py                  # Settings (env vars)
├── database.py                # DB engine, session factory
├── dependencies.py            # Shared dependencies
│
├── models/                    # SQLAlchemy ORM models
│   ├── __init__.py
│   ├── user.py
│   └── product.py
│
├── schemas/                   # Pydantic models
│   ├── __init__.py
│   ├── user.py
│   └── product.py
│
├── routers/                   # Route handlers
│   ├── __init__.py
│   ├── auth.py
│   ├── users.py
│   └── products.py
│
├── services/                  # Business logic
│   ├── __init__.py
│   ├── user_service.py
│   └── email_service.py
│
├── tests/                     # Test suite
│   ├── conftest.py
│   ├── test_users.py
│   └── test_products.py
│
├── .env
├── requirements.txt
└── Dockerfile
```

### APIRouter in Practice

```python
# routers/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.user import UserCreate, UserResponse, UserUpdate
from services import user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={
        404: {"description": "User not found"},
        401: {"description": "Not authenticated"}
    }
)


@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_all(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    if user_service.email_exists(db, data.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    return user_service.create(db, data)
```

```python
# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, products, auth

def create_app() -> FastAPI:
    """Application factory pattern."""
    app = FastAPI(
        title="My Production API",
        version="1.0.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc"
    )

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://myapp.com"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(auth.router,     prefix="/api/v1")
    app.include_router(users.router,    prefix="/api/v1")
    app.include_router(products.router, prefix="/api/v1")

    return app


app = create_app()
```

---

## 📌 Topic 10: Middleware

### What is Middleware?

Middleware is code that runs **before and after every request** — like a security guard at the building entrance who checks everyone going in and out.

```
Request  → [Middleware 1] → [Middleware 2] → Route Handler
Response ← [Middleware 1] ← [Middleware 2] ← Route Handler
```

### Built-in CORS Middleware

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend on a different domain to call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://myapp.com",
        "https://admin.myapp.com",
        # "http://localhost:3000"  # For local development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization", "Content-Type"],
)
```

### Custom Middleware: Request Logging

```python
import time
import uuid
import logging
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)
app = FastAPI()


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        start_time = time.perf_counter()

        # Attach request_id for tracing
        request.state.request_id = request_id

        logger.info(
            f"[{request_id}] → {request.method} {request.url.path}"
        )

        response = await call_next(request)

        duration_ms = (time.perf_counter() - start_time) * 1000
        logger.info(
            f"[{request_id}] ← {response.status_code} "
            f"({duration_ms:.2f}ms)"
        )

        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = f"{duration_ms:.2f}ms"
        return response


app.add_middleware(RequestLoggingMiddleware)
```

### Custom Middleware: Rate Limiting (Simple)

```python
import time
from collections import defaultdict
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Simple in-memory rate limiter (use Redis in production)
request_counts: dict[str, list] = defaultdict(list)
RATE_LIMIT   = 100   # requests
TIME_WINDOW  = 60    # seconds


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now       = time.time()
        window_start = now - TIME_WINDOW

        # Remove old entries
        request_counts[client_ip] = [
            t for t in request_counts[client_ip] if t > window_start
        ]

        if len(request_counts[client_ip]) >= RATE_LIMIT:
            return JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded. Try again later."},
                headers={"Retry-After": str(TIME_WINDOW)}
            )

        request_counts[client_ip].append(now)
        return await call_next(request)


app.add_middleware(RateLimitMiddleware)
```

---

## 📌 Topic 11: Exception Handling

### FastAPI's HTTPException

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID must be a positive integer"
        )

    user = fetch_user_from_db(user_id)  # hypothetical
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found",
            headers={"X-Error-Code": "USER_NOT_FOUND"}  # Custom header
        )
    return user
```

### Custom Exception Classes

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


# ─── Custom exception classes ─────────────────────────────────────────────────
class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400, error_code: str = "APP_ERROR"):
        self.message     = message
        self.status_code = status_code
        self.error_code  = error_code
        super().__init__(message)


class ResourceNotFoundError(AppException):
    def __init__(self, resource: str, identifier):
        super().__init__(
            message=f"{resource} with ID '{identifier}' was not found",
            status_code=404,
            error_code="RESOURCE_NOT_FOUND"
        )


class DuplicateResourceError(AppException):
    def __init__(self, resource: str, field: str, value: str):
        super().__init__(
            message=f"{resource} with {field}='{value}' already exists",
            status_code=409,
            error_code="DUPLICATE_RESOURCE"
        )


# ─── Global exception handler ─────────────────────────────────────────────────
app = FastAPI()


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success":    False,
            "error_code": exc.error_code,
            "message":    exc.message
        }
    )


# ─── Usage ────────────────────────────────────────────────────────────────────
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = None  # DB lookup returns None
    if not user:
        raise ResourceNotFoundError("User", user_id)
    return user


@app.post("/users")
def create_user(email: str):
    existing = True  # DB found a duplicate
    if existing:
        raise DuplicateResourceError("User", "email", email)
```

### Global Unhandled Exception Handler

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

app    = FastAPI()
logger = logging.getLogger(__name__)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch-all for unhandled exceptions — never expose stack traces in production."""
    logger.exception(f"Unhandled exception on {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An internal server error occurred. Please try again later."
        }
    )
```

---

## 📌 Topic 12: Authentication with JWT

### How JWT Works

```
1. User logs in with credentials
2. Server validates → creates a signed JWT token
3. Client stores the token (localStorage / cookie)
4. Client sends token in every request: Authorization: Bearer <token>
5. Server verifies signature on each request
6. If valid → process request; if invalid → 401 Unauthorized
```

### JWT Token Structure

```
Header.Payload.Signature
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsImV4cCI6MTcxOTAwMDAwMH0.abc123
```

### Full JWT Implementation

```python
# auth.py
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# pip install python-jose[cryptography] passlib[bcrypt]

SECRET_KEY       = "your-super-secret-key-change-in-production"  # Use env var!
ALGORITHM        = "HS256"
ACCESS_EXPIRE_M  = 30    # 30 minutes
REFRESH_EXPIRE_D = 7     # 7 days

pwd_context       = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme     = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# ─── Password utilities ───────────────────────────────────────────────────────
def hash_password(plain: str) -> str:
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# ─── Token creation ───────────────────────────────────────────────────────────
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire    = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_EXPIRE_M))
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    expire    = datetime.now(timezone.utc) + timedelta(days=REFRESH_EXPIRE_D)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ─── Token verification ───────────────────────────────────────────────────────
def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


# ─── Current user dependency ──────────────────────────────────────────────────
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = decode_token(token)
    if payload.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid token type")
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    return {"user_id": user_id, "role": payload.get("role", "viewer")}


def require_role(*roles):
    """Role-based access control dependency."""
    def checker(current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return checker
```

```python
# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth import (
    hash_password, verify_password,
    create_access_token, create_refresh_token, decode_token
)

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Simulated user store — replace with DB
fake_users = {
    "alice@example.com": {
        "id": "1",
        "email": "alice@example.com",
        "hashed_password": hash_password("Secret123!"),
        "role": "admin"
    }
}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    token_data = {"sub": user["id"], "role": user["role"]}
    return {
        "access_token":  create_access_token(token_data),
        "refresh_token": create_refresh_token(token_data),
        "token_type":    "bearer"
    }


@router.post("/refresh")
def refresh(refresh_token: str):
    payload = decode_token(refresh_token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    token_data = {"sub": payload["sub"], "role": payload.get("role")}
    return {
        "access_token": create_access_token(token_data),
        "token_type":   "bearer"
    }


@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return current_user
```

### 🎯 Interview Questions

> **Q: What is the difference between authentication and authorization?**
> A: Authentication verifies *who* you are (login with credentials). Authorization determines *what* you can do (role/permission checks). JWT handles authentication; role-based access control handles authorization.

> **Q: Where should JWTs be stored on the client side?**
> A: For web apps, httpOnly cookies are the most secure (prevents XSS). localStorage is convenient but vulnerable to XSS. For mobile apps, secure storage (Keychain/Keystore) is recommended. Never store tokens in regular cookies or sessionStorage for sensitive apps.

---

## 📌 Topic 13: Database Integration with SQLAlchemy

### Setup

```bash
pip install sqlalchemy psycopg2-binary alembic
# For SQLite (development): pip install sqlalchemy
```

### Database Configuration

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

engine = create_engine(
    DATABASE_URL,
    # SQLite only — needed for async/multithreaded use
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### ORM Models

```python
# models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SAEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base
import enum


class UserRole(str, enum.Enum):
    admin  = "admin"
    editor = "editor"
    viewer = "viewer"


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    email      = Column(String(255), unique=True, index=True, nullable=False)
    password   = Column(String(255), nullable=False)
    role       = Column(SAEnum(UserRole), default=UserRole.viewer)
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc),
                        onupdate=lambda: datetime.now(timezone.utc))

    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
```

### CRUD Service Layer

```python
# services/user_service.py
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional, List
from models.user import User
from schemas.user import UserCreate, UserUpdate
from auth import hash_password


class UserService:
    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        search: Optional[str] = None
    ) -> List[User]:
        query = db.query(User).filter(User.is_active == True)
        if search:
            query = query.filter(
                or_(
                    User.name.ilike(f"%{search}%"),
                    User.email.ilike(f"%{search}%")
                )
            )
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id, User.is_active == True).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create(db: Session, data: UserCreate) -> User:
        user = User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password),
            role=data.role
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update(db: Session, user: User, data: UserUpdate) -> User:
        update_data = data.model_dump(exclude_unset=True)
        if "password" in update_data:
            update_data["password"] = hash_password(update_data["password"])
        for field, value in update_data.items():
            setattr(user, field, value)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def soft_delete(db: Session, user: User) -> User:
        user.is_active = False
        db.commit()
        return user


user_service = UserService()
```

---

## 📌 Topic 14: CRUD APIs (Full Example)

```python
# routers/users.py (full CRUD with DB)
from fastapi import APIRouter, Depends, HTTPException, Query, Path, status
from sqlalchemy.orm import Session
from typing import Optional, List
from database import get_db
from services.user_service import user_service
from schemas.user import UserCreate, UserResponse, UserUpdate
from auth import get_current_user, require_role

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
def list_users(
    skip:   int           = Query(0, ge=0),
    limit:  int           = Query(10, le=100),
    search: Optional[str] = Query(None),
    db:     Session       = Depends(get_db),
    _:      dict          = Depends(get_current_user)  # Protected route
):
    return user_service.get_all(db, skip=skip, limit=limit, search=search)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int     = Path(..., ge=1),
    db:      Session = Depends(get_db),
    _:       dict    = Depends(get_current_user)
):
    user = user_service.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    """Public endpoint — no auth required for registration."""
    if user_service.get_by_email(db, data.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    return user_service.create(db, data)


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(
    user_id:      int        = Path(..., ge=1),
    data:         UserUpdate = ...,
    db:           Session    = Depends(get_db),
    current_user: dict       = Depends(get_current_user)
):
    user = user_service.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Users can only update themselves, admins can update anyone
    if str(user.id) != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Cannot update another user's profile")
    return user_service.update(db, user, data)


@router.delete("/{user_id}", status_code=204)
def delete_user(
    user_id: int     = Path(..., ge=1),
    db:      Session = Depends(get_db),
    _:       dict    = Depends(require_role("admin"))  # Admin only
):
    user = user_service.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_service.soft_delete(db, user)
```

---

## 🧪 MINI PROJECT #2: Secure Blog API with JWT Auth

### Problem Statement
Build a full blog API where users can register, login, create posts, and manage their content. Non-authenticated users can read posts; authenticated users can write.

### Features
- 👤 User registration & login (JWT)
- 📝 Create / Read / Update / Delete posts
- 🔐 Authorization (only post author can edit/delete)
- 🏷️ Post categories & tags
- 📄 Pagination and search
- 🗄️ SQLite database (SQLAlchemy)

### Folder Structure

```
blog_api/
├── main.py
├── database.py
├── auth.py
├── models/
│   ├── user.py
│   └── post.py
├── schemas/
│   ├── user.py
│   └── post.py
├── services/
│   ├── user_service.py
│   └── post_service.py
├── routers/
│   ├── auth.py
│   ├── users.py
│   └── posts.py
├── .env
└── requirements.txt
```

### Key Implementation Highlights

```python
# models/post.py
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base


class Post(Base):
    __tablename__ = "posts"

    id         = Column(Integer, primary_key=True, index=True)
    title      = Column(String(200), nullable=False)
    content    = Column(Text, nullable=False)
    slug       = Column(String(250), unique=True, index=True)
    is_published = Column(Boolean, default=False)
    author_id  = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    author = relationship("User", back_populates="posts")
```

```python
# routers/posts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth import get_current_user
from services.post_service import post_service
from schemas.post import PostCreate, PostResponse, PostUpdate

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse, status_code=201)
def create_post(
    data:         PostCreate = ...,
    db:           Session    = Depends(get_db),
    current_user: dict       = Depends(get_current_user)
):
    return post_service.create(db, data, author_id=int(current_user["user_id"]))


@router.delete("/{post_id}", status_code=204)
def delete_post(
    post_id:      int     = ...,
    db:           Session = Depends(get_db),
    current_user: dict    = Depends(get_current_user)
):
    post = post_service.get_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if str(post.author_id) != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    post_service.delete(db, post)
```

### Bonus Improvements (Portfolio)
- 📸 Image upload for post cover photos (S3/Cloudinary)
- 💬 Comments with nested replies
- ❤️ Like/bookmark system
- 📧 Email notifications on new comments
- 🔍 Full-text search with Elasticsearch

---

# 🔥 Level 3 — Advanced

---

## 📌 Topic 15: Async Programming (async/await)

### Why Async Matters

Think of sync code as a **single-window bank** — one customer at a time. Async code is like a **bank with a ticket system** — the teller takes your request, tells you to wait, serves others, then comes back to you.

```
Sync:  Request1(5s) → Request2(5s) → Request3(5s) = 15s total
Async: Request1 start → Request2 start → Request3 start → all finish ~5s
```

### Sync vs Async in FastAPI

```python
from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()


# ─── SYNCHRONOUS (blocks the thread) ─────────────────────────────────────────
@app.get("/sync")
def sync_endpoint():
    import time
    time.sleep(2)  # Blocks the entire server for 2 seconds!
    return {"mode": "sync"}


# ─── ASYNCHRONOUS (non-blocking) ─────────────────────────────────────────────
@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(2)  # Other requests can run while this waits
    return {"mode": "async"}


# ─── Async HTTP calls (external APIs) ────────────────────────────────────────
@app.get("/github/{username}")
async def get_github_profile(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/users/{username}")
        response.raise_for_status()
        return response.json()


# ─── Parallel async operations ────────────────────────────────────────────────
@app.get("/dashboard")
async def get_dashboard(user_id: int):
    # Run multiple DB queries in parallel
    users_task    = asyncio.create_task(fetch_user(user_id))
    posts_task    = asyncio.create_task(fetch_user_posts(user_id))
    stats_task    = asyncio.create_task(fetch_user_stats(user_id))

    user, posts, stats = await asyncio.gather(users_task, posts_task, stats_task)

    return {"user": user, "posts": posts, "stats": stats}
```

### Async SQLAlchemy (Production Pattern)

```python
# For truly async DB operations, use SQLAlchemy 2.0 async
# pip install sqlalchemy[asyncio] asyncpg

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://user:pass@localhost/db"

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session


# In your route:
from sqlalchemy import select

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### 💡 Pro Tips

- Use `async def` when calling I/O-bound operations (DB, HTTP, file I/O)
- Use `def` for CPU-bound operations (FastAPI runs them in a thread pool automatically)
- Use `asyncio.gather()` to run multiple async operations in parallel
- Never use `time.sleep()` in async code — use `await asyncio.sleep()`

---

## 📌 Topic 16: Background Tasks

### What Are Background Tasks?

Background tasks run **after the response is sent** to the client. Perfect for:
- Sending emails
- Generating reports
- Logging analytics
- Processing uploaded files

```python
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import asyncio
import logging

app    = FastAPI()
logger = logging.getLogger(__name__)


# ─── Background task functions ────────────────────────────────────────────────
async def send_welcome_email(email: str, name: str):
    """Simulate email sending."""
    await asyncio.sleep(2)  # Simulate SMTP delay
    logger.info(f"Welcome email sent to {email}")
    # In reality: await send_smtp_email(...)


def log_user_action(user_id: int, action: str):
    """Sync logging task."""
    logger.info(f"User {user_id} performed: {action}")


# ─── Routes using background tasks ────────────────────────────────────────────
class RegisterRequest(BaseModel):
    name:  str
    email: str


@app.post("/register", status_code=201)
async def register(
    data:    RegisterRequest,
    tasks:   BackgroundTasks
):
    # 1. Save to DB (fast)
    user_id = 42  # Pretend we saved the user

    # 2. Schedule background tasks (non-blocking)
    tasks.add_task(send_welcome_email, data.email, data.name)
    tasks.add_task(log_user_action, user_id, "registration")

    # 3. Respond immediately — email sends in background
    return {
        "message": "Registration successful! Welcome email is on its way.",
        "user_id": user_id
    }
```

### Celery for Heavy Background Jobs (Production)

```bash
pip install celery[redis] redis
```

```python
# celery_app.py
from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
)


@celery.task(bind=True, max_retries=3)
def process_video(self, video_id: int):
    """Heavy task that runs in a Celery worker process."""
    try:
        # ... process video ...
        pass
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)  # Retry in 60 seconds


# In your FastAPI route:
@app.post("/videos/{video_id}/process")
def trigger_processing(video_id: int):
    task = process_video.delay(video_id)
    return {"task_id": task.id, "status": "queued"}


@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task   = celery.AsyncResult(task_id)
    return {"task_id": task_id, "status": task.status, "result": task.result}
```

---

## 📌 Topic 17: WebSockets

### Real-Time Communication with FastAPI

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import json

app = FastAPI()


# ─── Connection Manager ───────────────────────────────────────────────────────
class ConnectionManager:
    def __init__(self):
        self.active: List[WebSocket]               = []
        self.rooms:  dict[str, List[WebSocket]]    = {}

    async def connect(self, ws: WebSocket, room: str = "global"):
        await ws.accept()
        self.active.append(ws)
        if room not in self.rooms:
            self.rooms[room] = []
        self.rooms[room].append(ws)

    def disconnect(self, ws: WebSocket, room: str = "global"):
        self.active.remove(ws)
        if room in self.rooms and ws in self.rooms[room]:
            self.rooms[room].remove(ws)

    async def send_personal(self, message: dict, ws: WebSocket):
        await ws.send_json(message)

    async def broadcast_to_room(self, message: dict, room: str):
        for ws in self.rooms.get(room, []):
            try:
                await ws.send_json(message)
            except Exception:
                pass  # Client disconnected


manager = ConnectionManager()


# ─── Chat WebSocket ───────────────────────────────────────────────────────────
@app.websocket("/ws/chat/{room}/{username}")
async def chat_websocket(ws: WebSocket, room: str, username: str):
    await manager.connect(ws, room)
    await manager.broadcast_to_room(
        {"type": "system", "message": f"{username} joined the room"},
        room
    )
    try:
        while True:
            data = await ws.receive_json()
            await manager.broadcast_to_room(
                {
                    "type":    "message",
                    "user":    username,
                    "message": data.get("message", ""),
                    "room":    room
                },
                room
            )
    except WebSocketDisconnect:
        manager.disconnect(ws, room)
        await manager.broadcast_to_room(
            {"type": "system", "message": f"{username} left the room"},
            room
        )
```

### Simple WebSocket Test Client (HTML)

```html
<!-- test_ws.html -->
<!DOCTYPE html>
<html>
<body>
<h2>Chat Room</h2>
<div id="messages"></div>
<input id="msg" type="text" placeholder="Type a message">
<button onclick="sendMessage()">Send</button>

<script>
const ws = new WebSocket("ws://localhost:8000/ws/chat/general/alice");
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    document.getElementById("messages").innerHTML +=
        `<p><b>${data.user || "System"}:</b> ${data.message}</p>`;
};
function sendMessage() {
    const msg = document.getElementById("msg").value;
    ws.send(JSON.stringify({ message: msg }));
}
</script>
</body>
</html>
```

---

## 📌 Topic 18: Caching with Redis

```bash
pip install redis[asyncio] fastapi-cache2[redis]
```

```python
from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
import json

app = FastAPI()


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8")
    FastAPICache.init(RedisBackend(redis), prefix="myapp-cache")


# ─── Cache with decorator ─────────────────────────────────────────────────────
@app.get("/products/{product_id}")
@cache(expire=300)  # Cache for 5 minutes
async def get_product(product_id: int):
    # This expensive DB query only runs every 5 minutes
    return await fetch_product_from_db(product_id)


# ─── Manual caching pattern ───────────────────────────────────────────────────
import redis.asyncio as aioredis

async def get_redis() -> aioredis.Redis:
    return aioredis.from_url("redis://localhost:6379", decode_responses=True)


@app.get("/leaderboard")
async def get_leaderboard(redis: aioredis.Redis = Depends(get_redis)):
    cache_key = "leaderboard:top10"
    cached    = await redis.get(cache_key)

    if cached:
        return {"source": "cache", "data": json.loads(cached)}

    # Compute expensive leaderboard
    data = [{"rank": i, "user": f"user_{i}", "score": 1000 - i*10}
            for i in range(1, 11)]

    # Store in Redis with 60-second TTL
    await redis.setex(cache_key, 60, json.dumps(data))
    return {"source": "database", "data": data}


# ─── Cache invalidation ───────────────────────────────────────────────────────
@app.post("/leaderboard/invalidate")
async def invalidate_leaderboard(redis: aioredis.Redis = Depends(get_redis)):
    await redis.delete("leaderboard:top10")
    return {"message": "Leaderboard cache cleared"}
```

---

## 📌 Topic 19: Rate Limiting

```bash
pip install slowapi
```

```python
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


# ─── Route-level rate limits ──────────────────────────────────────────────────
@app.get("/public")
@limiter.limit("30/minute")
async def public_endpoint(request: Request):
    return {"message": "Public endpoint"}


@app.post("/auth/login")
@limiter.limit("5/minute")              # Strict limit on login attempts
async def login(request: Request):
    return {"message": "Login attempt"}


@app.get("/api/data")
@limiter.limit("100/minute;1000/hour")  # Multiple limits
async def get_data(request: Request):
    return {"data": "premium content"}
```

---

## 📌 Topic 20: API Versioning

```python
from fastapi import FastAPI
from routers.v1 import users as users_v1
from routers.v2 import users as users_v2

app = FastAPI(title="Versioned API")

# Version 1 (legacy — still supported)
app.include_router(users_v1.router, prefix="/api/v1", tags=["v1 - Users"])

# Version 2 (current — with breaking changes)
app.include_router(users_v2.router, prefix="/api/v2", tags=["v2 - Users"])
```

```python
# routers/v2/users.py — new response format
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class PaginatedResponse(BaseModel):
    data:        list
    total:       int
    page:        int
    per_page:    int
    total_pages: int


@router.get("/users", response_model=PaginatedResponse)
def list_users_v2(page: int = 1, per_page: int = 10):
    """v2: Returns paginated response with metadata."""
    # Breaking change from v1: different response structure
    return {
        "data":        [],
        "total":       0,
        "page":        page,
        "per_page":    per_page,
        "total_pages": 0
    }
```

---

## 📌 Topic 21: Testing with Pytest

```bash
pip install pytest pytest-asyncio httpx
```

```python
# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app

# Use in-memory SQLite for tests
TEST_DB = "sqlite:///./test.db"
engine  = create_engine(TEST_DB, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
```

```python
# tests/test_users.py
import pytest
from fastapi.testclient import TestClient


class TestUserEndpoints:
    def test_create_user_success(self, client: TestClient):
        payload = {"name": "Test User", "email": "test@example.com", "password": "Secret123!"}
        response = client.post("/api/v1/users", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "test@example.com"
        assert "password" not in data  # Never expose password!
        assert "id" in data

    def test_create_user_duplicate_email(self, client: TestClient):
        payload = {"name": "User 1", "email": "dup@example.com", "password": "Secret123!"}
        client.post("/api/v1/users", json=payload)  # First creation
        response = client.post("/api/v1/users", json=payload)  # Duplicate
        assert response.status_code == 409

    def test_get_user_not_found(self, client: TestClient):
        response = client.get("/api/v1/users/99999")
        assert response.status_code == 404

    def test_list_users_pagination(self, client: TestClient):
        response = client.get("/api/v1/users?skip=0&limit=5")
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestAuthEndpoints:
    def test_login_success(self, client: TestClient):
        # Create user first
        client.post("/api/v1/users", json={
            "name": "Auth User", "email": "auth@example.com", "password": "Secret123!"
        })
        response = client.post(
            "/api/v1/auth/login",
            data={"username": "auth@example.com", "password": "Secret123!"}
        )
        assert response.status_code == 200
        assert "access_token" in response.json()

    def test_login_wrong_password(self, client: TestClient):
        response = client.post(
            "/api/v1/auth/login",
            data={"username": "auth@example.com", "password": "WrongPass!"}
        )
        assert response.status_code == 401

    def test_protected_route_without_token(self, client: TestClient):
        response = client.get("/api/v1/users")
        assert response.status_code == 401
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=. --cov-report=html

# Run specific test file
pytest tests/test_users.py -v

# Run tests matching a pattern
pytest tests/ -k "test_login" -v
```

---

## 🧪 MINI PROJECT #3: E-Commerce Product API

### Problem Statement
Build a production-grade product catalog API with categories, inventory, and search — the kind recruiters look for in portfolios.

### Features
- 🛍️ Product CRUD with categories
- 🔍 Full-text search with filters (price range, category, in-stock)
- 📦 Inventory management
- 🔐 JWT auth (admin for write, public for read)
- 💾 Redis caching on product lists
- ⚡ Async endpoints
- ✅ Pytest test suite

### Folder Structure

```
ecommerce_api/
├── main.py
├── database.py
├── auth.py
├── models/
│   ├── product.py
│   └── category.py
├── schemas/
│   ├── product.py
│   └── category.py
├── services/
│   ├── product_service.py
│   └── cache_service.py
├── routers/
│   ├── products.py
│   └── categories.py
├── tests/
│   ├── conftest.py
│   ├── test_products.py
│   └── test_categories.py
├── .env
├── docker-compose.yml
└── requirements.txt
```

### Key Implementation Highlights

```python
# services/product_service.py
from sqlalchemy import select, and_, or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

async def search_products(
    db:           AsyncSession,
    keyword:      Optional[str]   = None,
    category_id:  Optional[int]   = None,
    min_price:    Optional[float] = None,
    max_price:    Optional[float] = None,
    in_stock:     bool            = False,
    skip:         int             = 0,
    limit:        int             = 20
):
    query = select(Product).where(Product.is_active == True)

    if keyword:
        query = query.where(
            or_(
                Product.name.ilike(f"%{keyword}%"),
                Product.description.ilike(f"%{keyword}%")
            )
        )
    if category_id:
        query = query.where(Product.category_id == category_id)
    if min_price is not None:
        query = query.where(Product.price >= min_price)
    if max_price is not None:
        query = query.where(Product.price <= max_price)
    if in_stock:
        query = query.where(Product.stock_quantity > 0)

    total_query  = select(func.count()).select_from(query.subquery())
    total        = (await db.execute(total_query)).scalar()
    result       = await db.execute(query.offset(skip).limit(limit))
    products     = result.scalars().all()

    return {"items": products, "total": total, "skip": skip, "limit": limit}
```

### Bonus Improvements (Portfolio)
- 🖼️ Product image upload (AWS S3)
- ⭐ Reviews and ratings system
- 🛒 Shopping cart (Redis-based)
- 📊 Admin dashboard with sales analytics
- 📦 Order management with status tracking

---

# 🏭 Level 4 — Expert / Production

---

## 📌 Topic 22: Dockerizing FastAPI

### Dockerfile

```dockerfile
# Dockerfile
FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ─── Dependency layer (cached separately) ────────────────────────────────────
FROM base AS deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ─── Application layer ────────────────────────────────────────────────────────
FROM deps AS app
COPY . .

# Create non-root user (security best practice)
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000

# Production command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### docker-compose.yml

```yaml
# docker-compose.yml
version: "3.9"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=${SECRET_KEY}
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER:     postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB:       myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout:  5s
      retries:  5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - api
    restart: unless-stopped

volumes:
  postgres_data:
```

### Nginx Configuration

```nginx
# nginx.conf
events { worker_connections 1024; }

http {
    upstream fastapi_app {
        server api:8000;
    }

    server {
        listen 80;
        server_name myapp.com;
        return 301 https://$host$request_uri;
    }

    server {
        listen 443 ssl;
        server_name myapp.com;

        ssl_certificate     /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;

        location / {
            proxy_pass       http://fastapi_app;
            proxy_set_header Host              $host;
            proxy_set_header X-Real-IP         $remote_addr;
            proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /ws/ {
            proxy_pass         http://fastapi_app;
            proxy_http_version 1.1;
            proxy_set_header   Upgrade    $http_upgrade;
            proxy_set_header   Connection "upgrade";
        }
    }
}
```

---

## 📌 Topic 23: CI/CD Basics

### GitHub Actions Pipeline

```yaml
# .github/workflows/ci.yml
name: FastAPI CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # ─── Test Job ───────────────────────────────────────────────────────────────
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER:     testuser
          POSTGRES_PASSWORD: testpass
          POSTGRES_DB:       testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Cache pip packages
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

      - name: Install dependencies
        run: pip install -r requirements.txt pytest pytest-cov httpx

      - name: Run tests with coverage
        env:
          DATABASE_URL: postgresql://testuser:testpass@localhost/testdb
          SECRET_KEY:   test-secret-key
        run: pytest tests/ -v --cov=. --cov-report=xml

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3

  # ─── Build & Push Docker Image ──────────────────────────────────────────────
  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v4

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: myusername/myapp:latest,myusername/myapp:${{ github.sha }}

  # ─── Deploy to VPS ──────────────────────────────────────────────────────────
  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Deploy to VPS via SSH
        uses: appleboy/ssh-action@v1
        with:
          host:     ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USER }}
          key:      ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /app
            docker pull myusername/myapp:latest
            docker-compose up -d --no-deps api
            docker system prune -f
```

---

## 📌 Topic 24: Deployment (Cloud/VPS)

### Deployment on Ubuntu VPS (DigitalOcean / Hetzner)

```bash
# 1. Server setup
ssh root@your-vps-ip

# Create non-root user
adduser deploy
usermod -aG sudo deploy
rsync --archive --chown=deploy:deploy ~/.ssh /home/deploy

# 2. Install Docker
curl -fsSL https://get.docker.com | sh
usermod -aG docker deploy

# 3. Install Docker Compose
apt install docker-compose-plugin

# 4. Clone your project
su - deploy
git clone https://github.com/yourusername/myapp.git /app
cd /app

# 5. Set up environment variables
cp .env.example .env
nano .env  # Fill in production values

# 6. Run the stack
docker compose up -d

# 7. Set up SSL with Let's Encrypt
docker run --rm \
  -v /etc/letsencrypt:/etc/letsencrypt \
  -v /var/www/certbot:/var/www/certbot \
  -p 80:80 certbot/certbot certonly \
  --standalone -d yourdomain.com
```

### Alembic Database Migrations

```bash
pip install alembic

# Initialize migrations
alembic init migrations

# Create a new migration
alembic revision --autogenerate -m "add users table"

# Apply migrations
alembic upgrade head

# Rollback one step
alembic downgrade -1
```

```python
# migrations/env.py (configure target metadata)
from models.user    import User    # noqa: F401 — import all models
from models.product import Product # noqa: F401
from database import Base

target_metadata = Base.metadata
```

---

## 📌 Topic 25: Logging & Monitoring

### Structured Logging Setup

```python
# logging_config.py
import logging
import sys
from pythonjsonlogger import jsonlogger  # pip install python-json-logger


def setup_logging(level: str = "INFO"):
    logger    = logging.getLogger()
    handler   = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(name)s %(levelname)s %(message)s",
        rename_fields={"asctime": "timestamp", "levelname": "level"}
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, level.upper()))
    return logger


# main.py
from logging_config import setup_logging
logger = setup_logging()

# In routes:
logger.info("User created", extra={"user_id": 42, "email": "user@example.com"})
logger.warning("Rate limit approached", extra={"ip": "1.2.3.4", "count": 95})
logger.error("DB connection failed", extra={"db_url": "redacted"}, exc_info=True)
```

### Health Check Endpoints

```python
from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import get_db
import redis
import time

app = FastAPI()


@app.get("/health", tags=["Health"])
async def health_check():
    """Basic liveness check — used by load balancers."""
    return {"status": "ok", "timestamp": time.time()}


@app.get("/health/ready", tags=["Health"])
async def readiness_check(db: Session = Depends(get_db)):
    """Readiness check — verifies dependencies are up."""
    checks = {}

    # Check DB
    try:
        db.execute("SELECT 1")
        checks["database"] = "ok"
    except Exception as e:
        checks["database"] = f"error: {e}"

    # Check Redis
    try:
        r = redis.from_url("redis://localhost:6379")
        r.ping()
        checks["redis"] = "ok"
    except Exception as e:
        checks["redis"] = f"error: {e}"

    all_ok     = all(v == "ok" for v in checks.values())
    status_code = 200 if all_ok else 503

    return JSONResponse(
        status_code=status_code,
        content={"status": "ready" if all_ok else "degraded", "checks": checks}
    )
```

---

## 📌 Topic 26: Security — OWASP Top 10 for APIs

### 1. Broken Object Level Authorization (BOLA)

```python
# ❌ Vulnerable: Anyone can access any user's data
@app.get("/users/{user_id}/profile")
def get_profile(user_id: int):
    return db.get_user(user_id)  # No ownership check!

# ✅ Secure: Verify ownership
@app.get("/users/{user_id}/profile")
def get_profile(user_id: int, current_user: dict = Depends(get_current_user)):
    if str(user_id) != current_user["user_id"] and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    return db.get_user(user_id)
```

### 2. Broken Authentication

```python
# ✅ Secure token validation with all checks
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Verify token type
    if payload.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid token type")

    # Verify user still exists and is active
    user = db.get_user(payload["sub"])
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    return user
```

### 3. Injection Prevention

```python
# ❌ SQL Injection vulnerable
@app.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    return db.execute(f"SELECT * FROM users WHERE name = '{q}'")  # DANGEROUS!

# ✅ Safe: SQLAlchemy parameterized queries
@app.get("/search")
def search(q: str, db: Session = Depends(get_db)):
    return db.query(User).filter(User.name.ilike(f"%{q}%")).all()
```

### 4. Security Headers Middleware

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"]   = "nosniff"
        response.headers["X-Frame-Options"]          = "DENY"
        response.headers["X-XSS-Protection"]         = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"]  = "default-src 'self'"
        response.headers["Referrer-Policy"]          = "strict-origin-when-cross-origin"
        # Remove server identification
        del response.headers["server"] if "server" in response.headers else None
        return response


app.add_middleware(SecurityHeadersMiddleware)
```

### 5. Input Sanitization

```python
import bleach
from pydantic import BaseModel, field_validator


class CommentCreate(BaseModel):
    content: str

    @field_validator("content")
    @classmethod
    def sanitize_html(cls, v: str) -> str:
        # Allow only safe HTML tags
        allowed_tags  = ["p", "br", "strong", "em", "ul", "li"]
        allowed_attrs = {}
        return bleach.clean(v, tags=allowed_tags, attributes=allowed_attrs, strip=True)
```

---

## 🧪 MINI PROJECT #4: Task Management API (Production-Ready)

### Problem Statement
Build a production-grade Kanban task management API with team workspaces, role-based access control, background notifications, and Redis caching.

### Features
- 🏢 Workspaces with team members
- 📋 Projects and task boards
- ✅ Tasks with status, priority, assignee, due dates
- 🔔 Email notifications (background tasks)
- 💾 Redis caching on board data
- 🔐 JWT + RBAC (admin, editor, viewer)
- 🐳 Docker + Docker Compose
- ✅ Full Pytest suite
- 📊 Health checks & structured logging

### Folder Structure

```
taskmanager/
├── main.py
├── config.py                  # Pydantic Settings
├── database.py
├── auth.py
├── models/
│   ├── user.py
│   ├── workspace.py
│   ├── project.py
│   └── task.py
├── schemas/
│   ├── user.py
│   ├── workspace.py
│   └── task.py
├── services/
│   ├── task_service.py
│   ├── notification_service.py
│   └── cache_service.py
├── routers/
│   ├── auth.py
│   ├── workspaces.py
│   ├── tasks.py
│   └── health.py
├── middleware/
│   ├── logging.py
│   └── security.py
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── migrations/
├── .env
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml
└── requirements.txt
```

### Bonus Improvements (Portfolio)
- 📱 WebSocket for real-time board updates
- 📎 File attachments (S3)
- 📈 Project analytics and reporting
- 🔗 GitHub/Jira integration webhooks
- 📅 Calendar view for tasks

---

# 🤖 AI Integration with FastAPI

---

## Building AI-Powered APIs

FastAPI is the **#1 choice** for serving AI models and integrating with LLM APIs. Here's why:
- Async support handles concurrent AI requests efficiently
- Streaming support for LLM token-by-token output
- Type validation for AI request/response schemas
- Easy deployment alongside ML models

---

## Example 1: Chatbot API

```python
# pip install openai fastapi uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
from openai import AsyncOpenAI
import json

app    = FastAPI(title="AI Chatbot API")
client = AsyncOpenAI(api_key="your-openai-api-key")  # Use env var!


class Message(BaseModel):
    role:    str   # "user" | "assistant" | "system"
    content: str


class ChatRequest(BaseModel):
    messages:    List[Message]
    model:       str  = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens:  int   = 1000
    stream:      bool  = False


class ChatResponse(BaseModel):
    message:    str
    model:      str
    usage:      dict
    finish_reason: str


# ─── Standard (non-streaming) ─────────────────────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await client.chat.completions.create(
            model=request.model,
            messages=[m.model_dump() for m in request.messages],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        choice = response.choices[0]
        return ChatResponse(
            message=choice.message.content,
            model=response.model,
            usage=response.usage.model_dump(),
            finish_reason=choice.finish_reason
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─── Streaming response ───────────────────────────────────────────────────────
@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Returns tokens as Server-Sent Events."""
    async def event_generator():
        try:
            stream = await client.chat.completions.create(
                model=request.model,
                messages=[m.model_dump() for m in request.messages],
                temperature=request.temperature,
                max_tokens=request.max_tokens,
                stream=True,
            )
            async for chunk in stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    yield f"data: {json.dumps({'token': delta.content})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control":     "no-cache",
            "X-Accel-Buffering": "no"
        }
    )
```

**Request Example:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is FastAPI?"}
    ]
  }'
```

**Response Example:**
```json
{
  "message": "FastAPI is a modern, high-performance Python web framework for building APIs...",
  "model": "gpt-4o-mini",
  "usage": {"prompt_tokens": 25, "completion_tokens": 80, "total_tokens": 105},
  "finish_reason": "stop"
}
```

---

## Example 2: Text Summarizer API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import AsyncOpenAI
from enum import Enum

app    = FastAPI(title="AI Text Summarizer")
client = AsyncOpenAI()


class SummaryLength(str, Enum):
    short  = "short"    # 1-2 sentences
    medium = "medium"   # 1 paragraph
    long   = "long"     # Multiple paragraphs


class SummarizeRequest(BaseModel):
    text:          str           = Field(..., min_length=50, max_length=50_000)
    length:        SummaryLength = SummaryLength.medium
    language:      str           = "English"
    bullet_points: bool          = False


class SummarizeResponse(BaseModel):
    summary:       str
    original_words: int
    summary_words:  int
    reduction_pct:  float


@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    length_map = {
        SummaryLength.short:  "1-2 sentences",
        SummaryLength.medium: "1 paragraph (3-5 sentences)",
        SummaryLength.long:   "3-5 paragraphs"
    }

    format_instruction = "Format as bullet points." if request.bullet_points else ""

    prompt = f"""Summarize the following text in {length_map[request.length]}.
Write the summary in {request.language}. {format_instruction}

TEXT:
{request.text}

SUMMARY:"""

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert text summarizer. Be concise and accurate."},
                {"role": "user",   "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        summary = response.choices[0].message.content.strip()

        original_wc = len(request.text.split())
        summary_wc  = len(summary.split())
        reduction   = round((1 - summary_wc / original_wc) * 100, 1)

        return SummarizeResponse(
            summary=summary,
            original_words=original_wc,
            summary_words=summary_wc,
            reduction_pct=reduction
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI error: {e}")
```

**Request Example:**
```json
{
  "text": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints. The key features are: Fast: Very high performance, on par with NodeJS and Go... [long text]",
  "length": "short",
  "language": "English",
  "bullet_points": false
}
```

**Response Example:**
```json
{
  "summary": "FastAPI is a high-performance Python web framework for building APIs using type hints, offering automatic documentation and async support.",
  "original_words": 450,
  "summary_words": 22,
  "reduction_pct": 95.1
}
```

---

## Example 3: AI Code Reviewer API

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
from openai import AsyncOpenAI
from typing import List
from enum import Enum

app    = FastAPI(title="AI Code Reviewer API")
client = AsyncOpenAI()


class ProgrammingLanguage(str, Enum):
    python     = "Python"
    javascript = "JavaScript"
    typescript = "TypeScript"
    java       = "Java"
    go         = "Go"


class ReviewFocus(str, Enum):
    security     = "security"
    performance  = "performance"
    readability  = "readability"
    best_practice = "best_practices"
    all          = "all"


class CodeReviewRequest(BaseModel):
    code:     str               = Field(..., min_length=10, max_length=10_000)
    language: ProgrammingLanguage
    focus:    ReviewFocus       = ReviewFocus.all
    context:  str               = Field("", max_length=500,
                                        description="Optional context about what the code does")


class CodeIssue(BaseModel):
    severity:    str   # "critical" | "warning" | "suggestion"
    line_range:  str   # e.g., "15-18"
    description: str
    suggestion:  str


class CodeReviewResponse(BaseModel):
    overall_score: int           # 0-100
    summary:       str
    issues:        List[CodeIssue]
    improved_code: str
    positive_aspects: List[str]


@app.post("/review", response_model=CodeReviewResponse)
async def review_code(request: CodeReviewRequest):
    focus_map = {
        ReviewFocus.security:      "Focus especially on security vulnerabilities.",
        ReviewFocus.performance:   "Focus especially on performance bottlenecks.",
        ReviewFocus.readability:   "Focus especially on code readability and clarity.",
        ReviewFocus.best_practice: "Focus especially on best practices and design patterns.",
        ReviewFocus.all:           "Cover security, performance, readability, and best practices."
    }

    system_prompt = f"""You are a senior {request.language.value} developer and code reviewer.
Review the provided code and respond ONLY with valid JSON in this exact format:
{{
  "overall_score": <0-100 integer>,
  "summary": "<2-3 sentence summary>",
  "issues": [
    {{
      "severity": "<critical|warning|suggestion>",
      "line_range": "<line numbers or 'general'>",
      "description": "<what's wrong>",
      "suggestion": "<how to fix it>"
    }}
  ],
  "improved_code": "<complete rewritten code>",
  "positive_aspects": ["<thing done well 1>", "<thing done well 2>"]
}}"""

    user_prompt = f"""{focus_map[request.focus]}
{"Context: " + request.context if request.context else ""}

```{request.language.value.lower()}
{request.code}
```"""

    import json
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ],
        temperature=0.2,
        response_format={"type": "json_object"}
    )

    result = json.loads(response.choices[0].message.content)
    return CodeReviewResponse(**result)
```

**Request Example:**
```json
{
  "code": "def get_user(id):\n    query = f'SELECT * FROM users WHERE id = {id}'\n    return db.execute(query)",
  "language": "Python",
  "focus": "security",
  "context": "A user lookup function in a web API"
}
```

**Response Example:**
```json
{
  "overall_score": 15,
  "summary": "The code contains a critical SQL injection vulnerability and lacks error handling. It needs immediate security remediation before any production use.",
  "issues": [
    {
      "severity": "critical",
      "line_range": "2",
      "description": "SQL Injection vulnerability: user input is directly interpolated into query string",
      "suggestion": "Use parameterized queries: db.execute('SELECT * FROM users WHERE id = ?', (id,))"
    }
  ],
  "improved_code": "def get_user(user_id: int):\n    try:\n        result = db.execute('SELECT * FROM users WHERE id = ?', (user_id,))\n        return result.fetchone()\n    except Exception as e:\n        logger.error(f'DB error: {e}')\n        raise",
  "positive_aspects": ["Function has a clear, descriptive name"]
}
```

---

## 🧪 MINI PROJECT #5: AI-Powered Resume Analyzer API

### Problem Statement
Build an API that accepts a resume (text or PDF) and a job description, uses AI to analyze the match, give a score, and provide actionable improvement suggestions.

### Features
- 📄 Resume upload (PDF / plain text)
- 📝 Job description input
- 🤖 AI-powered match scoring (0-100)
- 💡 Gap analysis (missing skills, keywords)
- ✍️ Rewrite suggestions for each section
- 📊 ATS (Applicant Tracking System) optimization tips
- 💾 Redis caching (same resume+JD = cached result)
- 🔐 API key authentication

### Folder Structure

```
resume_analyzer/
├── main.py
├── config.py
├── routers/
│   └── analyzer.py
├── services/
│   ├── ai_service.py
│   ├── pdf_service.py
│   └── cache_service.py
├── schemas/
│   └── analysis.py
├── tests/
│   └── test_analyzer.py
├── .env
├── Dockerfile
└── requirements.txt
```

### Key Implementation

```python
# services/ai_service.py
from openai import AsyncOpenAI
from schemas.analysis import ResumeAnalysisResponse
import json

client = AsyncOpenAI()


async def analyze_resume(resume_text: str, job_description: str) -> ResumeAnalysisResponse:
    prompt = f"""Analyze this resume against the job description and respond with JSON:
{{
  "match_score": <0-100>,
  "summary": "<2 sentence executive summary>",
  "matching_skills": ["<skill1>", "<skill2>"],
  "missing_skills": ["<skill1>", "<skill2>"],
  "ats_keywords_missing": ["<keyword1>"],
  "section_feedback": {{
    "summary": "<feedback on professional summary>",
    "experience": "<feedback on experience section>",
    "skills": "<feedback on skills section>",
    "education": "<feedback on education section>"
  }},
  "top_improvements": ["<improvement1>", "<improvement2>", "<improvement3>"],
  "rewritten_summary": "<AI-rewritten professional summary>"
}}

RESUME:
{resume_text[:4000]}

JOB DESCRIPTION:
{job_description[:2000]}"""

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert ATS resume analyzer and career coach."},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.3,
        response_format={"type": "json_object"}
    )

    return ResumeAnalysisResponse(**json.loads(response.choices[0].message.content))
```

### Bonus Improvements (Portfolio)
- 📧 Email the analysis report as PDF
- 🌐 Multi-language resume support
- 📊 Dashboard with application tracking
- 🔄 Version comparison (before/after resume)
- 🤝 LinkedIn profile import

---

# 🚀 Portfolio-Ready Projects

---

## Project 1: Multi-Tenant SaaS API

**Description:** A scalable backend for a SaaS product where multiple companies (tenants) share the same infrastructure but have completely isolated data.

**Key Features:**
- Tenant isolation via schema-per-tenant PostgreSQL
- Custom domain support per tenant
- Subscription tiers (Free / Pro / Enterprise)
- Usage-based billing integration (Stripe)
- Admin panel API

**Why It Impresses Recruiters:** Shows understanding of multi-tenancy, database design, and SaaS architecture — rare and valuable skills.

**Tech Stack:** FastAPI + PostgreSQL + Redis + Stripe + Docker

---

## Project 2: Real-Time Collaborative API

**Description:** Backend for a real-time document editing tool (like Google Docs lite).

**Key Features:**
- WebSocket rooms per document
- Operational Transform (OT) for conflict resolution
- Redis Pub/Sub for multi-server scaling
- Document version history
- Permission system (owner / editor / viewer)

**Why It Impresses Recruiters:** WebSockets + Redis Pub/Sub + real-time systems = senior-level skills.

**Tech Stack:** FastAPI + WebSockets + Redis Pub/Sub + PostgreSQL

---

## Project 3: AI Content Generation Platform

**Description:** API platform for generating, storing, and managing AI-generated content (blog posts, social media, emails).

**Key Features:**
- Multi-model support (GPT-4, Claude, Gemini)
- Template system with variables
- Token usage tracking and cost estimation
- Content history and versioning
- Rate limiting per user tier

**Why It Impresses Recruiters:** Combines AI integration with production API design — hot market right now.

**Tech Stack:** FastAPI + OpenAI/Anthropic APIs + PostgreSQL + Redis + Celery

---

## Project 4: Financial Data API

**Description:** Personal finance tracking API with transaction categorization, budget alerts, and spending analytics.

**Key Features:**
- Bank transaction import (CSV/OFX)
- AI-powered auto-categorization
- Budget management with overspend alerts
- Monthly spending reports (PDF export)
- Multi-currency support with live rates

**Why It Impresses Recruiters:** Shows data processing, external API integration, and report generation.

**Tech Stack:** FastAPI + SQLAlchemy + Celery + Redis + OpenAI + ReportLab

---

## Project 5: DevOps Monitoring API

**Description:** Lightweight server monitoring API that collects metrics, detects anomalies, and sends alerts.

**Key Features:**
- Agent-based metric collection (CPU, memory, disk, network)
- Time-series data storage (TimescaleDB or InfluxDB)
- Anomaly detection (Z-score / ML model)
- Alert rules engine (email, Slack, webhook)
- Grafana-compatible metrics endpoint

**Why It Impresses Recruiters:** Shows infrastructure knowledge, time-series data, and DevOps awareness.

**Tech Stack:** FastAPI + TimescaleDB + Redis + Celery + Slack API

---

# 💰 Freelancing Guide

---

## Services to Offer as a FastAPI Developer

### Service Packages

**Starter Gig (~$50–$150)**
- Simple REST API (5-10 endpoints)
- Pydantic validation
- Basic CRUD with SQLite/PostgreSQL
- Swagger documentation
- *Timeline: 1-3 days*

**Standard Package ($200–$600)**
- Full REST API with authentication (JWT)
- Database integration + migrations
- Role-based access control
- Docker deployment
- Basic test suite
- *Timeline: 5-10 days*

**Premium Package ($800–$2,500)**
- Production-grade API
- Microservices architecture
- Redis caching + rate limiting
- CI/CD pipeline (GitHub Actions)
- VPS/cloud deployment
- Monitoring setup
- Full test coverage
- *Timeline: 2-4 weeks*

**AI Integration Add-on (+$200–$800)**
- OpenAI/Claude API integration
- Chatbot endpoint
- Document analysis
- Content generation API

### Where to Find Clients

- **Upwork** — Most freelance API jobs
- **Toptal** — Premium clients, high rates (requires vetting)
- **Fiverr** — Good for packaged services
- **LinkedIn** — Cold outreach to startups
- **X (Twitter)** — Build in public, attract inbound

### Pricing Strategy

```
Year 1 (Building portfolio):   $15–$30/hr  |  Focus on reviews + case studies
Year 2 (Established):          $40–$70/hr  |  Niche in AI or fintech
Year 3+ (Expert):              $80–$150/hr |  Productized services + retainers
```

### 💡 Freelancing Pro Tips

1. **Specialize** — "FastAPI + AI APIs" commands 3x the rate of generic backend
2. **Document everything** — Deliver Swagger docs + README with every project
3. **Offer retainers** — Monthly maintenance contracts ($300–$500/mo) for passive income
4. **Build public tools** — A free open-source FastAPI template = inbound leads
5. **Collect testimonials** — Social proof is worth more than a portfolio

---

# 🧑‍💻 Hiring & Career Tips

---

## What Recruiters Look For in a FastAPI Developer

### Technical Expectations

| Level    | Expected Knowledge |
|----------|--------------------|
| Junior   | CRUD APIs, Pydantic, basic auth, SQLAlchemy |
| Mid      | DI, testing, Docker, async, JWT, Redis |
| Senior   | System design, microservices, CI/CD, monitoring, security |
| Staff    | Architecture decisions, API gateway, distributed systems |

### GitHub Profile Tips

1. **Pin your best 6 repos** — They're the first thing recruiters see
2. **Every repo needs:**
   - Clear, professional README with project description, tech stack, setup instructions, API docs link
   - Working demo (Railway / Render free tier)
   - Tests with coverage badge
   - Docker support
3. **README structure for backend projects:**
   ```
   # Project Name
   ## What it does (2-3 sentences)
   ## Tech Stack
   ## Quick Start (3-5 commands)
   ## API Documentation (link)
   ## Key Features
   ## Architecture Diagram
   ## Environment Variables (list, never values)
   ## Running Tests
   ```
4. **Show commit quality** — Meaningful commit messages, not "fix stuff"

### Resume Tips for Backend Developer

**Header:** Name + Location + Email + GitHub + LinkedIn + Portfolio/Demo

**Summary (2-3 lines):**
> Backend developer with 2+ years building REST APIs with FastAPI and Python. Specialized in AI integrations and cloud deployments. Shipped products used by 10K+ users.

**Skills Section:**
```
Languages:   Python, SQL
Frameworks:  FastAPI, SQLAlchemy, Pydantic, Celery
Databases:   PostgreSQL, Redis, SQLite
DevOps:      Docker, GitHub Actions, Nginx, AWS/GCP
Tools:       Git, Postman, Pytest, Alembic
Concepts:    REST API, JWT, WebSockets, Microservices, OWASP
```

**Project Section Format:**
```
[Project Name] | [Links: GitHub | Live Demo]
- Brief description of what it does and who uses it
- Metric: "Handles 500+ concurrent requests with <100ms response time"
- Metric: "Reduced API response time by 60% with Redis caching"
- Tech used: FastAPI, PostgreSQL, Redis, Docker, AWS EC2
```

### 🎯 Common Interview Questions at Companies

> **Q: How does FastAPI handle concurrent requests?**
> A: FastAPI uses Uvicorn (ASGI server) with async Python. For `async def` endpoints, it's truly non-blocking. For sync `def` endpoints, FastAPI runs them in a thread pool to avoid blocking the event loop.

> **Q: Explain your approach to API security.**
> A: Layered approach — HTTPS everywhere, JWT with short expiry + refresh tokens, RBAC for authorization, parameterized queries for SQL injection prevention, input validation via Pydantic, rate limiting, and OWASP-aligned security headers.

> **Q: How would you scale a FastAPI app to handle 1 million requests/day?**
> A: Horizontal scaling (multiple workers/containers), Redis for caching hot data, CDN for static assets, async I/O for all DB/HTTP calls, read replicas for DB, queue heavy tasks to Celery workers, and a load balancer (Nginx/ALB) in front.

---

# 🛣️ Roadmap: What's Next

---

## After FastAPI — Your Learning Path

```
                    [FastAPI ✅]
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
   [System Design] [API Security]   [AI/ML Serving]
         │               │               │
    Microservices    OAuth 2.0      LangChain
    Event Sourcing   API Gateway    Vector DBs
    CQRS             Zero Trust     RAG Systems
    Message Queues   WAF            Model Fine-tuning
    (RabbitMQ/Kafka)                FastAPI + HuggingFace
         │               │               │
         └───────────────┼───────────────┘
                         ▼
              [Cloud & Infrastructure]
                   AWS / GCP / Azure
                   Kubernetes (K8s)
                   Terraform (IaC)
                   Prometheus + Grafana
                         │
                         ▼
              [Senior/Staff Engineer]
                   System Design
                   Architecture Reviews
                   Technical Leadership
```

## Recommended Learning Order

**Month 1-2 (After FastAPI):**
- System Design fundamentals (Alex Xu's System Design Interview)
- PostgreSQL advanced (indexes, query optimization, EXPLAIN ANALYZE)
- Redis advanced (data structures, pub/sub, streams)

**Month 3-4:**
- Docker advanced + Kubernetes basics (K8s)
- Message queues: Celery → RabbitMQ → Kafka
- OAuth 2.0 + OpenID Connect

**Month 5-6:**
- Cloud: AWS (EC2, RDS, S3, Lambda, ECS)
- Infrastructure as Code (Terraform)
- Monitoring: Prometheus + Grafana + ELK Stack

**Month 7-12 (Pick a specialization):**
- **AI Backend:** LangChain, Vector DBs (Pinecone/pgvector), RAG, streaming LLMs
- **Fintech Backend:** PCI-DSS, Stripe, fraud detection, event sourcing
- **DevOps/Platform:** Kubernetes, service mesh (Istio), GitOps

## Essential Resources

**Books:**
- *Architecture Patterns with Python* — Harry Percival
- *Designing Data-Intensive Applications* — Martin Kleppmann
- *The Clean Architecture* — Robert C. Martin

**Courses:**
- FastAPI official docs: https://fastapi.tiangolo.com
- TestDriven.io FastAPI series
- ByteByteGo (System Design)

**Tools to Learn:**
- Postman → HTTPie → Bruno (API testing)
- pgAdmin → DBeaver (DB management)
- Grafana + Prometheus (monitoring)
- GitHub Actions + ArgoCD (CI/CD)

---

## 🏁 Final Words

FastAPI is not just a framework — it's a **career accelerator**. The combination of:

- **Modern Python** (type hints, async)
- **Production tooling** (Docker, CI/CD, monitoring)
- **AI integration** (the hottest market right now)
- **Clean API design** (RESTful, versioned, documented)

...makes a FastAPI developer extremely valuable in today's job market.

**The path is:**
1. ✅ Master the fundamentals (this guide)
2. 🔨 Build 2-3 real projects (portfolio)
3. 🚀 Deploy publicly (Railway, Render, VPS)
4. 📢 Share on GitHub + LinkedIn
5. 💼 Apply or freelance with confidence

> *"The best API is one that is well-documented, well-tested, secure by default, and a joy to use."*

---

*Guide maintained at: github.com/yourusername/fastapi-master-course*
*Last updated: 2025*
