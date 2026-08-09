#007 How do you add validation to a path parameter using Path()?

# FastAPI provides the `Path()` function to add validation rules 
# (such as minimum/maximum values, descriptions, etc.) to path parameters.

from fastapi import Path

@app.get("/items/{item_id}")
def get_item(item_id: int = Path(..., ge=1, le=1000)):
    """
    Explanation:
        ...  → makes the parameter required
        ge=1 → value must be >= 1 (greater than or equal to 1)
        le=1000 → value must be <= 1000 (less than or equal to 1000)

    Example:
        /items/10   → valid
        /items/0    → 422 error (less than 1)
        /items/2000 → 422 error (greater than 1000)

    Returns:
        dict: Validated item ID.
    """
    return {"id": item_id}


#008 How do you add validation to a query parameter using Query()?

# FastAPI provides the `Query()` function to add validation rules 
# (such as length constraints, regex, defaults, etc.) to query parameters.

from fastapi import Query

@app.get("/search")
def search(q: str = Query(..., min_length=3, max_length=50)):
    """
    Explanation:
        ...           → makes the query parameter required
        min_length=3  → minimum length of 3 characters
        max_length=50 → maximum length of 50 characters

    Example:
        /search?q=api     → valid
        /search?q=ab      → 422 error (too short)
        /search          → 422 error (missing required parameter)

    Returns:
        dict: Validated query string.
    """
    return {"q": q}




#--------------------------------------
#009 What is the `...` (Ellipsis) used for in Path() and Query()?

# The `...` (Ellipsis) is used to indicate that a parameter is REQUIRED 
# and has NO default value.

# It tells FastAPI:
# ➜ "This value must be provided by the client"
# ➜ If missing → automatically return 422 Validation Error

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., ge=1),      # required path parameter
    q: str = Query(..., min_length=3)    # required query parameter
):
    """
    Example:
        /items/10?q=abc   → valid
        /items/10         → 422 error (missing 'q')
    
    Explanation:
        Path(...)  ≡ Path(default=...)
        Query(...) ≡ Query(default=...)
    """
    return {
        "item_id": item_id,
        "query": q
    }


# Key Notes:
# ✔ `...` = required field (no default)
# ✔ Same as explicitly writing: default=...
# ✔ If omitted → FastAPI returns 422 automatically


#-------------------------------------------------
#010 How do you accept a list of query parameters with the same name?

# FastAPI allows multiple query parameters with the same name by using a list type.
# When the same key appears multiple times in the URL, FastAPI collects all values into a list.

from typing import List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
def get_items(ids: List[int] = Query([])):
    """
    Example:
        /items?ids=1&ids=2&ids=3

        ids → [1, 2, 3]

    Notes:
        - Each 'ids' in the URL is captured and converted to int
        - Default is an empty list [] if no values are provided

    Returns:
        dict: List of IDs from query parameters
    """
    return {"ids": ids}


# Optional Improvement (Recommended):
# Use None instead of [] to avoid mutable default issues

from typing import Optional, List

@app.get("/items")
def get_items(ids: Optional[List[int]] = Query(None)):
    """
    Example:
        /items?ids=5&ids=10 → ids = [5, 10]
        /items              → ids = None
    """
    return {"ids": ids}