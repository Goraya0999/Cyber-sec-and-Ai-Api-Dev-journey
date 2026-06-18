# Route Ordering in FastAPI

## What is Route Ordering?

**Route ordering** is the order in which API endpoints are defined in a FastAPI application.

FastAPI checks routes **from top to bottom**. The first route that matches the incoming request is executed.

Because of this, the order of route definitions is important.

---

# Why is Route Ordering Important?

FastAPI stops searching for a matching route as soon as it finds one.

If a **dynamic route** is defined before a **fixed (static) route**, the dynamic route may capture requests intended for the fixed route.

This can lead to unexpected behavior or validation errors.

---

# Static Route

A **static route** contains a fixed URL path.

Example:

```text
/users/me
```

The path never changes.

---

# Dynamic Route

A **dynamic route** contains one or more path parameters.

Example:

```text
/users/{id}
```

The value of `id` changes with each request.

---

# Incorrect Route Ordering

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    return {"id": id}

@app.get("/users/me")
def current_user():
    return {"user": "Current User"}
```

Request:

```text
GET /users/me
```

FastAPI first checks:

```text
/users/{id}
```

It treats `"me"` as the value of `id`.

Since `"me"` is not an integer, FastAPI returns:

```http
422 Unprocessable Entity
```

The `/users/me` endpoint is never reached.

---

# Correct Route Ordering

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
def current_user():
    return {"user": "Current User"}

@app.get("/users/{id}")
def get_user(id: int):
    return {"id": id}
```

Request:

```text
GET /users/me
```

Response:

```json
{
    "user": "Current User"
}
```

Request:

```text
GET /users/5
```

Response:

```json
{
    "id": 5
}
```

---

# How FastAPI Matches Routes

FastAPI processes routes sequentially.

```text
Incoming Request
        │
        ▼
Route 1
        │
   Match?
   │    │
 No     Yes
 │       │
 ▼       ▼
Route 2  Execute Route
 │
 ▼
Route 3
 │
 ▼
...
```

The first matching route is executed.

---

# Route Matching Example

Defined routes:

```python
@app.get("/products/latest")
```

```python
@app.get("/products/{id}")
```

### Request

```text
GET /products/latest
```

FastAPI matches:

```text
/products/latest
```

### Request

```text
GET /products/25
```

FastAPI matches:

```text
/products/{id}
```

---

# Best Practice

Always define **specific (static)** routes before **general (dynamic)** routes.

Correct order:

```text
/users/me
/users/profile
/users/settings
/users/{id}
```

Incorrect order:

```text
/users/{id}
/users/me
/users/profile
/users/settings
```

---

# Common Mistakes

## Defining Dynamic Routes First

```python
@app.get("/items/{id}")
```

before

```python
@app.get("/items/new")
```

This may cause `"new"` to be interpreted as the `id` parameter.

---

## Using Overlapping Routes

Avoid creating routes that can match the same URL unless their order is carefully planned.

Example:

```text
/posts/latest
/posts/{id}
```

Define `/posts/latest` before `/posts/{id}`.

---

# Best Practices

* Define static routes before dynamic routes.
* Keep route paths clear and descriptive.
* Avoid ambiguous URL patterns.
* Use meaningful path parameter names.
* Group related routes together for better readability.
* Test endpoints after adding new routes to ensure correct matching.
