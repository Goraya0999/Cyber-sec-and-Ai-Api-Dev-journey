# Query Parameters in FastAPI

## What are Query Parameters?

A **query parameter** is a key-value pair added to the end of a URL after the **question mark (`?`)**.

Query parameters are used to send **optional information** to the server without changing the URL path.

They help filter, search, sort, paginate, or customize the data returned by an API.

---

# Why Use Query Parameters?

Query parameters allow clients to request data in different ways using the same endpoint.

Instead of creating multiple endpoints, one endpoint can handle many different requests based on the provided query parameters.

---

# URL Structure

```text
https://example.com/path?key=value
```

### Components

| Component | Description                      |
| --------- | -------------------------------- |
| `?`       | Starts the query string          |
| `key`     | Parameter name                   |
| `=`       | Assigns a value to the parameter |
| `value`   | Parameter value                  |

---

# Basic Example

URL:

```text
/products?category=laptop
```

* Path: `/products`
* Query Parameter: `category=laptop`

---

# Query Parameter Syntax

```python
@app.get("/items")
def get_items(name: str):
    ...
```

If a parameter is **not part of the path**, FastAPI automatically treats it as a **query parameter**.

---

# Basic Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_user(name: str):
    return {"name": name}
```

Request:

```text
GET /users?name=Ali
```

Response:

```json
{
    "name": "Ali"
}
```

---

# Multiple Query Parameters

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products(category: str, brand: str):
    return {
        "category": category,
        "brand": brand
    }
```

Request:

```text
GET /products?category=Laptop&brand=HP
```

Response:

```json
{
    "category": "Laptop",
    "brand": "HP"
}
```

---

# Optional Query Parameters

A query parameter becomes optional by assigning it a default value.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_user(name: str = "Guest"):
    return {"name": name}
```

Request:

```text
GET /users
```

Response:

```json
{
    "name": "Guest"
}
```

Request:

```text
GET /users?name=Ali
```

Response:

```json
{
    "name": "Ali"
}
```

---

# Query Parameters with Different Data Types

## String (`str`)

```python
@app.get("/users")
def get_user(name: str):
    return {"name": name}
```

Example:

```text
GET /users?name=Ali
```

---

## Integer (`int`)

```python
@app.get("/users")
def get_user(age: int):
    return {"age": age}
```

Example:

```text
GET /users?age=25
```

---

## Float (`float`)

```python
@app.get("/products")
def get_product(price: float):
    return {"price": price}
```

Example:

```text
GET /products?price=99.99
```

---

## Boolean (`bool`)

FastAPI automatically converts common boolean values.

```python
@app.get("/users")
def get_user(active: bool):
    return {"active": active}
```

Example:

```text
GET /users?active=true
```

Response:

```json
{
    "active": true
}
```

Accepted values include:

* true
* false
* 1
* 0
* yes
* no
* on
* off

---

# Required Query Parameters

A query parameter without a default value is required.

```python
@app.get("/search")
def search(keyword: str):
    return {"keyword": keyword}
```

Valid request:

```text
GET /search?keyword=python
```

Missing parameter:

```text
GET /search
```

Response:

```http
422 Unprocessable Entity
```

---

# Query Parameters with Default Values

```python
@app.get("/products")
def get_products(limit: int = 10):
    return {"limit": limit}
```

Request:

```text
GET /products
```

Response:

```json
{
    "limit": 10
}
```

---

# Combining Path and Query Parameters

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int, active: bool = True):
    return {
        "id": id,
        "active": active
    }
```

Request:

```text
GET /users/5?active=false
```

Response:

```json
{
    "id": 5,
    "active": false
}
```

---

# Multiple Query Parameters

```python
@app.get("/search")
def search(
    keyword: str,
    page: int = 1,
    limit: int = 10
):
    return {
        "keyword": keyword,
        "page": page,
        "limit": limit
    }
```

Request:

```text
GET /search?keyword=python&page=2&limit=20
```

---

# Path Parameters vs Query Parameters

| Feature  | Path Parameter      | Query Parameter          |
| -------- | ------------------- | ------------------------ |
| Location | URL path            | After `?` in URL         |
| Required | Usually Yes         | Optional or Required     |
| Purpose  | Identify a resource | Filter or customize data |
| Example  | `/users/5`          | `/users?active=true`     |

---

# Common Use Cases

* Searching data
* Filtering results
* Sorting records
* Pagination
* Selecting language
* Enabling or disabling features
* Limiting returned records

---

# Best Practices

* Use path parameters to identify a specific resource.
* Use query parameters to filter, search, sort, or paginate data.
* Give query parameters meaningful names.
* Provide sensible default values when appropriate.
* Use proper type hints (`str`, `int`, `float`, `bool`) for automatic validation.
* Keep query parameter names short, clear, and descriptive.
