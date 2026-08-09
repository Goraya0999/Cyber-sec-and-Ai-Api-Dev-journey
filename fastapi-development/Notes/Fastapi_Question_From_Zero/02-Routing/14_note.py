#041 How do you convert a query parameter to a Pydantic model?

# You can use Depends() to automatically convert query parameters
# into a Pydantic model for structured validation and cleaner code.

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class Filter(BaseModel):
    skip: int = 0
    limit: int = 10


@app.get("/items")
def get_items(filter: Filter = Depends()):
    """
    Behavior:
        - Query params are automatically mapped to the Filter model
        - Validation is handled by Pydantic

    Example:
        /items?skip=5&limit=20

    Output:
        {
            "skip": 5,
            "limit": 20
        }

    Notes:
        - Cleaner than manually parsing query params
        - Great for grouping related parameters
        - Automatically documented in Swagger UI
    """
    return filter


#-------------------------


#042 How do you return a streaming response?

# StreamingResponse allows sending data in chunks instead of all at once.
# Useful for large data, logs, or real-time streaming.

from fastapi.responses import StreamingResponse


def generate_data():
    """
    Generator function:
        - Yields data chunk by chunk
        - Keeps memory usage low
    """
    for i in range(5):
        yield f"chunk {i}\n"


@app.get("/stream")
def stream():
    """
    Behavior:
        - Sends response in parts (streaming)
        - Client receives data progressively

    Use Cases:
        ✔ Large file downloads
        ✔ Real-time logs
        ✔ Data streaming APIs

    media_type:
        - 'text/plain' for simple text stream
        - can also use 'application/json', etc.
    """
    return StreamingResponse(generate_data(), media_type="text/plain")
#-----------------------------------------------
#043 How do you return a file download?

# FileResponse is used to send files (PDF, images, etc.) as a downloadable response

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/download")
def download():
    """
    Behavior:
        - Sends a file to the client
        - Browser will download it instead of displaying (based on headers)

    filename:
        - Controls the name of the downloaded file

    Example:
        /download → downloads "report.pdf"

    Notes:
        - File must exist in the given path
        - Can be used for PDFs, images, CSVs, etc.
    """
    return FileResponse("report.pdf", filename="report.pdf")


#-------------------------


#044 What is the 422 Unprocessable Entity error?

# FastAPI automatically returns 422 when request validation fails

from fastapi import Body


@app.post("/users")
def create_user(age: int = Body(...)):
    """
    422 Error occurs when:
        - Wrong data type (e.g., string instead of int)
        - Missing required field
        - Fails validation rules (e.g., constraints)

    Example (Invalid Request):
        POST /users
        Body: { "age": "twenty" }  ❌

    Response:
        {
            "detail": [
                {
                    "loc": ["body", "age"],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer"
                }
            ]
        }

    Notes:
        - Handled automatically by FastAPI + Pydantic
        - Helps ensure data integrity and API reliability
    """
    return {"age": age}