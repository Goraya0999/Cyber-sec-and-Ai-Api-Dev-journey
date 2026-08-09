#010 How do you validate an email field in Pydantic?

# Pydantic provides EmailStr for built-in email validation
# It ensures:
# ✔ Proper email format
# ✔ Rejects invalid email strings

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """
    email:
        - Must be a valid email address
        - Automatically validated by Pydantic

    Note:
        Requires external dependency:
        pip install email-validator
    """
    email: EmailStr


# Example:
user = User(email="test@example.com")  # ✅ Valid
# user = User(email="invalid-email")   # ❌ Raises validation error


#-------------------------


#011 How do you validate a URL in Pydantic?

# Use HttpUrl for strict URL validation

from pydantic import HttpUrl


class Site(BaseModel):
    """
    url:
        - Must be a valid HTTP/HTTPS URL
        - Includes scheme, domain, etc.
    """
    url: HttpUrl


# Example:
site = Site(url="https://example.com")  # ✅ Valid
# site = Site(url="not-a-url")          # ❌ Validation error


#-------------------------


#012 What is model_dump() in Pydantic v2?

# model_dump() converts a Pydantic model into a standard Python dictionary
# (Replacement for .dict() in Pydantic v1)

class Item(BaseModel):
    name: str
    price: float


item = Item(name="Widget", price=5.0)

# Convert model to dictionary
data = item.model_dump()

print(data)
# Output:
# {'name': 'Widget', 'price': 5.0}


# Advanced usage:
# You can control output using parameters

filtered_data = item.model_dump(exclude={"price"})  # Exclude specific field

print(filtered_data)
# Output:
# {'name': 'Widget'}