#034 What does the lt, gt, le, ge parameters do in Query/Path?

# These parameters are used to apply numeric validation constraints
# on query or path parameters.

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
def get_items(
    price: int = Query(..., gt=0, lt=1000)
):
    """
    Constraints used:
        gt → greater than
        lt → less than
        ge → greater than or equal
        le → less than or equal

    In this example:
        price must be > 0 and < 1000

    Behavior:
        - If value doesn't satisfy condition → FastAPI returns 422
        - Validation happens automatically (no manual checks needed)

    Example:
        /items?price=500   ✔ valid
        /items?price=0     ❌ invalid (not > 0)
        /items?price=1500  ❌ invalid (not < 1000)
    """
    return {"price": price}


#-------------------------


#035 How do you get the full URL of the current request?

# FastAPI provides the Request object which contains full request info

from fastapi import Request


@app.get("/url")
def get_url(request: Request):
    """
    request.url gives full URL including:
        - scheme (http/https)
        - host (127.0.0.1:8000)
        - path
        - query parameters

    str(request.url) converts it to string
    """

    # example output:
    # http://127.0.0.1:8000/url?x=10
    return {"url": str(request.url)}
#-------------------------------------------------
#036 How do you add a route for favicon.ico?

# Browsers automatically request /favicon.ico when loading a site.
# If not handled, it may return 404 in logs.

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """
    This route serves the favicon file.

    include_in_schema=False:
        - hides this route from Swagger docs
        - since it's not part of actual API logic

    FileResponse:
        - sends a file directly as response
        - here it returns favicon.ico from static folder

    Notes:
        - Make sure file exists at: static/favicon.ico
        - Otherwise you'll get file not found error
    """

    return FileResponse("static/favicon.ico")