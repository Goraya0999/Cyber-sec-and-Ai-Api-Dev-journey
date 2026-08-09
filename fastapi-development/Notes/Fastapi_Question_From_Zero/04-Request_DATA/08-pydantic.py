#021 How do you accept a raw dict as a body in FastAPI?

from typing import Dict, Any
from fastapi import Body, FastAPI

app = FastAPI()

@app.post("/data")
def receive_data(data: Dict[str, Any] = Body(...)):
    return data


# Professional Comment:
# Using Dict[str, Any] is useful when the structure is dynamic or unknown,
# but you lose validation and documentation benefits of Pydantic models.
# In real projects, prefer BaseModel unless flexibility is absolutely required.
#--------------------------------
#022 How do you read the content-type header from a request?

from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/check")
async def check(request: Request):
    return {"content_type": request.headers.get("content-type")}


# Professional Comment:
# Directly accessing headers via Request is powerful for low-level control.
# However, if you only need specific headers, using Header() dependency is cleaner
# and keeps your endpoint more declarative and easier to test.

#----------------------------------------------------------------
#023 How do you forward/proxy a request body to another service?

import httpx
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/proxy")
async def proxy(request: Request):
    # Read raw request body
    body = await request.body()

    # Forward request to another backend service
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "http://backend/",
            content=body,
            headers={"content-type": request.headers.get("content-type")}
        )

    return r.json()


# Professional Comment:
# This is a basic proxy implementation. In real-world scenarios:
# - Always forward important headers (Authorization, Content-Type, etc.)
# - Handle timeouts and retries (httpx has built-in timeout support)
# - Validate or sanitize incoming data before forwarding (security)
# - Stream large bodies instead of loading fully into memory
# - Consider using a proper API Gateway (NGINX, Kong) for heavy traffic