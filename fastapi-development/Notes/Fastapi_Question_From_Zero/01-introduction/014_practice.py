from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="My API",
    description="response_model understanding testing",
    version="1.0.0"
)

# Fake database
fake_db = [
    {
        "id": 1,
        "name": "Ali",
        "password": "secret123",
        "email": "ali@gmail.com"
    },
    {
        "id": 2,
        "name": "Sajjad",
        "password": "secret123",
        "email": "saj@gmail.com"
    }
]

# Full model (used internally)
class User(BaseModel):
    name: str
    password: str
    email: str

# Response model (safe output)
class UserResponse(BaseModel):
    name: str
    email: str

# GET user by ID
@app.get("/user/{id}", response_model=UserResponse)
def get_user(id: int):
    """
    Retrieve a user by ID.

    - Filters sensitive fields using response_model
    - Returns only safe data (name, email)
    """
    for i in fake_db:
        if i["id"] == id:
            return i  # response_model will filter automatically

    raise HTTPException(status_code=404, detail="User not found")