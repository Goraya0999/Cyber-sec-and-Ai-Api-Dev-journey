#045 How do you suppress the default 422 validation error?

# You can override FastAPI's default RequestValidationError handler
# to customize or suppress the 422 response format.

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def custom_validation_handler(request: Request, exc: RequestValidationError):
    """
    Behavior:
        - Overrides default 422 error response
        - Allows custom structure or message

    Use Cases:
        ✔ Hide detailed validation errors
        ✔ Return simplified error messages
        ✔ Standardize API error format

    Example Custom Response:
        {
            "error": "Invalid request data"
        }
    """
    return JSONResponse(
        status_code=400,  # you can change from 422 → 400 if needed
        content={"error": "Invalid request data"}
    )


#-------------------------


#046 How do you define a route with multiple response status codes in docs?

# You can use 'responses' parameter in route decorator
# to document multiple possible HTTP responses in Swagger UI.

from fastapi import HTTPException


@app.get(
    "/items/{id}",
    responses={
        200: {"description": "OK"},
        404: {"description": "Not Found"},
        403: {"description": "Forbidden"}
    }
)
def get_item(id: int):
    """
    Behavior:
        - Adds multiple response codes in API documentation
        - Improves API clarity for clients

    Example:
        /items/1   → 200 OK
        /items/0   → 404 Not Found

    Notes:
        - 'responses' is only for documentation
        - Actual status codes must still be returned manually
    """

    if id == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"id": id}
#-----------------------------------------
#047 How do you get client IP address from a request?

# FastAPI provides the Request object to access client connection details

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/ip")
def get_ip(request: Request):
    """
    request.client.host:
        - Returns the IP address of the client making the request

    Example Output:
        {
            "ip": "127.0.0.1"
        }

    Notes:
        - In production (behind proxy/load balancer), IP may not be real client IP
        - In such cases, check headers like:
            ✔ X-Forwarded-For
            ✔ X-Real-IP
    """
    return {"ip": request.client.host}


#-------------------------


#048 How do you access request headers in FastAPI?

# You can access headers using the Request object

@app.get("/headers")
def get_headers(request: Request):
    """
    request.headers:
        - Returns all HTTP headers
        - Acts like a dictionary-like object

    Example:
        /headers

    Output:
        {
            "host": "127.0.0.1:8000",
            "user-agent": "Mozilla/5.0",
            ...
        }

    Notes:
        - Headers are case-insensitive
        - Useful for authentication, tracking, debugging
    """
    return dict(request.headers)