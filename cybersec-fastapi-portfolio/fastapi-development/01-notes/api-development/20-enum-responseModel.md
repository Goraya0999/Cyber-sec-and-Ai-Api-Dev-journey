````md id="4txp8m"
# Enum and Response Models in FastAPI

# Enum

## What is an Enum?

An **Enum (Enumeration)** is a special Python class that defines a fixed set of constant values.

Instead of allowing any value, an Enum restricts a variable to predefined choices.

---

# Why Use Enum?

Enum helps to:

- Prevent invalid values.
- Improve code readability.
- Reduce typing mistakes.
- Make APIs more predictable.
- Validate user input automatically.

---

# Importing Enum

```python
from enum import Enum
```

---

# Basic Syntax

```python
from enum import Enum

class Status(Enum):
    PLACED = "placed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
```

---

# Syntax Breakdown

| Component | Description |
|-----------|-------------|
| `class` | Creates a new class. |
| `Status` | Enum class name. |
| `Enum` | Parent class that enables enumeration. |
| `PLACED` | Enum member name. |
| `"placed"` | Enum member value. |

---

# Using Enum in a Pydantic Model

```python
from enum import Enum
from pydantic import BaseModel

class Status(Enum):
    PLACED = "placed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

class Shipment(BaseModel):
    content: str
    status: Status
```

---

# Valid Request

```json
{
    "content": "Laptop",
    "status": "placed"
}
```

---

# Invalid Request

```json
{
    "content": "Laptop",
    "status": "sending"
}
```

Response:

```http
422 Unprocessable Entity
```

---

# Advantages of Enum

- Restricts values.
- Prevents invalid input.
- Improves validation.
- Easier to maintain.
- Better API documentation.

---

# Common Uses

- Order Status
- Shipment Status
- User Roles
- Payment Status
- Priority Levels
- Gender
- Account Status

---

# Understanding Response Models

## What is a Response Model?

A **Response Model** is a Pydantic model that defines the structure of data returned by a FastAPI endpoint.

It acts as a blueprint for the API response.

---

# Why Use Response Models?

Response models help to:

- Validate response data.
- Return only required fields.
- Hide sensitive information.
- Generate accurate API documentation.
- Ensure consistent API responses.

---

# Request Model vs Response Model

| Request Model | Response Model |
|--------------|----------------|
| Validates incoming data. | Validates outgoing data. |
| Used for client requests. | Used for server responses. |
| Defines request body. | Defines response body. |

---

# Importing BaseModel

```python
from pydantic import BaseModel
```

---

# Creating a Response Model

```python
from pydantic import BaseModel

class ShipmentResponse(BaseModel):
    content: str
    weight: float
    status: str
```

---

# Using `response_model`

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ShipmentResponse(BaseModel):
    content: str
    weight: float
    status: str

@app.get("/shipment", response_model=ShipmentResponse)
def get_shipment():
    return {
        "content": "Books",
        "weight": 10,
        "status": "placed"
    }
```

---

# Syntax Breakdown

| Component | Description |
|-----------|-------------|
| `response_model` | Specifies the model used to validate the response. |
| `ShipmentResponse` | Pydantic model describing the response structure. |

---

# Response Validation

FastAPI checks whether the returned data matches the response model.

If the returned data is invalid, FastAPI raises a validation error instead of sending incorrect data to the client.

---

# Example

Model:

```python
class ShipmentResponse(BaseModel):
    content: str
    weight: float
```

Returned Data:

```python
{
    "content": "Books",
    "weight": 15
}
```

Validation:

```text
Passed
```

---

Returned Data:

```python
{
    "weight": 15
}
```

Validation:

```text
Failed
```

Reason:

```text
Missing required field: content
```

---

# Response Filtering

If extra fields are returned, FastAPI removes fields that are not defined in the response model.

Example:

Returned Data:

```python
{
    "content": "Books",
    "weight": 10,
    "status": "placed",
    "secret_code": "ABC123"
}
```

Response Model:

```python
class ShipmentResponse(BaseModel):
    content: str
    weight: float
    status: str
```

Actual Response:

```json
{
    "content": "Books",
    "weight": 10,
    "status": "placed"
}
```

The `secret_code` field is automatically excluded.

---

# Using Different Models

Large applications often use separate models for requests and responses.

Example:

```python
class ShipmentCreate(BaseModel):
    content: str
    weight: float

class ShipmentResponse(BaseModel):
    id: int
    content: str
    weight: float
    status: str
```

---

# Response Validation Flow

```text
Endpoint
    │
    ▼
Return Data
    │
    ▼
Response Model
    │
    ▼
Validate Fields
    │
    ├── Valid
    │      │
    │      ▼
    │  Send Response
    │
    └── Invalid
           │
           ▼
    Validation Error
```

---

# Advantages of Response Models

- Automatic validation.
- Consistent API responses.
- Removes unwanted fields.
- Protects sensitive data.
- Better API documentation.
- Cleaner code.

---

# Best Practices

- Create separate models for requests and responses.
- Use Enums for fields with fixed values.
- Always specify `response_model` for API endpoints.
- Never expose sensitive fields in response models.
- Use meaningful model names.
- Validate all outgoing responses.

---


````
