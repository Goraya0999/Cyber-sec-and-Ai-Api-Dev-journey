#016 Why does FastAPI convert hyphens in header names to underscores?

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/headers")
def read_header(x_token: str = Header(None)):
    """
    HTTP headers use hyphens:
        X-Token

    Python variables cannot contain hyphens:
        x-token ❌ (invalid)
        x_token ✅ (valid)

    FastAPI automatically converts:
        X-Token  →  x_token
    """

    return {"x_token": x_token}


# Professional Comment:
# ✔ This mapping is automatic and avoids syntax issues in Python
# ✔ You can still use alias if you want exact control over header names
# ✔ Important when working with custom headers like X-API-KEY, X-Request-ID



#017 How do you accept duplicate headers (list of header values)?

from typing import List
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items")
def get_items(x_token: List[str] = Header(None)):
    """
    Accepts multiple values for the same header.

    Example:
        X-Token: abc
        X-Token: def

    OR:
        X-Token: abc, def
    """

    return {
        "tokens": x_token
    }


# Example Request Headers:
"""
X-Token: token1
X-Token: token2
"""


# Professional Comment:
# ✔ Useful for APIs that support multiple auth tokens or scopes
# ✔ FastAPI automatically collects duplicate headers into a list
# ✔ Always validate each value (do not blindly trust multiple tokens)
# ✔ Be careful: some clients send comma-separated values instead of multiple headers

#--------------------------------------------
#018 How do you validate the Content-Type of an uploaded file?

from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    """
    Validates uploaded file type using content_type.
    """

    if file.content_type != "image/png":
        raise HTTPException(
            status_code=400,
            detail="Only PNG files are allowed"
        )

    return {"ok": True, "filename": file.filename}


# Professional Comment:
# ✔ content_type comes from client → NOT fully trustworthy
# ✔ Always combine with server-side validation (e.g., check file signature/magic bytes)
# ✔ Never rely only on file extension (.png, .jpg)
# ✔ For production:
#     - Validate MIME type
#     - Validate file size
#     - Scan for malicious content if needed
# ✔ Consider using libraries like python-magic for deeper validation