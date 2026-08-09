#033 How do you mount a sub-application in FastAPI?

You can mount a sub-application in FastAPI using the `app.mount()` method.  
This allows you to split large applications into smaller, modular apps.  
Each sub-app works independently with its own routes and logic.  
It is useful for versioning or separating features like `/api/v1`, `/admin`, etc.

**Example:**
```python
from fastapi import FastAPI

app = FastAPI()
sub_app = FastAPI()

@sub_app.get("/ping")
def ping():
    return {"message": "pong"}

app.mount("/sub", sub_app)

#035 What is the difference between FastAPI and APIRouter?

`FastAPI` is the main application instance used to run your API.  
`APIRouter` is used to organize and group related routes into separate modules.  
It helps in building large applications with clean and maintainable structure.  
Routers are included in the main app using `app.include_router()`.

**Example:**
```python
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/items")
def get_items():
    return ["item1", "item2"]

app.include_router(router, prefix="/api")