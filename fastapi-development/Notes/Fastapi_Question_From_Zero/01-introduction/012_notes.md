# FastAPI Notes (#027 - #029)

## Q1. What is Starlette and how is it related to FastAPI?

Starlette is a lightweight ASGI (Asynchronous Server Gateway Interface) framework used for building high-performance async web applications. FastAPI is built on top of Starlette and uses it as its core foundation. Starlette provides essential features such as routing, middleware, request handling, and response management. FastAPI extends these features by adding data validation using Pydantic and automatic OpenAPI documentation generation. This combination makes FastAPI powerful, fast, and easy to use. Developers benefit from both Starlette’s performance and FastAPI’s developer-friendly features.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI uses Starlette under the hood"}
```

---

## Q2. Can FastAPI handle WebSocket connections?

Yes, FastAPI supports WebSocket connections, allowing real-time communication between client and server. WebSockets are useful for applications like chat apps, live notifications, and streaming data. FastAPI provides this functionality using the `@app.websocket()` decorator and the `WebSocket` class. Unlike regular HTTP requests, WebSockets keep the connection open for continuous data exchange. FastAPI makes it easy to accept, send, and receive messages asynchronously. This feature is important for building modern interactive applications.

**Example:**

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello WebSocket")
    await websocket.close()
```

---

## Q3. How do you include a startup or shutdown event handler in FastAPI?

FastAPI allows you to define event handlers that run when the application starts or shuts down. These are useful for tasks like connecting to databases, loading resources, or cleaning up before shutdown. You can use the `@app.on_event("startup")` and `@app.on_event("shutdown")` decorators for this purpose. These functions can be asynchronous and run automatically at the appropriate lifecycle stage. This helps manage application resources efficiently. It is a common practice in production applications.

**Example:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    print("App starting")

@app.on_event("shutdown")
async def shutdown():
    print("App stopping")
```
