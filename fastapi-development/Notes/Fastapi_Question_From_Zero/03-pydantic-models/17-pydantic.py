#049 How do you define a model that must have at least one field set?

# Use @model_validator(mode="after")
# to perform validation after all fields
# have been processed.
#
# This is useful when at least one of several
# optional fields must contain a value.

from pydantic import BaseModel, model_validator


class ContactInfo(BaseModel):
    """
    Fields:
        email → optional
        phone → optional

    Rules:
        - At least one field must be provided
    """
    email: str | None = None
    phone: str | None = None

    @model_validator(mode="after")
    def validate_at_least_one_field(self):
        if self.email is None and self.phone is None:
            raise ValueError(
                "At least one of email or phone must be provided"
            )
        return self


# Example (Valid)

contact1 = ContactInfo(
    email="ali@example.com"
)

print(contact1)

# Output:
# email='ali@example.com' phone=None


# Example (Valid)

contact2 = ContactInfo(
    phone="+923001234567"
)

print(contact2)

# Output:
# email=None phone='+923001234567'


# Example (Invalid)

# ContactInfo()
#
# ValidationError:
# At least one of email or phone must be provided


# Professional Note:
# - model_validator() validates the entire model.
# - mode="after" runs after field validation.
# - Useful for:
#     • At least one field required
#     • Cross-field validation
#     • Business rule enforcement
#     • Complex validation logic
# - Replaces root_validator() from Pydantic v1.
# - Ideal when validation depends on multiple fields.


#-------------------------


#050 How do you use BaseSettings for configuration with env vars?

# BaseSettings automatically loads values
# from environment variables and .env files.
#
# It is commonly used for application
# configuration and secrets management.

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings.

    Environment Variables:
        DATABASE_URL
        SECRET_KEY
        DEBUG
    """
    database_url: str
    secret_key: str
    debug: bool = False


# Create settings object
settings = Settings()


# Example .env file

# DATABASE_URL=postgresql://user:pass@localhost/db
# SECRET_KEY=my_secret_key
# DEBUG=true


# Access values

print(settings.database_url)
print(settings.secret_key)
print(settings.debug)


# Professional Note:
# - BaseSettings automatically reads:
#     • Environment variables
#     • .env files
#     • System configuration values
# - Useful for:
#     • Database URLs
#     • API keys
#     • Secret keys
#     • Feature flags
# - Keeps sensitive data out of source code.
# - Supports different configurations for:
#     • Development
#     • Testing
#     • Production
# - Widely used in FastAPI applications for
#   centralized configuration management.


# Example Environment Variable Mapping:
#
# DATABASE_URL  -> settings.database_url
# SECRET_KEY    -> settings.secret_key
# DEBUG         -> settings.debug


#-------------------------