#048 What are operation-level response headers in FastAPI?

# You can add custom headers to a specific response by using the Response object

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/custom-header")
def custom_header(response: Response):
    """
    response.headers:
        - Allows adding custom headers to the HTTP response

    Example Header:
        X-App-Version: 1.0

    Use Cases:
        ✔ API versioning
        ✔ Security headers
        ✔ Custom metadata

    Notes:
        - Headers are sent along with the response
        - Only affects this specific route (operation-level)
    """
    response.headers["X-App-Version"] = "1.0"
    response.headers["X-Custom-Message"] = "Hello-Client"

    return {"message": "Headers added"}


#-------------------------


#049 How do you read headers from the request?

# You can access request headers using the Request object

from fastapi import Request


@app.get("/headers")
def get_headers(request: Request):
    """
    request.headers:
        - Returns all incoming HTTP headers
        - Works like a dictionary-like object

    Example:
        /headers

    Output:
        {
            "host": "127.0.0.1:8000",
            "user-agent": "Mozilla/5.0",
            ...
        }

    Notes:
        - Header keys are case-insensitive
        - Useful for authentication, logging, debugging
    """
    return dict(request.headers)


#-------------------------


#050 How do you declare a header parameter directly in the function signature?

# FastAPI provides Header() to directly extract specific headers

from fastapi import Header


@app.get("/items")
def get_items(user_agent: str = Header(None)):
    """
    user_agent:
        - Automatically reads 'User-Agent' header

    Example Request:
        GET /items
        Header: User-Agent: Mozilla/5.0

    Output:
        {
            "agent": "Mozilla/5.0"
        }

    Notes:
        - Header names are converted automatically:
            user_agent → User-Agent
        - You can set default values if header is missing
    """
    return {"agent": user_agent}