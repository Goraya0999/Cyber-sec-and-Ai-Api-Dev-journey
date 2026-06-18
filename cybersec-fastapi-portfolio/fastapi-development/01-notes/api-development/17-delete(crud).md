# CRUD Operations: DELETE Method in FastAPI

## What is the DELETE Method?

The **DELETE** method is an HTTP method used to **remove an existing resource** from the server.

Unlike the `GET` method, which retrieves data, or the `POST` method, which creates data, the `DELETE` method permanently removes a resource identified by its unique ID or path parameter.

---

# Why Use the DELETE Method?

The DELETE method provides a standard way for clients to remove resources from an application.

It is commonly used when data is no longer needed or must be permanently deleted.

---

# Characteristics of DELETE

* Removes an existing resource.
* Uses a **path parameter** to identify the resource.
* Modifies server data.
* Usually does not require a request body.
* Is **idempotent**, meaning sending the same DELETE request multiple times has the same final result (the resource remains deleted).

---

# DELETE Request Flow

```text
Client
   │
   │ DELETE Request
   ▼
FastAPI Server
   │
   │ Find Resource
   ▼
Database
   │
   │ Delete Resource
   ▼
FastAPI Server
   │
   │ Success Response
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

# Basic DELETE Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.delete("/users/{id}")
def delete_user(id: int):
    return {
        "message": f"User {id} deleted successfully"
    }
```

---

# Endpoint Breakdown

| Component       | Description                                          |
| --------------- | ---------------------------------------------------- |
| `@app.delete()` | Registers a DELETE endpoint.                         |
| `"/users/{id}"` | URL path containing the resource ID.                 |
| `id: int`       | Path parameter identifying the resource.             |
| `delete_user()` | Function executed when a DELETE request is received. |
| `return`        | Sends the response back to the client.               |

---

# Testing the Endpoint

### Request

```http
DELETE /users/1
```

### Response

```json
{
    "message": "User 1 deleted successfully"
}
```

---

# DELETE Response Status Codes

A successful DELETE request commonly returns:

```http
200 OK
```

or

```http
204 No Content
```

* **200 OK**: The resource was deleted successfully, and a response body is returned.
* **204 No Content**: The resource was deleted successfully, and no response body is returned.

---

# Example Using Status Code

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.delete("/users/{id}", status_code=status.HTTP_200_OK)
def delete_user(id: int):
    return {
        "message": "User deleted successfully"
    }
```

---

# DELETE with Resource Validation

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

users = {
    1: "Ali",
    2: "Ahmed"
}

@app.delete("/users/{id}")
def delete_user(id: int):

    if id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    del users[id]

    return {
        "message": "User deleted successfully"
    }
```

---

# DELETE vs Other CRUD Methods

| Method | Purpose                      |
| ------ | ---------------------------- |
| GET    | Retrieve a resource          |
| POST   | Create a new resource        |
| PUT    | Replace an existing resource |
| PATCH  | Partially update a resource  |
| DELETE | Remove an existing resource  |

---

# Common Use Cases

* Deleting user accounts
* Removing products
* Deleting blog posts
* Removing comments
* Canceling orders
* Deleting uploaded files
* Removing customer records
* Deleting inventory items

---

# Best Practices

* Use a path parameter to identify the resource.
* Verify that the resource exists before deleting it.
* Return **404 Not Found** if the resource does not exist.
* Return **200 OK** or **204 No Content** after successful deletion.
* Avoid using a request body with DELETE unless specifically required by the API design.
* Validate permissions before allowing deletion.
* Use `HTTPException` to return meaningful error responses when deletion fails.
