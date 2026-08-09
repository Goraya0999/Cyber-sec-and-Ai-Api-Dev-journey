#007 How do you read the raw request body?

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/raw")
async def raw_body(request: Request):
    """
    Reads raw request body as bytes (no parsing).
    Useful when:
        - Working with webhooks
        - Verifying signatures (Stripe, GitHub, etc.)
        - Handling non-JSON payloads
    """

    body = await request.body()  # raw bytes

    return {
        "length": len(body),   # total size of request body
        "preview": body[:50]   # first 50 bytes (debugging purpose)
    }


# Professional Comment:
# Always use raw body when exact payload matters (e.g., security validation).
# Avoid decoding unless necessary to prevent data corruption issues.



#008 How do you read request JSON manually?

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/json")
async def read_json(request: Request):
    """
    Manually parses JSON from request.
    FastAPI does NOT validate schema here.
    """

    data = await request.json()  # converts JSON -> Python dict

    return {
        "received_data": data,
        "type": str(type(data))
    }


# Professional Comment:
# Prefer Pydantic models for validation and structure.
# Manual JSON parsing is useful when:
#   - Schema is dynamic
#   - You don’t know structure beforehand
#   - You’re building generic middleware/tools


#-------------------------------------
#009 How do you mix form data and files in one request?

from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


@app.post("/profile")
async def profile(
    username: str = Form(...),        # form field (text data)
    avatar: UploadFile = File(...)    # file upload
):
    """
    FastAPI allows mixing:
        ✔ Form data (text fields)
        ✔ File uploads (binary data)
    in the same request using multipart/form-data
    """

    return {
        "user": username,
        "filename": avatar.filename,
        "content_type": avatar.content_type
    }


# Example Request (multipart/form-data):
"""
username = "john_doe"
avatar = profile.png
"""


# Professional Comment:
# ✔ This pattern is widely used in real-world APIs (profile update, posts, etc.)
# ✔ Always validate file type (e.g., image/png, image/jpeg)
# ✔ Never trust filename directly — sanitize before saving
# ✔ For large files, avoid reading fully into memory; stream or save in chunks