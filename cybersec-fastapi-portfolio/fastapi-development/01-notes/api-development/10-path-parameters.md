# Path Parameters in FastAPI

## What is a Path Parameter?

A **path parameter** is a variable that is part of the URL path. It allows the client to send dynamic values through the URL.

Instead of creating separate endpoints for different resources, one endpoint can handle multiple values using path parameters.

For example, instead of creating:

```text
/users/1
/users/2
/users/3
```

You create a single endpoint:

```text
/users/{id}
```

The value inside `{}` is replaced by the actual value sent by the client.

---

# Why Use Path Parameters?

Path parameters make APIs:

* Dynamic
* Reusable
* Easy to maintain
* Scalable

Without path parameters, you would need to create a separate endpoint for every resource.

---

# Path Parameter Syntax

```python
@app.get("/users/{id}")
```

## Syntax Breakdown

### `{}`

Curly braces indicate that the value is a **path parameter**.

### `id`

The name of the path parameter.

It can be any valid Python variable name.

---

# Basic Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    return {"User ID": id}
```

Request:

```text
GET /users/5
```

Response:

```json
{
    "User ID": 5
}
```

---

# Path Parameter Data Types

FastAPI automatically converts and validates path parameters based on their type hints.

---

# String (`str`)

A string accepts text values.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{username}")
def get_user(username: str):
    return {"Username": username}
```

Request:

```text
GET /users/ali
```

Response:

```json
{
    "Username": "ali"
}
```

---

# Integer (`int`)

An integer accepts whole numbers.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    return {"User ID": id}
```

Request:

```text
GET /users/25
```

Response:

```json
{
    "User ID": 25
}
```

If the client sends:

```text
GET /users/abc
```

FastAPI returns:

```http
422 Unprocessable Entity
```

because `"abc"` is not a valid integer.

---

# Float (`float`)

A float accepts decimal numbers.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/price/{amount}")
def get_price(amount: float):
    return {"Price": amount}
```

Request:

```text
GET /price/99.95
```

Response:

```json
{
    "Price": 99.95
}
```

---

# Multiple Path Parameters

You can use more than one path parameter in the same endpoint.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "User ID": user_id,
        "Post ID": post_id
    }
```

Request:

```text
GET /users/5/posts/12
```

Response:

```json
{
    "User ID": 5,
    "Post ID": 12
}
```

---

# Using Union Types (`|`)

Python allows a parameter to accept multiple data types using the pipe operator (`|`).

## Syntax

```python
variable: type1 | type2
```

The `|` operator means **"or"**.

---

# Example

```python
id: str | int | float
```

This means the `id` parameter can accept:

* String
* Integer
* Float

---

# Example in FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{id}")
def get_item(id: str | int | float):
    return {
        "Value": id,
        "Type": type(id).__name__
    }
```

Possible requests:

```text
GET /items/10
```

```text
GET /items/10.5
```

```text
GET /items/laptop
```

---

# Type Validation

FastAPI validates path parameters automatically.

If the value does not match the declared type, FastAPI returns an error.

Example:

```python
@app.get("/users/{id}")
def get_user(id: int):
    return {"id": id}
```

Request:

```text
GET /users/abc
```

Response:

```http
422 Unprocessable Entity
```

---

# Path Parameter Examples

| Endpoint             | Parameter Type |
| -------------------- | -------------- |
| `/users/{id}`        | `int`          |
| `/users/{username}`  | `str`          |
| `/products/{price}`  | `float`        |
| `/files/{filename}`  | `str`          |
| `/orders/{order_id}` | `int`          |

---

# Best Practices

* Use descriptive parameter names.
* Choose the correct data type.
* Use `int` for IDs whenever possible.
* Use `str` for names and text values.
* Use `float` only for decimal values.
* Keep endpoint names meaningful and consistent.
* Let FastAPI handle automatic validation instead of manual type checking.
