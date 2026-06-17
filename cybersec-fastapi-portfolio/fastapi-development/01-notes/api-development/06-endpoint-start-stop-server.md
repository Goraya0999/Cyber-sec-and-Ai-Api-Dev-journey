# API Endpoint and Basic FastAPI Server Operations

## What is an API Endpoint?

An **API Endpoint** is a specific URL where a client can send requests to interact with a resource or service.

An endpoint acts as an entry point to an API.

### Examples

```text
/
```

```text
/users
```

```text
/products
```

```text
/orders/1
```

---

# What is a Simple Endpoint?

A simple endpoint is the most basic route in a FastAPI application that responds to client requests.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

### Endpoint Breakdown

| Component     | Purpose                                     |
| ------------- | ------------------------------------------- |
| @app.get("/") | Creates a GET endpoint                      |
| "/"           | Root URL path                               |
| home()        | Function executed when endpoint is accessed |
| return        | Sends response back to client               |

### Endpoint URL

```text
http://127.0.0.1:8000/
```

### Response

```json
{
  "message": "Hello FastAPI"
}
```

---

# Multiple Endpoints Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/users")
def users():
    return {"message": "Users Endpoint"}

@app.get("/products")
def products():
    return {"message": "Products Endpoint"}
```

## Available Endpoints

| Endpoint  | Purpose             |
| --------- | ------------------- |
| /         | Home Page           |
| /users    | User Information    |
| /products | Product Information |

---

# Starting the FastAPI Server

Move to the project directory:

```bash
cd fastapi-project
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the server:

```bash
uvicorn main:app --reload
```

### Command Breakdown

| Part     | Meaning                        |
| -------- | ------------------------------ |
| uvicorn  | ASGI server                    |
| main     | Python file name               |
| app      | FastAPI object                 |
| --reload | Auto-restart when code changes |

### Successful Output

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Accessing the Server

## Home Endpoint

```text
http://127.0.0.1:8000/
```

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

---

# Stopping the FastAPI Server

While the server is running in the terminal:

```bash
CTRL + C
```

### Terminal Output

```text
INFO: Shutting down
INFO: Application shutdown complete
```

The server is now stopped.

---

# Restarting the Server

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the server again:

```bash
uvicorn main:app --reload
```

---

# Checking Running FastAPI Processes

View running Uvicorn processes:

```bash
ps aux | grep uvicorn
```

---

# Force Stop a Running Server

Find the process ID:

```bash
ps aux | grep uvicorn
```

Kill the process:

```bash
kill PROCESS_ID
```

Example:

```bash
kill 12345
```

Force kill if necessary:

```bash
kill -9 12345
```

---

# Basic FastAPI Workflow

```text
Create Endpoint
      │
      ▼
Start Uvicorn Server
      │
      ▼
Open Browser
      │
      ▼
Send Request
      │
      ▼
Receive Response
      │
      ▼
Stop Server (CTRL + C)
```
