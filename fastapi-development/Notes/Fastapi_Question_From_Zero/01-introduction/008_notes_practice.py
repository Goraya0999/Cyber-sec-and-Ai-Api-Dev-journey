# Import required libraries
from fastapi import FastAPI
from pydantic import BaseModel


# Create FastAPI application instance
app = FastAPI(
    title="My API",
    version="1.0.0"
)


# Root endpoint
# This route is used to test whether the API is working properly
@app.get("/")
def root():
    return {
        "message": "Hello World"
    }


# Pydantic BaseModel is used for data validation in FastAPI
# This class defines the structure of user input data
class User(BaseModel):
    name: str
    age: int


# POST endpoint to create a new user
# FastAPI automatically validates incoming request data
@app.post("/users")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age
    }