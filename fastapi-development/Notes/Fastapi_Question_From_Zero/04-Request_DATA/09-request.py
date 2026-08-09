# ============================================
# #024 How do you get query parameters as a dict?
# ============================================

from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/params")
def params(request: Request):
    # request.query_params returns a QueryParams object (immutable multi-dict)
    # converting it to dict gives a standard Python dictionary
    query_dict = dict(request.query_params)

    # NOTE:
    # - All values are returned as strings
    # - Example: /params?name=ali&age=20
    #   Output: {"name": "ali", "age": "20"}

    return query_dict


# ============================================
# #025 How do you send multipart/form-data from a test client?
# ============================================

from fastapi import UploadFile, File
from fastapi.testclient import TestClient

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    # UploadFile provides:
    # - file.filename  -> name of uploaded file
    # - file.file      -> actual file object (SpooledTemporaryFile)
    return {"filename": file.filename}


# Create a test client instance (simulates HTTP requests)
client = TestClient(app)

# Sending multipart/form-data request
response = client.post(
    "/upload",

    # files parameter is REQUIRED for multipart/form-data
    files={
        # Format: "field_name": ("filename", file_bytes, "content_type")
        "file": ("test.txt", b"hello", "text/plain")
    }
)

# Response will contain server output
print(response.json())


# ============================================
# PROFESSIONAL NOTES (INLINE STYLE)
# ============================================

# - Query parameters are always strings → manual type conversion required if needed
# - For multiple values (e.g., ?tag=a&tag=b), use:
#       request.query_params.getlist("tag")
#
# - In production APIs, prefer FastAPI automatic parsing:
#       def params(name: str, age: int)
#   → provides validation + type conversion
#
# - multipart/form-data is mandatory for file uploads (JSON cannot handle files)
#
# - Common mistake:
#       Using json={} instead of files={} → will NOT send file correctly
#
# - You can send both files and form data together:
#       client.post(..., files=..., data={"key": "value"})
#
# - TestClient is built on Starlette + requests → used for unit testing APIs
#
# - For large files in production:
#       Avoid loading entire file into memory → use streaming approach
#
# ============================================

# ============================================
# #026 How do you read path parameters within request middleware?
# ============================================

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # IMPORTANT:
        # Path parameters are NOT directly available in middleware
        # because routing has not been resolved yet at this stage

        # You only have access to raw URL path
        raw_path = request.url.path

        # Example:
        # If route is: /users/{user_id}
        # Request:     /users/123
        # raw_path → "/users/123"

        print(f"Incoming path: {raw_path}")

        # --------------------------------------------
        # Manual Parsing (if absolutely needed)
        # --------------------------------------------

        # Example manual extraction (NOT recommended for complex routes)
        parts = raw_path.strip("/").split("/")

        # Example logic:
        # /users/123 → ["users", "123"]
        user_id = None
        if len(parts) == 2 and parts[0] == "users":
            user_id = parts[1]
            print(f"Extracted user_id (manual): {user_id}")

        # --------------------------------------------
        # Continue request processing
        # --------------------------------------------
        response = await call_next(request)

        return response


# Add middleware to app
app.add_middleware(LoggingMiddleware)


# ============================================
# PROPER WAY (AFTER ROUTING - DEPENDENCY)
# ============================================

from fastapi import Depends


def log_path_params(request: Request):
    # After routing is resolved, path_params become available
    # This is the CORRECT way to access them
    path_params = request.path_params

    print(f"Path params (correct way): {path_params}")


@app.get("/users/{user_id}")
async def get_user(user_id: int, dep=Depends(log_path_params)):
    # user_id is automatically parsed and validated by FastAPI
    return {"user_id": user_id}


# ============================================
# PROFESSIONAL NOTES (INLINE STYLE)
# ============================================

# - Middleware runs BEFORE routing → no access to path_params
# - request.url.path gives raw string path only
#
# - Manual parsing is fragile:
#     - Breaks with nested routes
#     - Hard to maintain
#
# - Best practice:
#     - Use Dependencies (Depends) for accessing path_params
#     - Or use custom APIRoute class for advanced control
#
# - Middleware is best for:
#     - Logging
#     - Authentication (token-level, not route-level)
#     - Metrics / monitoring
#
# - If you MUST access route-level data in middleware:
#     - Use request.scope["path"] or request.scope["route"] (advanced)
#     - But note: route may not be resolved yet depending on middleware order
#
# ============================================
# ============================================
# #027 How do you handle a request with no Content-Type header?
# ============================================

from fastapi import FastAPI, Request, Body, HTTPException

app = FastAPI()


@app.get("/no-body")
def no_body_endpoint(name: str, age: int):
    # Query parameters DO NOT require Content-Type header
    # Example request:
    #   GET /no-body?name=ali&age=20
    # This works perfectly without any Content-Type
    return {"name": name, "age": age}


@app.post("/expect-body")
async def expect_body(request: Request):
    # When request contains body but NO Content-Type header:
    # FastAPI cannot determine how to parse it (JSON, form, etc.)

    try:
        data = await request.json()  # This expects "application/json"
    except Exception:
        # If Content-Type is missing or invalid → parsing fails
        raise HTTPException(
            status_code=400,
            detail="Missing or invalid Content-Type header"
        )

    return {"received": data}


@app.post("/auto-validate")
def auto_validate(data: dict = Body(...)):
    # FastAPI automatically validates request body based on Content-Type
    # If Content-Type is missing:
    # → FastAPI returns 422 Unprocessable Entity

    return data


# ============================================
# PROFESSIONAL NOTES (INLINE STYLE)
# ============================================

# - Content-Type header tells server how to parse request body
#     application/json
#     multipart/form-data
#     application/x-www-form-urlencoded
#
# - If NO Content-Type:
#     - Query/path params → work fine
#     - Body parsing → FAILS (422 or parsing error)
#
# - FastAPI relies on Content-Type for automatic validation
#
# - Best practice:
#     - Always send correct Content-Type from client
#
# - Manual handling (advanced):
#     - Use request.body() to read raw bytes if needed
#     - Then parse manually
#
# - Security:
#     - Reject requests with missing/invalid Content-Type if body is required
#
# ============================================



# ============================================
# #028 How do you validate that a request body is not empty?
# ============================================

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    # Field(...):
    # - "..." means REQUIRED field (cannot be missing)

    name: str = Field(
        ...,              # required field
        min_length=1      # ensures NOT empty string ""
    )

    price: float = Field(
        ...,              # required field
        gt=0              # ensures value > 0 (not zero or negative)
    )


@app.post("/items")
def create_item(item: ItemCreate):
    # FastAPI automatically:
    # - Validates request body
    # - Returns 422 if:
    #     - Body is missing
    #     - Field is missing
    #     - name == "" (empty string)
    #     - price <= 0

    return {"item": item}


# ============================================
# PROFESSIONAL NOTES (INLINE STYLE)
# ============================================

# - Empty body → FastAPI returns 422 automatically
#
# - Field(...):
#     - Makes field required
#
# - min_length=1:
#     - Prevents empty string ""
#
# - gt=0:
#     - Prevents zero or negative values
#
# - Additional validations:
#
#     from pydantic import validator
#
#     @validator("name")
#     def no_whitespace(cls, v):
#         if not v.strip():
#             raise ValueError("Name cannot be empty or whitespace")
#         return v
#
# - For optional fields:
#     name: Optional[str] = None
#
# - Best practice:
#     - Always validate input using Pydantic models
#     - Avoid manual validation unless necessary
#
# ============================================