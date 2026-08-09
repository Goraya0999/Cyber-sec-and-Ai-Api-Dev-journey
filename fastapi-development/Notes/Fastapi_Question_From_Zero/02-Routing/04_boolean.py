#011 How does FastAPI handle boolean query parameters?

# FastAPI automatically converts query parameters to boolean values.
# It supports multiple truthy and falsy representations (case-insensitive).

# ✔ True values:
#    "true", "1", "on", "yes"
#
# ✔ False values:
#    "false", "0", "off", "no"

from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items(active: bool = True):
    """
    Examples:
        /items?active=true   → active = True
        /items?active=1      → active = True
        /items?active=yes    → active = True

        /items?active=false  → active = False
        /items?active=0      → active = False
        /items?active=no     → active = False

        /items               → active = True (default value)

    Returns:
        dict: Boolean value after automatic conversion
    """
    return {"active": active}

#-----------------------------------------------
#012 What is the difference between path parameters and query parameters?

# Path Parameters:
# - Part of the URL path itself
# - Defined using `{}` in the route
# - ALWAYS required
# - Used to identify a specific resource

# Query Parameters:
# - Passed after `?` in the URL
# - Not part of the path
# - OPTIONAL by default (can be required if no default is given)
# - Used for filtering, searching, pagination, etc.

from fastapi import FastAPI

app = FastAPI()

# Example of PATH parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    URL: /items/10
    item_id → required
    """
    return {"item_id": item_id}


# Example of QUERY parameters
@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    """
    URL: /items?skip=5&limit=20

    skip  → optional (default=0)
    limit → optional (default=10)
    """
    return {
        "skip": skip,
        "limit": limit
    }


# Key Differences Summary:
# ✔ Path → required, part of URL, identifies resource
# ✔ Query → optional, after ?, used for filtering/pagination\
    
    #--------------------------------------------
    #013 How do you catch all paths with a wildcard path parameter?

# FastAPI allows capturing an entire path (including `/`) using the special
# `:path` converter. This is useful for file systems, nested routes, etc.

from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    """
    Example:
        /files/docs/readme.txt   → file_path = "docs/readme.txt"
        /files/a/b/c/image.png   → file_path = "a/b/c/image.png"

    Notes:
        - `:path` allows slashes `/` inside the parameter
        - Without `:path`, FastAPI would stop at the first `/`
        - Always keep this route LAST if you have overlapping routes,
        otherwise it may catch everything

    Returns:
        dict: Captured full path
    """
    return {"path": file_path}

#-------------------------------------------
#014 How do you add a description and alias to a query parameter?

# FastAPI allows you to enhance query parameters using Query()
# by adding metadata like alias and description.

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
def get_items(
    q: str = Query(
        None,
        alias="search-term",                  # external name in URL
        description="Search keyword"          # shown in Swagger docs
    )
):
    """
    Example:
        /items?search-term=fastapi

        q → "fastapi"

    Notes:
        - alias="search-term" → client uses this name in URL
        - description → visible in API documentation (Swagger UI)
    """
    return {"q": q}


#015 How do you define an enum path parameter?

# Enums restrict values to a predefined set.
# FastAPI automatically validates and documents them.

from enum import Enum

class Color(str, Enum):
    red = "red"
    green = "green"

@app.get("/colors/{color}")
def get_color(color: Color):
    """
    Example:
        /colors/red   → valid
        /colors/blue  → 422 error (invalid enum value)

    Notes:
        - Only "red" or "green" are allowed
        - Automatically appears as dropdown in Swagger UI
    """
    return {"color": color}