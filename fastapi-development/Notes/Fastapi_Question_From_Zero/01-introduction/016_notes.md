#036 How do you add a global prefix to all routes?

You can add a global prefix using `root_path` in FastAPI or `prefix` in `APIRouter`.  
`root_path` is mainly used when your app is deployed under a subpath (e.g., behind a proxy).  
`APIRouter(prefix=...)` is the common way to group routes with a shared prefix.  
This helps in API versioning like `/api/v1`.

**Example:**
```python
from fastapi import FastAPI, APIRouter

app = FastAPI(root_path="/api/v1")  # deployment-level prefix

router = APIRouter(prefix="/api/v1")

@router.get("/users")
def get_users():
    return ["Ali", "Ahmed"]

app.include_router(router)



#037 How do you configure CORS in FastAPI?

CORS (Cross-Origin Resource Sharing) allows your API to accept requests from different domains.  
In FastAPI, it is configured using `CORSMiddleware`.  
You can control which origins, methods, and headers are allowed.  
This is essential for frontend-backend integration (e.g., React with FastAPI).

**Example:**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all domains
    allow_methods=["*"],   # allow all HTTP methods
    allow_headers=["*"],   # allow all headers
)


#038 What is app.include_router() used for?

`app.include_router()` is used to attach an `APIRouter` to the main FastAPI application.  
It allows you to organize routes into separate modules for better structure.  
You can also add a `prefix` and `tags` while including the router.  
This helps in building scalable and maintainable APIs.

**Example:**
```python
from fastapi import FastAPI, APIRouter

app = FastAPI()
items_router = APIRouter()

@items_router.get("/")
def get_items():
    return ["item1", "item2"]

app.include_router(items_router, prefix="/items", tags=["items"])