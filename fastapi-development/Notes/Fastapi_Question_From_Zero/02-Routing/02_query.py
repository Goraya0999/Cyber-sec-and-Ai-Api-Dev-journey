#004 How do you define a query parameter in FastAPI?

# Any function parameter that is NOT part of the path is automatically 
# treated as a query parameter by FastAPI.

# Query parameters are passed in the URL after `?` in key=value format.
# You can also provide default values to make them optional.

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    """
    Example:
        /items?skip=5&limit=20

        skip  → 5
        limit → 20

    Returns:
        dict: Pagination values from query parameters.
    """
    return {
        "skip": skip,
        "limit": limit
    }
#----------------------------------------------

#005 How do you make a query parameter required (no default)?

# To make a query parameter required, do NOT provide a default value.
# FastAPI will automatically validate the request and return a from typing import Optional
# 422 Unprocessable Entity error if the parameter is missing.

@app.get("/search")
def search(q: str):
    """
    Example:
        /search?q=fastapi  → valid
        /search            → 422 error (missing required parameter)

    Args:
        q (str): Required query parameter.

    Returns:
        dict: The search query.
    """
    return {
        "query": q
    }
    
#------------------------------------------
#006 How do you make a query parameter optional?

# A query parameter is optional when you provide a default value.
# The most explicit and recommended way is to use `Optional[type] = None`,
# which clearly indicates that the parameter can be either the given type or None.



@app.get("/items")
def get_items(q: Optional[str] = None):
    """
    Example:
        /items?q=hello → q = "hello"
        /items         → q = None (not provided)

    Args:
        q (Optional[str]): Optional query parameter.

    Returns:
        dict: The query value (or None if not provided).
    """
    return {"q": q}


# Alternative (less explicit but valid):
# FastAPI will still treat it as optional if a default value is provided.

@app.get("/items")
def get_items(q: str = None):
    """
    Note:
        This works, but using Optional[str] is preferred for clarity 
        and better type hinting.
    """
    return {"q": q}