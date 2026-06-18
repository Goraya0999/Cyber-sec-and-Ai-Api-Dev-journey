# CRUD Operations: POST Method in FastAPI

## What is the POST Method?

The **POST** method is an HTTP method used to **create a new resource** on the server.

Unlike the `GET` method, which only retrieves data, the `POST` method sends data from the client to the server for processing and storage.

---

# Why Use the POST Method?

The POST method is used whenever a client needs to add new data to a system.

Common examples include:

* User registration
* User login
* Creating products
* Placing orders
* Uploading data
* Creating blog posts

---

# Characteristics of POST

* Creates a new resource.
* Sends data in the **request body**.
* Modifies server data.
* Can trigger database insertion.
* Returns a success response after creation.

---

# POST Request Flow

```text
Client
   │
   │ POST Request + Data
   ▼
FastAPI Server
   │
   │ Process Data
   ▼
Database
   │
   │ Store Data
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

# Basic POST Endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user():
    return {"message": "User created successfully"}
```

---

# Endpoint Breakdown

| Component       | Description                                        |
| --------------- | -------------------------------------------------- |
| `@app.post()`   | Registers a POST endpoint.                         |
| `"/users"`      | URL path for creating users.                       |
| `create_user()` | Function executed when a POST request is received. |
| `return`        | Sends a response to the client.                    |

---

# Testing the Endpoint

### Request

```http
POST /users
```

### Response

```json
{
    "message": "User created successfully"
}
```

---

# POST Endpoint with Data

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
```

### Request

```http
POST /users?name=Ali&age=22
```

### Response

```json
{
    "name": "Ali",
    "age": 22
}
```

> **Note:** This example uses query parameters for simplicity. In real-world FastAPI applications, POST requests typically send data in the request body using a Pydantic model.

---

# POST Response Status Code

When a resource is successfully created, the standard HTTP status code is:

```http
201 Created
```

FastAPI can return this status code automatically by specifying it in the route decorator.

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully"}
```

---

# Difference Between GET and POST

| Feature              | GET                    | POST            |
| -------------------- | ---------------------- | --------------- |
| Purpose              | Retrieve data          | Create new data |
| Sends Data           | URL (Query Parameters) | Request Body    |
| Modifies Server Data | No                     | Yes             |
| Typical Status Code  | 200 OK                 | 201 Created     |

---

# Common Use Cases

* User registration
* User login
* Creating products
* Creating orders
* Adding comments
* Creating blog posts
* Submitting forms
* Uploading application data

---

# Best Practices

* Use `POST` only for creating new resources.
* Return **201 Created** when a resource is successfully created.
* Validate incoming data before processing it.
* Use descriptive endpoint names such as `/users`, `/products`, or `/orders`.
* In production applications, send POST data in the request body using Pydantic models instead of query parameters.
