# ==========================================================
# FASTAPI NOTES — #028 & #029
# ==========================================================

from fastapi import FastAPI, Response
from datetime import date

app = FastAPI()


# ==========================================================
# #028 Return different status codes conditionally
# ==========================================================
@app.get("/items/{id}")
def get_item(id: int, response: Response):
    # here FastAPI gives us the Response object automatically
    # we can manually change status_code based on condition

    if id == 0:
        # just handling a simple edge case
        # instead of breaking the flow, we change the status code
        response.status_code = 404
        return {"error": "item not found"}  # still returning JSON

    # normal case
    return {"id": id}


# ==========================================================
# #029 Accept date as a path parameter
# ==========================================================
@app.get("/events/{event_date}")
def get_event(event_date: date):
    # FastAPI automatically converts string → date object
    # expected format: YYYY-MM-DD

    # if user sends wrong format, FastAPI itself throws 422 error
    # no need to manually validate here

    return {"event_date": event_date}

#----------------------------------------------
#030 What is a 'path operation function' in FastAPI?

# A path operation function is the function that is linked with a route
# using a decorator like @app.get(), @app.post(), etc.
# It is responsible for handling the request and returning the response.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    This function is a path operation function.

    Why?
        - It is attached to the path "/" using @app.get("/")
        - When a client sends a GET request to "/", this function runs

    Flow:
        Request → FastAPI matches route → this function executes → response returned

    Notes:
        - Function name can be anything
        - Return value is automatically converted to JSON
        - You can add parameters (path, query, body, etc.)
    """
    return {"message": "Hello from root"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Another path operation function example.

    This one:
        - Handles GET request on /items/{item_id}
        - Takes path parameter `item_id`
    """
    return {"item_id": item_id}