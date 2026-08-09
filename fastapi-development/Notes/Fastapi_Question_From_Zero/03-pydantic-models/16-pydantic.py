#046 How do you define a discriminated union in Pydantic?

# A discriminated union allows Pydantic to choose
# the correct model based on the value of a specific field.
#
# Use Field(discriminator="field_name")
# together with Union[] and Literal values.

from typing import Literal, Union
from pydantic import BaseModel, Field


class Cat(BaseModel):
    """
    Cat model
    """
    type: Literal["cat"]
    meow: str


class Dog(BaseModel):
    """
    Dog model
    """
    type: Literal["dog"]
    bark: str


class Pet(BaseModel):
    """
    Fields:
        pet → can be either Cat or Dog

    Rules:
        - Pydantic checks the 'type' field
        - Automatically selects the correct model
    """
    pet: Union[Cat, Dog] = Field(
        ...,
        discriminator="type"
    )


# Example 1: Cat

cat_pet = Pet(
    pet={
        "type": "cat",
        "meow": "Meow Meow"
    }
)

print(cat_pet)

# Output:
# pet=Cat(type='cat', meow='Meow Meow')


# Example 2: Dog

dog_pet = Pet(
    pet={
        "type": "dog",
        "bark": "Woof Woof"
    }
)

print(dog_pet)

# Output:
# pet=Dog(type='dog', bark='Woof Woof')


# Example 3: Invalid Type

# Pet(
#     pet={
#         "type": "bird",
#         "sound": "tweet"
#     }
# )
#
# ValidationError:
# Input tag 'bird' does not match any expected tags


# Professional Note:
# - Discriminated unions provide efficient validation
#   for multiple possible model types.
# - The discriminator field ("type" here)
#   determines which model should be used.
# - Common use cases:
#     • Different payment methods
#     • Multiple event types
#     • API message formats
#     • Vehicle or animal hierarchies
# - More efficient and predictable than a regular
#   Union because Pydantic does not need to try
#   every model during validation.
# - FastAPI uses discriminated unions to generate
#   clearer OpenAPI/Swagger documentation.


#-------------------------
#047 How do you use Pydantic's SecretStr for sensitive data?

# SecretStr is used to store sensitive string values
# such as passwords, API keys, and tokens.
# The actual value is hidden when printed or serialized.

from pydantic import BaseModel, SecretStr


class Config(BaseModel):
    """
    Fields:
        password → sensitive string

    Notes:
        - Hidden in print output
        - Hidden in model representation
        - Can be accessed using get_secret_value()
    """
    password: SecretStr


# Example
config = Config(password="MySuperSecretPassword")

print(config)

# Output:
# password=SecretStr('**********')


print(config.password)

# Output:
# **********


# Read actual value
print(config.password.get_secret_value())

# Output:
# MySuperSecretPassword


# Professional Note:
# - SecretStr protects sensitive information
#   from accidental exposure in logs.
# - Useful for:
#     • Passwords
#     • API keys
#     • Access tokens
#     • Database credentials
# - The secret is still stored internally.
# - Use get_secret_value() only when the
#   real value is actually needed.
# - Pydantic also provides SecretBytes
#   for sensitive binary data.


#-------------------------


#048 How do you add a custom JSON encoder for a Pydantic model?

# Use model_config and json_encoders
# to customize how specific types are
# converted during JSON serialization.

from datetime import datetime
from pydantic import BaseModel, ConfigDict


class Event(BaseModel):
    """
    Fields:
        created → datetime value

    Notes:
        - Datetime is converted using a custom encoder
        - Encoder returns ISO 8601 formatted string
    """
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )

    created: datetime


# Example
event = Event(
    created=datetime(2025, 1, 1, 10, 30, 0)
)

print(event.model_dump())

# Output:
# {
#     'created': datetime.datetime(2025, 1, 1, 10, 30)
# }


print(event.model_dump_json())

# Output:
# {
#     "created":"2025-01-01T10:30:00"
# }


#  Note:
# - json_encoders lets you control how
#   custom types are serialized to JSON.
# - Common use cases:
#     • datetime formatting
#     • UUID formatting
#     • Decimal conversion
#     • Custom domain objects
# - The encoder is applied when generating
#   JSON output (e.g., model_dump_json()).
# - Helps ensure API responses match
#   required formatting standards.
# - In Pydantic v2, field serializers are
#   often preferred for more advanced cases,
#   but json_encoders remains useful for
#   model-wide serialization behavior.


#-------------------------
