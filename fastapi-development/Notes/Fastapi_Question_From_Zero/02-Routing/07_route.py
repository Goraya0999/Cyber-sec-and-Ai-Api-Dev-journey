#022 How do you add route-level dependencies in include_router?

# You can attach dependencies to ALL routes in a router using `dependencies`
# inside `include_router()`. These dependencies run before each request.

from fastapi import FastAPI, APIRouter, Depends, HTTPException

app = FastAPI()
router = APIRouter()

def verify_token():
    """
    Example dependency:
        - Could check headers, auth token, etc.
    """
    # Dummy check (replace with real logic)
    token = "secret"
    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/")
def get_items():
    return {"message": "All items"}

# Apply dependency to all routes in this router
app.include_router(
    router,
    prefix="/items",
    dependencies=[Depends(verify_token)]
)

"""
Result:
    Every request to /items/* will first run verify_token()
"""


#023 What is the order of route matching in FastAPI?

# FastAPI matches routes in the ORDER they are defined.
# More specific (fixed) routes should come BEFORE dynamic (path parameter) routes.

from fastapi import FastAPI

app = FastAPI()

# ✔ Correct order
@app.get("/items/search")
def search_items():
    return {"message": "search route"}

@app.get("/items/{item_id}")
def get_item(item_id: str):
    return {"item_id": item_id}


"""
Example:
    /items/search → handled by search_items()

# ❌ Wrong order (if reversed):
@app.get("/items/{item_id}")
@app.get("/items/search")

Then:
    /items/search → item_id = "search" (WRONG behavior)

Key Rule:
    ✔ Define fixed/static routes FIRST
    ✔ Define dynamic routes AFTER
"""
#--------------------------------------------------
#024 How do you create a redirect response in FastAPI?

# FastAPI provides RedirectResponse to redirect a client 
# from one URL to another.

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/old")
def old_route():
    """
    When a client accesses /old,
    they will be redirected to /new
    """
    return RedirectResponse(
        url="/new",
        status_code=301   # 301 = Permanent Redirect
    )


@app.get("/new")
def new_route():
    return {"message": "You have been redirected to the new route"}


# Common Status Codes:
# 301 → Permanent Redirect (SEO-friendly, cached by browsers)
# 302 → Temporary Redirect (default behavior in many cases)

# Example:
# /old → automatically redirects → /new