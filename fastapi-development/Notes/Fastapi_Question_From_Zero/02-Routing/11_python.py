#031 How do you group multiple routers with a common prefix in one include?

# When you have multiple routers, you can include them in a loop
# and apply the same prefix (e.g., "/api/v1") to all of them.

from fastapi import FastAPI, APIRouter

app = FastAPI()

# creating sample routers
users_router = APIRouter()
items_router = APIRouter()
orders_router = APIRouter()


@users_router.get("/users")
def get_users():
    return {"users": []}


@items_router.get("/items")
def get_items():
    return {"items": []}


@orders_router.get("/orders")
def get_orders():
    return {"orders": []}


# applying same prefix to all routers
for router in [users_router, items_router, orders_router]:
    app.include_router(router, prefix="/api/v1")


# Now routes will be:
# /api/v1/users
# /api/v1/items
# /api/v1/orders


#-------------------------


#032 How do you serve static files with FastAPI?

# FastAPI allows serving static files (CSS, JS, images, etc.)
# using StaticFiles and mounting it to a path.

from fastapi.staticfiles import StaticFiles

# mounting static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

"""
Explanation:
    - "/static" → URL path where files will be accessible
    - "static" → folder name in your project directory
    - name="static" → internal reference name

Example:
    If file exists: static/style.css
    Access via:     http://localhost:8000/static/style.css

Notes:
    - Commonly used for frontend assets
    - Folder must exist, otherwise error occurs
"""


#033 How do you serve a single HTML file from FastAPI?

# FastAPI allows returning raw HTML content using HTMLResponse.
# This is useful when you want to directly send HTML without templates.

from fastapi.responses import HTMLResponse



@app.get("/", response_class=HTMLResponse)
def homepage():
    """
    This route returns a simple HTML page.

    Why response_class=HTMLResponse?
        - Tells FastAPI to treat response as HTML (not JSON)
        - Sets correct Content-Type: text/html

    Behavior:
        - Browser will render this as a webpage
        - Not shown as plain text like JSON responses
    """

    # returning raw HTML string
    return """
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Hello</h1>
            <p>This is a simple HTML response</p>
        </body>
    </html>
    """