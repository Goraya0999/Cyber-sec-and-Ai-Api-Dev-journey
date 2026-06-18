# CRUD Operations: PATCH Method in FastAPI

## What is the PATCH Method?

The **PATCH** method is an HTTP method used to **partially update an existing resource** on the server.

Unlike the `PUT` method, which replaces the entire resource, the `PATCH` method updates **only the specified fields**, leaving all other fields unchanged.

---

# Why Use the PATCH Method?

The PATCH method is used when only a small portion of a resource needs to be modified.

Instead of sending all resource data, the client sends only the fields that need to be updated.

This reduces network usage and improves efficiency.

---

# Characteristics of PATCH

* Updates an existing resource.
* Modifies only specified fields.
* Sends data in the **request body**.
* Does not replace the entire resource.
* More efficient than `PUT` for partial updates.

---

# PATCH Request Flow

```text
Client
   │
   │ PATCH Request + Updated Fields
   ▼
FastAPI Server
   │
   │ Find Existing Resource
   ▼
Database
   │
   │ Update Selected Fields
   ▼
FastAPI Server
   │
   │ Updated Response
   ▼
Client
```

---

# Import FastAPI

```python
from fastapi import FastAPI
```

---

# Create a FastAPI Application

```python
app = FastAPI()
```

---

# Basic PATCH Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.patch("/users/{id}")
def update_user(id: int):
    return {
        "message": f"User {id} updated successfully"
    }
```

---

# Endpoint Breakdown

| Component       | Description                                         |
| --------------- | --------------------------------------------------- |
| `@app.patch()`  | Registers a PATCH endpoint.                         |
| `"/users/{id}"` | URL path containing the resource ID.                |
| `id: int`       | Path parameter identifying the resource.            |
| `update_user()` | Function executed when a PATCH request is received. |
| `return`        | Sends the response to the client.                   |

---

# Testing the Endpoint

### Request

```http
PATCH /users/1
```

### Response

```json
{
    "message": "User 1 updated successfully"
}
```

---

# PATCH Endpoint with Updated Data

```python
from fastapi import FastAPI

app = FastAPI()

@app.patch("/users/{id}")
def update_user(id: int, age: int):
    return {
        "id": id,
        "updated_age": age
    }
```

### Request

```http
PATCH /users/1?age=23
```

### Response

```json
{
    "id": 1,
    "updated_age": 23
}
```

> **Note:** This example uses query parameters for simplicity. In real-world FastAPI applications, PATCH requests typically send only the fields to update in the request body using a Pydantic model.

---

# PATCH Response Status Code

A successful PATCH request usually returns:

```http
200 OK
```

or

```http
204 No Content
```

Example:

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.patch("/users/{id}", status_code=status.HTTP_200_OK)
def update_user(id: int):
    return {
        "message": "User updated successfully"
    }
```

---

# PATCH vs PUT

| Feature            | PATCH                       | PUT                           |
| ------------------ | --------------------------- | ----------------------------- |
| Purpose            | Partially update a resource | Completely replace a resource |
| Updated Fields     | Only specified fields       | All fields                    |
| Request Data       | Partial resource            | Complete resource             |
| Efficiency         | Higher                      | Lower for small updates       |
| Common Status Code | 200 OK / 204 No Content     | 200 OK / 204 No Content       |

---

# Common Use Cases

* Changing a user's email address
* Updating a password
* Changing a profile picture
* Updating an account status
* Editing product prices
* Updating inventory quantity
* Modifying application settings

---

# Best Practices

* Use `PATCH` only for partial updates.
* Use a path parameter to identify the resource.
* Send only the fields that need to be changed.
* Return **200 OK** or **204 No Content** after a successful update.
* Validate incoming data before applying updates.
* Use Pydantic models for request body validation in production applications.
