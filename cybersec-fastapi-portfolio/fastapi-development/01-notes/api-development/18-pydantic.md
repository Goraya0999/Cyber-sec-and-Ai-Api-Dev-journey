# Pydantic in FastAPI

## What is Pydantic?

**Pydantic** is a Python library used for **data validation**, **data parsing**, and **data serialization** based on Python type hints.

In FastAPI, Pydantic is used to define the **structure of request and response data**.

Instead of manually checking whether the data sent by a client is valid, Pydantic automatically validates it.

---

# Why Use Pydantic?

Pydantic exists to solve several common problems when handling data:

- Validate incoming data automatically.
- Convert data into the correct Python data types.
- Detect invalid or missing data.
- Reduce manual validation code.
- Generate API documentation automatically.
- Improve code readability and maintainability.

---

# Where is Pydantic Used?

Pydantic is commonly used in:

- FastAPI
- REST APIs
- Backend Development
- Data Validation
- Configuration Management
- JSON Parsing
- Machine Learning Projects

---

# How Pydantic Works

```text
Client Request
      │
      ▼
 JSON Data
      │
      ▼
Pydantic Model
      │
      ▼
Validate Data
      │
      ├── Valid
      │      │
      │      ▼
      │  Pass to FastAPI
      │
      └── Invalid
             │
             ▼
      Return 422 Error
```

---

# Installing Pydantic

Pydantic is automatically installed when FastAPI is installed.

To install it separately:

```bash
pip install pydantic
```

---

# Importing Pydantic

```python
from pydantic import BaseModel
```

---

# What is `BaseModel`?

`BaseModel` is the base class provided by Pydantic.

Every Pydantic model must inherit from `BaseModel`.

It provides:

- Data validation
- Type conversion
- JSON serialization
- Automatic documentation support

---

# Creating a Pydantic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

---

# Syntax Breakdown

| Component | Description |
|-----------|-------------|
| `class` | Creates a new class. |
| `User` | Name of the model. |
| `(BaseModel)` | Inherits validation features from Pydantic. |
| `name: str` | `name` must be a string. |
| `age: int` | `age` must be an integer. |
| `email: str` | `email` must be a string. |

---

# Using a Pydantic Model in FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user
```

---

# Request Body

```json
{
    "name": "Ali",
    "age": 22
}
```

---

# Response

```json
{
    "name": "Ali",
    "age": 22
}
```

---

# Automatic Data Validation

If the client sends invalid data:

```json
{
    "name": "Ali",
    "age": "Twenty"
}
```

FastAPI automatically returns:

```http
422 Unprocessable Entity
```

No manual validation code is required.

---

# Automatic Type Conversion

Pydantic attempts to convert compatible data types automatically.

Example Request:

```json
{
    "name": "Ali",
    "age": "22"
}
```

Pydantic converts:

```text
"22"
```

to

```text
22
```

because the model expects an integer.

---

# Required Fields

Every field without a default value is required.

Example:

```python
class User(BaseModel):
    name: str
    age: int
```

Both fields must be provided.

---

# Optional Fields

Optional fields have a default value.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int = 18
```

If `age` is omitted, it defaults to `18`.

---

# Supported Data Types

| Type | Description |
|------|-------------|
| `str` | String |
| `int` | Integer |
| `float` | Decimal number |
| `bool` | Boolean value |
| `list` | List of items |
| `dict` | Dictionary |
| `set` | Set of unique values |
| `tuple` | Immutable collection |

---

# Nested Models

Pydantic models can contain other Pydantic models.

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    address: Address
```

---

# Validation Process

```text
Client
   │
   ▼
JSON Request
   │
   ▼
Pydantic Model
   │
   ▼
Check Required Fields
   │
   ▼
Validate Data Types
   │
   ▼
Convert Compatible Types
   │
   ▼
FastAPI Endpoint
```

---

# Advantages of Pydantic

- Automatic data validation.
- Automatic type conversion.
- Less manual validation code.
- Cleaner and more readable code.
- Better error messages.
- Automatic API documentation.
- Easy integration with FastAPI.

---

# Limitations

- Requires learning model-based programming.
- Strict validation may reject incorrectly formatted data.
- Complex nested models can increase code complexity.

---

# Common Mistakes

- Forgetting to inherit from `BaseModel`.
- Using incorrect data types.
- Missing required fields.
- Confusing query parameters with request body models.
- Expecting automatic conversion for incompatible values.

---

# Best Practices

- Create a separate Pydantic model for each request body.
- Use meaningful model names.
- Keep models focused on a single purpose.
- Use proper Python type hints.
- Reuse models whenever possible.
- Validate all client input using Pydantic.

---

# Pydantic vs Regular Python Class

| Feature | Regular Class | Pydantic Model |
|----------|---------------|----------------|
| Data Validation | No | Yes |
| Type Checking | Manual | Automatic |
| JSON Support | Manual | Automatic |
| FastAPI Integration | No | Yes |
| API Documentation | No | Yes |

---

