# Pydantic Model Fields

## What are Model Fields?

A **Model Field** is a variable defined inside a **Pydantic model** that represents a piece of data.

Each field has:

- A name
- A data type
- An optional default value
- Optional validation rules

When FastAPI receives data from a client, Pydantic validates every model field before the data reaches your endpoint.

---

# Why Use Model Fields?

Model fields help to:

- Define the structure of input data.
- Validate client requests automatically.
- Enforce data types.
- Provide default values.
- Apply validation rules.
- Generate API documentation.

---

# Basic Syntax

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

---

# Syntax Breakdown

| Component | Description |
|-----------|-------------|
| `class` | Creates a model. |
| `User` | Model name. |
| `BaseModel` | Parent class that provides validation. |
| `name` | Field name. |
| `str` | Field data type. |
| `age` | Another field. |
| `int` | Integer data type. |

---

# Required Fields

A field without a default value is **required**.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Request:

```json
{
    "name": "Ali",
    "age": 22
}
```

---

# Optional Fields with Default Values

A field becomes optional if it has a default value.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int = 18
```

If `age` is not provided, it automatically becomes:

```text
18
```

---

# Using `None` as a Default Value

```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: Optional[str] = None
```

The `phone` field is optional.

---

# Common Field Data Types

| Type | Description |
|------|-------------|
| `str` | String |
| `int` | Integer |
| `float` | Decimal number |
| `bool` | Boolean |
| `list` | List |
| `dict` | Dictionary |
| `set` | Set |
| `tuple` | Tuple |
| `Optional[T]` | Optional field |

---

# Field Validation with `Field()`

Pydantic provides the `Field()` function to add validation rules and metadata.

Import it using:

```python
from pydantic import Field
```

---

# Basic Syntax

```python
field_name: data_type = Field(...)
```

---

# Required Field Using `Field`

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(...)
```

The `...` (Ellipsis) means the field is required.

---

# Default Value Using `Field`

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    age: int = Field(default=18)
```

---

# String Length Validation

## Minimum Length

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=3)
```

---

## Maximum Length

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(max_length=20)
```

---

## Minimum and Maximum Length

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=3, max_length=20)
```

---

# Numeric Validation

## Greater Than (`gt`)

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    price: float = Field(gt=0)
```

Value must be greater than `0`.

---

## Greater Than or Equal (`ge`)

```python
class Product(BaseModel):
    price: float = Field(ge=1)
```

---

## Less Than (`lt`)

```python
class Product(BaseModel):
    price: float = Field(lt=100)
```

---

## Less Than or Equal (`le`)

```python
class Product(BaseModel):
    price: float = Field(le=100)
```

---

## Range Validation

```python
class Product(BaseModel):
    price: float = Field(ge=1, le=100)
```

Allowed values:

```text
1 ≤ price ≤ 100
```

---

# Field Description

Descriptions appear in FastAPI documentation.

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(description="User's full name")
```

---

# Field Example

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(example="Ali")
```

---

# Complete Example

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=30
    )

    price: float = Field(
        ge=1,
        le=500
    )

    quantity: int = Field(
        ge=1
    )
```

---

# Validation Flow

```text
Client Request
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
Apply Field Rules
       │
       ▼
Accepted
```

---

# Common `Field()` Parameters

| Parameter | Description |
|-----------|-------------|
| `default` | Default value. |
| `...` | Required field. |
| `title` | Field title in documentation. |
| `description` | Field description. |
| `example` | Example value for documentation. |
| `min_length` | Minimum string length. |
| `max_length` | Maximum string length. |
| `gt` | Greater than. |
| `ge` | Greater than or equal. |
| `lt` | Less than. |
| `le` | Less than or equal. |

---

# Common Validation Errors

| Invalid Input | Reason |
|--------------|--------|
| `"age": "abc"` | Invalid integer. |
| `"name": ""` | May violate `min_length`. |
| `"price": -5` | Violates `gt` or `ge`. |
| Missing required field | Required field not provided. |

FastAPI returns:

```http
422 Unprocessable Entity
```

---

# Best Practices

- Always use proper type hints.
- Use `Field()` for validation rules.
- Keep field names meaningful.
- Use descriptions for better API documentation.
- Validate numeric ranges.
- Validate string lengths.
- Provide default values only when appropriate.
- Use `Optional` only when a field is truly optional.

---

