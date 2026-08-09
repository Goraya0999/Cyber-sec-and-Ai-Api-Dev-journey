# How to Install FastAPI?

we can install FastAPI using pip (Python package manager).

## Step 1: Install FastAPI
```bash
pip install fastapi

# Install Server

pip install uvicorn

# Example code (main.py):
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"} 


```bash
uvicorn main:app --reload