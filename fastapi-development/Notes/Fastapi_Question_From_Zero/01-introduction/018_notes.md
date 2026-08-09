# 🚀 FastAPI Notes — Request Object & Exception Handling

## 🔹 #041 — Get Current Request Object

### 📖 What is Request Object?
The `Request` object represents the incoming HTTP request. It allows access to:
- URL
- Headers
- Client info

### ✅ Example
```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/info")
def info(request: Request):
    return {"url": str(request.url)}
```

### 💡 Use Cases
- Logging requests
- Getting client IP: `request.client.host`
- Access headers: `request.headers.get("user-agent")`

---

## 🔹 #042 — Global Exception Handler

### 📖 What is Exception Handling?
Custom global handlers let you control error responses.

### ✅ Example
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )
```

### 🧪 Usage
```python
@app.get("/test")
def test():
    raise ValueError("Invalid input")
```

### 📤 Response
```json
{
  "detail": "Invalid input"
}
```

---

## 🚀 Summary

| Concept | Description |
|--------|------------|
| Request Object | Access request data |
| Exception Handler | Customize errors |