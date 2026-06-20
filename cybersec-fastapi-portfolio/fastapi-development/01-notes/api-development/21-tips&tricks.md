# Pydantic Data Validation, `model_dump()`, and `exclude_none`

## Why Does FastAPI Use Pydantic?

FastAPI uses **Pydantic** to validate, parse, and serialize data.

Instead of manually checking every value received from a client, FastAPI relies on Pydantic models to ensure the data follows the expected structure and data types.

This reduces errors, improves security, and makes API development easier.

---

# Data Validation

## What is Data Validation?

**Data validation** is the process of checking whether incoming or outgoing data satisfies predefined rules.

These rules may include:

- Correct data type
- Required fields
- Value ranges
- String length
- Allowed values

If validation fails, FastAPI automatically returns an error.

---

# Data Conversion (Type Conversion)

## What is Data Conversion?

Pydantic automatically converts compatible data into the expected Python type.

Example:

Client Request:

```json
{
    "weight": "15"
}
```

Pydantic Model:

```python
weight: float
```

Converted Value:

```python
15.0
```

If conversion is impossible, FastAPI returns:

```http
422 Unprocessable Entity
```

---

# Response Validation

By default, FastAPI also validates the data returned by an endpoint.

If the returned data does not match the response model, FastAPI raises a validation error.

This ensures clients always receive correctly structured data.

---

# Disabling Response Validation

Sometimes you may not want FastAPI to validate the response.

This is useful when:

- Returning dynamic data.
- Returning data from external libraries.
- Improving performance.
- Validation is unnecessary.

Simply do not specify the `response_model` parameter.

Example:

```python
@app.get("/shipment")
def get_shipment():
    return shipment
```

No response validation is performed.

---

# Partial Updates

## Why Are Partial Updates Needed?

When updating an object, the client may only want to modify a few fields instead of sending the entire object.

Example:

Original Shipment:

```text
Content : Laptop
Weight  : 10
Status  : Placed
```

Client wants to update only:

```text
Status : Delivered
```

Sending the complete object is unnecessary.

---

# Optional Fields

Partial updates are implemented by making fields optional.

Example:

```python
from typing import Optional
from pydantic import BaseModel

class ShipmentUpdate(BaseModel):
    content: Optional[str] = None
    weight: Optional[float] = None
    status: Optional[str] = None
```

Every field can now be omitted.

---

# What is `model_dump()`?

`model_dump()` is a Pydantic method that converts a model object into a standard Python dictionary.

It is the replacement for the older `.dict()` method in Pydantic v2.

---

# Why Use `model_dump()`?

`model_dump()` is commonly used to:

- Convert models into dictionaries.
- Save data to databases.
- Return JSON responses.
- Update existing objects.
- Serialize model data.

---

# Syntax

```python
model.model_dump()
```

---

# Example

```python
from pydantic import BaseModel

class Shipment(BaseModel):
    content: str
    weight: float

shipment = Shipment(
    content="Books",
    weight=12
)

print(shipment.model_dump())
```

Output:

```python
{
    "content": "Books",
    "weight": 12.0
}
```

---

# What is `exclude_none`?

`exclude_none` is an option of `model_dump()`.

When set to `True`, fields whose value is `None` are excluded from the resulting dictionary.

---

# Why Use `exclude_none`?

It helps:

- Ignore fields that were not provided.
- Prevent overwriting existing values with `None`.
- Perform partial updates safely.
- Produce cleaner dictionaries.

---

# Syntax

```python
model.model_dump(exclude_none=True)
```

---

# Example Without `exclude_none`

```python
from typing import Optional
from pydantic import BaseModel

class ShipmentUpdate(BaseModel):
    content: Optional[str] = None
    weight: Optional[float] = None
    status: Optional[str] = None

shipment = ShipmentUpdate(
    status="Delivered"
)

print(shipment.model_dump())
```

Output:

```python
{
    "content": None,
    "weight": None,
    "status": "Delivered"
}
```

---

# Example With `exclude_none=True`

```python
print(shipment.model_dump(exclude_none=True))
```

Output:

```python
{
    "status": "Delivered"
}
```

Only fields with actual values are included.

---

# Updating Existing Data

Existing Shipment:

```python
shipment = {
    "content": "Laptop",
    "weight": 10,
    "status": "Placed"
}
```

Update Request:

```python
update = ShipmentUpdate(
    status="Delivered"
)
```

Convert to Dictionary:

```python
update_data = update.model_dump(exclude_none=True)
```

Result:

```python
{
    "status": "Delivered"
}
```

Update Dictionary:

```python
shipment.update(update_data)
```

Final Shipment:

```python
{
    "content": "Laptop",
    "weight": 10,
    "status": "Delivered"
}
```

Only the `status` field is updated.

---

# Update Flow

```text
Client Request
       │
       ▼
Pydantic Update Model
       │
       ▼
model_dump(exclude_none=True)
       │
       ▼
Dictionary
       │
       ▼
Update Existing Object
       │
       ▼
Return Updated Data
```

---

# `model_dump()` vs `model_dump(exclude_none=True)`

| Method | Output |
|---------|--------|
| `model_dump()` | Includes all fields, even if they are `None`. |
| `model_dump(exclude_none=True)` | Excludes fields whose value is `None`. |

---

# Common Parameters of `model_dump()`

| Parameter | Description |
|-----------|-------------|
| `exclude_none=True` | Removes fields with `None` values. |
| `exclude_defaults=True` | Removes fields that have default values. |
| `exclude_unset=True` | Removes fields that were not explicitly provided by the client. |
| `include={}` | Includes only specified fields. |
| `exclude={}` | Excludes specified fields. |

---

# Advantages

- Automatic data validation.
- Automatic type conversion.
- Easy conversion to dictionaries.
- Safe partial updates.
- Cleaner output.
- Less manual code.

---

# Best Practices

- Use separate models for create, update, and response operations.
- Use optional fields for PATCH requests.
- Use `model_dump(exclude_none=True)` for partial updates.
- Validate all client data with Pydantic.
- Avoid modifying dictionaries manually when a Pydantic model can be used.

---

