#019 How do you limit the size of an uploaded file?

from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """
    Limits file size by reading content and checking length.
    """

    content = await file.read()  # reads entire file into memory

    if len(content) > 1_000_000:  # 1MB limit
        raise HTTPException(
            status_code=413,
            detail="File too large"
        )

    return {
        "size": len(content),
        "filename": file.filename
    }


# Professional Comment:
# ✔ Simple approach but NOT efficient for large files (loads into memory)
# ✔ For production:
#     - Read in chunks (streaming) instead of full read
#     - Enforce limits at reverse proxy (NGINX, etc.)
# ✔ Always combine with:
#     - Content-Type validation
#     - File extension checks
# ✔ 413 = standard HTTP status for "Payload Too Large"
#-----------------------------------
#020 How do you receive a list of JSON objects as a request body?

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/bulk")
def bulk_create(items: List[Item]):
    """
    Receives a list (array) of JSON objects.
    FastAPI automatically:
        ✔ Parses list
        ✔ Validates each object using Item model
    """

    return {
        "count": len(items),
        "items": items
    }


# Example Request JSON:
"""
[
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25}
]
"""


# Professional Comment:
# ✔ Each item is validated individually (very powerful feature)
# ✔ If one item is invalid → entire request fails (atomic behavior)
# ✔ Useful for bulk operations (insert/update)
# ✔ For very large lists:
#     - Consider pagination or chunked processing
#     - Avoid huge payloads to prevent performance issues