# CRUD Operations: PUT Method in FastAPI

## What is the PUT Method?

The **PUT** method is an HTTP method used to **completely replace an existing resource** on the server.

Unlike the `POST` method, which creates a new resource, the `PUT` method updates an existing resource by replacing all of its data.

---

# Why Use the PUT Method?

The PUT method is used when the client wants to update an existing resource with new information.

Common examples include:

* Updating a user's profile
* Replacing product information
* Updating an order
* Replacing employee details
* Updating customer information

---

# Characteristics of PUT

* Updates an existing resource.
* Replaces all fields of the resource.
* Sends data in the **request body**.
* Modifies server data.
* Is **idempotent**, meaning sending the same request multiple times produces the same result.

---

# PUT Request Flow

```text
Client
   │
   │ PUT Request + Updated Data
   ▼
FastAPI Server
   │
   │ Find Existing Resource
   ▼
Database
   │
   │ Replace Resource
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

# Basic PUT Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.put("/users/{id}")
def update_user(id: int):
    return {
        "message": f"User {id} updated successfully"
    }
```

---

# Endpoint Breakdown

| Component       | Description                                       |
| --------------- | ------------------------------------------------- |
| `@app.put()`    | Registers a PUT endpoint.                         |
| `"/users/{id}"` | URL path containing the resource ID.              |
| `id: int`       | Path parameter identifying the resource.          |
| `update_user()` | Function executed when a PUT request is received. |
| `return`        | Sends the response to the client.                 |

---

# Testing the Endpoint

### Request

```http
PUT /users/1
```

### Response

```json
{
    "message": "User 1 updated successfully"
}
```

---

# PUT Endpoint with Updated Data

```python
from fastapi import FastAPI

app = FastAPI()

@app.put("/users/{id}")
def update_user(id: int, name: str, age: int):
    return {
        "id": id,
        "name": name,
        "age": age
    }
```

### Request

```http
PUT /users/1?name=Ali&age=23
```

### Response

```json
{
    "id": 1,
    "name": "Ali",
    "age": 23
}
```

> **Note:** This example uses query parameters for simplicity. In real-world FastAPI applications, PUT requests usually send data in the request body using a Pydantic model.

---

# PUT Response Status Code

A successful PUT request usually returns:

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

@app.put("/users/{id}", status_code=status.HTTP_200_OK)
def update_user(id: int):
    return {
        "message": "User updated successfully"
    }
```

---

# PUT vs POST

| Feature            | POST                  | PUT                          |
| ------------------ | --------------------- | ---------------------------- |
| Purpose            | Create a new resource | Replace an existing resource |
| Resource Exists    | No                    | Yes                          |
| Sends Data         | Request Body          | Request Body                 |
| Idempotent         | No                    | Yes                          |
| Common Status Code | 201 Created           | 200 OK / 204 No Content      |

---

# Common Use Cases

* Updating user profiles
* Replacing product information
* Updating employee records
* Updating customer details
* Replacing order information
* Updating account settings

---

# Best Practices

* Use `PUT` only to replace an existing resource.
* Use a path parameter to identify the resource.
* Send the complete updated resource in the request body.
* Return **200 OK** or **204 No Content** after a successful update.
* Validate incoming data before updating the resource.
* Use Pydantic models for request body validation in production applications.
