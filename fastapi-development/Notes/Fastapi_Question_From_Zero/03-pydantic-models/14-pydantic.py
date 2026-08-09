#040 How do you forbid extra fields in a Pydantic model?

# Use ConfigDict(extra="forbid")
# to reject any fields that are not defined
# in the model.

from pydantic import BaseModel, ConfigDict


class StrictItem(BaseModel):
    """
    Fields:
        name → required string

    Rules:
        - Extra fields are not allowed
    """
    model_config = ConfigDict(extra="forbid")

    name: str


# Example (Valid)
item = StrictItem(name="Laptop")
print(item)

# Output:
# name='Laptop'


# Example (Invalid)
# StrictItem(name="Laptop", price=1000)
#
# ValidationError:
# Extra inputs are not permitted


# Professional Note:
# - extra="forbid" enforces a strict schema.
# - Any unexpected field causes ValidationError.
# - Useful for:
#     • Public APIs
#     • Security-sensitive applications
#     • Preventing accidental client mistakes
# - Helps ensure only expected data is accepted.


#-------------------------


#041 How do you define a model with a set field?

# Use Set[type] when you want a collection
# of unique values.

from typing import Set
from pydantic import BaseModel, Field


class Article(BaseModel):
    """
    Fields:
        tags → set of unique strings

    Notes:
        - Duplicate values are automatically removed
        - Sets are unordered collections
    """
    tags: Set[str] = Field(default_factory=set)


# Example
article = Article(
    tags={"python", "fastapi", "python", "api"}
)

print(article)

# Output:
# tags={'python', 'fastapi', 'api'}


print(len(article.tags))

# Output:
# 3


# Professional Note:
# - Set automatically removes duplicates.
# - Useful for:
#     • Tags
#     • Categories
#     • Permissions
#     • Unique identifiers
# - Prefer default_factory=set instead of set()
#   to avoid mutable default value issues.
# - During JSON serialization, sets are converted
#   into lists because JSON has no set type.


#-------------------------


#042 How do you use a Pydantic model as a query parameter (flat model)?

# Use Depends() with a Pydantic model.
# FastAPI reads each model field from
# the query string automatically.

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class ItemFilter(BaseModel):
    """
    Query Parameters:
        category → item category
        min_price → minimum price filter
        max_price → maximum price filter
    """
    category: str | None = None
    min_price: float | None = None
    max_price: float | None = None


@app.get("/items")
def get_items(filters: ItemFilter = Depends()):
    """
    Example Request:

    GET /items?
        category=electronics&
        min_price=100&
        max_price=1000

    FastAPI automatically creates:

    ItemFilter(
        category="electronics",
        min_price=100,
        max_price=1000
    )
    """
    return filters


# Example Response:
# {
#     "category": "electronics",
#     "min_price": 100.0,
#     "max_price": 1000.0
# }


# Professional Note:
# - Depends() allows FastAPI to populate
#   the Pydantic model from query parameters.
# - Each field becomes an individual query parameter.
# - Useful for:
#     • Filtering
#     • Searching
#     • Pagination
#     • Sorting
# - Keeps endpoint signatures clean when many
#   query parameters are required.
# - FastAPI still performs full validation on
#   all query values using the model rules.


#-------------------------