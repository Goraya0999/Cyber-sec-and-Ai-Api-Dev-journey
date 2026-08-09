#022 What is model_config in Pydantic v2?

# model_config replaces the old Config class from Pydantic v1
# It is used to configure model behavior globally

from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    """
    model_config:
        - Applies rules to entire model
        - Cleaner and more explicit than v1 Config class
    """
    model_config = ConfigDict(
        str_strip_whitespace=True   # Automatically trims whitespace from strings
    )

    name: str


# Example:
item = Item(name="   Laptop   ")
print(item.name)  # "Laptop" (whitespace removed)


#-------------------------


#023 How do you configure Pydantic to use attribute names instead of aliases for output?

# populate_by_name=True allows using field names even when alias is defined

from pydantic import Field


class Product(BaseModel):
    """
    item_name:
        - Has alias 'itemName'
        - Can accept both 'item_name' and 'itemName' in input
    """
    model_config = ConfigDict(populate_by_name=True)

    item_name: str = Field(..., alias="itemName")


# Example:
product = Product(item_name="Phone")   # ✅ Works
product2 = Product(itemName="Tablet") # ✅ Also works


#-------------------------


#024 How do you serialize a model to JSON string?

# Use model_dump_json() in Pydantic v2

class Order(BaseModel):
    name: str
    price: float


order = Order(name="Widget", price=5.0)

# Convert to JSON string
json_str = order.model_dump_json()

print(json_str)
# Output:
# '{"name":"Widget","price":5.0}'


# Professional Note:
# model_dump()  → Python dict
# model_dump_json() → JSON string