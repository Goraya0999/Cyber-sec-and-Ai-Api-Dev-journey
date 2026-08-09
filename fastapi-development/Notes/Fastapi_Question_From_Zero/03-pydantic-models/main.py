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