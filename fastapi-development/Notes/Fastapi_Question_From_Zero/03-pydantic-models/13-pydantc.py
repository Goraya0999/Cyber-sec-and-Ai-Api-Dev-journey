#037 How do you define a Pydantic model with a constrained string?

# Use constr() to apply validation rules
# such as minimum length, maximum length,
# and regex pattern matching.

from pydantic import BaseModel, constr


class User(BaseModel):
    """
    Fields:
        username → string with validation rules

    Rules:
        - Minimum length = 3
        - Maximum length = 20
        - Only letters, numbers, and underscores allowed
    """
    username: constr(
        min_length=3,
        max_length=20,
        pattern=r'^[a-zA-Z0-9_]+$'
    )


# Example (Valid)
user = User(username="ali_123")
print(user)

# Output:
# username='ali_123'


# Example (Invalid)
# User(username="a!")
#
# ValidationError:
# - Too short
# - Invalid characters


# Professional Note:
# - constr() creates a constrained string type.
# - Useful for validating:
#     • Usernames
#     • Password formats
#     • Product codes
#     • Registration numbers
# - Validation occurs automatically when
#   the model instance is created.
# - Helps enforce business rules at the model level.


#-------------------------


#038 How do you define a constrained integer with Pydantic?

# Use conint() to restrict integer values
# using minimum and maximum boundaries.

from pydantic import BaseModel, conint


class Product(BaseModel):
    """
    Fields:
        quantity → integer with range validation

    Rules:
        - Must be >= 0
        - Must be <= 999
    """
    quantity: conint(
        ge=0,
        le=999
    )


# Example (Valid)
product = Product(quantity=50)
print(product)

# Output:
# quantity=50


# Example (Invalid)
# Product(quantity=-5)
#
# ValidationError:
# Input should be greater than or equal to 0


# Example (Invalid)
# Product(quantity=1000)
#
# ValidationError:
# Input should be less than or equal to 999


# Professional Note:
# - conint() creates a constrained integer type.
# - Common constraints:
#     • ge = greater than or equal
#     • gt = greater than
#     • le = less than or equal
#     • lt = less than
# - Useful for:
#     • Age limits
#     • Stock quantities
#     • Ratings
#     • Numeric business rules
# - Prevents invalid values before application logic runs.


#-------------------------


#039 What happens when extra fields are sent that aren't in the model?

# By default, Pydantic ignores unknown fields.
# You can change this behavior using model_config.

from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    """
    Default behavior:
        Extra fields are ignored
    """
    name: str


user = User(
    name="Ali",
    age=22
)

print(user)

# Output:
# name='Ali'

print(user.model_dump())

# Output:
# {
#     'name': 'Ali'
# }


# Example: Reject extra fields

class StrictUser(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str


# StrictUser(name="Ali", age=22)
#
# ValidationError:
# Extra inputs are not permitted


# Example: Allow extra fields

class FlexibleUser(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str


user2 = FlexibleUser(
    name="Ali",
    age=22
)

print(user2)

# Output:
# name='Ali' age=22


# Professional Note:
# - extra="ignore" (default)
#     → Unknown fields are discarded.
#
# - extra="forbid"
#     → Unknown fields cause ValidationError.
#
# - extra="allow"
#     → Unknown fields are stored and preserved.
#
# - For production APIs, extra="forbid"
#   is often preferred because it catches
#   unexpected client input early.
#
# - This setting helps control how strict
#   your API validation should be.


#-------------------------