# response_model in FastAPI (Intermediate Explanation)

`response_model` defines the exact structure of data your API will return using a Pydantic model.  
It not only validates the response but also removes any extra or sensitive fields.  
This is very useful when your internal data contains more information than you want to expose.  
It ensures consistency, security, and clean API responses.

**Intermediate Example:**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Full internal model (contains sensitive data)
class UserInDB(BaseModel):
    id: int
    username: str
    password: str   # sensitive
    email: str

# Response model (safe data only)
class UserOut(BaseModel):
    id: int
    username: str

@app.get("/user", response_model=UserOut)
def get_user():
    return {
        "id": 1,
        "username": "ali",
        "password": "secret123",
        "email": "ali@example.com"
    }


#032 What does status_code parameter do in a route decorator?

`status_code` in FastAPI defines the HTTP status code returned when a request is successful.  
By default, FastAPI returns `200 OK`, but you can change it based on the action.  
For example, `201 Created` is used when a new resource is successfully created.  
It helps make your API more meaningful and aligned with HTTP standards.

**Example:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items", status_code=201)
def create_item():
    return {"created": True}