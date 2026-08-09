# How to define a path parameter in FastAPI

# A path parameter is defined by placing its name inside curly braces `{}` 
# in the route path. The same name must be used as a function argument 
# so FastAPI can automatically pass the value from the URL to the function.

@app.get("/home/{path_parameter}")
def parameter(path_parameter: str):
    """
    Handles requests to /home/{path_parameter}

    Args:
        path_parameter (str): Value extracted from the URL path.

    Returns:
        dict: A JSON response containing the received path parameter.
    """
    return {"path_parameter": path_parameter}

#----------------------------------------------------
#002 What type conversion does FastAPI perform on path parameters?

# FastAPI automatically converts path parameters (which are received as strings 
# from the URL) into the type you declare in the function signature.

# Supported types include: int, float, bool, str, UUID, etc.
# If the conversion fails (e.g., passing "abc" where an int is expected), 
# FastAPI automatically returns a 422 Unprocessable Entity error.

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Example:
        URL: /items/10  → item_id will be converted to integer 10
        URL: /items/abc → will raise 422 validation error
    """
    return {"item_id": item_id}
#-----------------------------------------------
#003 How do you define multiple path parameters in one route?

# You can define multiple path parameters by including each parameter 
# inside curly braces `{}` in the route path.
# Each parameter must also be declared as a function argument with the same name.

@app.get("/users/{user_id}/items/{item_id}")
def get_user_item(user_id: int, item_id: int):
    """
    Example:
        URL: /users/5/items/20
        user_id → 5 (converted to int)
        item_id → 20 (converted to int)

    Returns:
        dict: A JSON response containing both path parameters.
    """
    return {
        "user_id": user_id,
        "item_id": item_id
    }