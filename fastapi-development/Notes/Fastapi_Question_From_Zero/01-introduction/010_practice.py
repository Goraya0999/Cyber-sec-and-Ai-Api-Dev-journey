# Import FastAPI library
from fastapi import FastAPI, Response


# Create FastAPI application instance
app = FastAPI()


# GET endpoint
# This route is used to retrieve items
@app.get("/items")
def get_items():
    return {
        "message": "Items delivered"
    }


# POST endpoint
# This route is used to create a new item
@app.post("/items")
def create_items():
    return {
        "message": "Item created"
    }
    
    #----------------------------------------------#
# Returning None from a route handler
# FastAPI automatically converts None into JSON null
@app.get("/empty")
def empty_response():
    return None


# Returning an empty response with HTTP status code 204
# 204 means "No Content"
@app.get("/no_content")
def no_content():
    return Response(status_code=204)


# -------------------- Synchronous vs Asynchronous Route Handlers -------------------- #

# Synchronous route handler
# FastAPI executes this function in a standard blocking way.
# Best suited for CPU-bound tasks or simple operations.
@app.get("/sync")
def sync_handler():
    return {
        "message": "This is a synchronous route handler"
    }


# Asynchronous route handler
# The 'async' keyword allows FastAPI to handle multiple requests efficiently.
# Best suited for I/O-bound operations such as database queries,
# API calls, or file handling.
@app.get("/async")
async def async_handler():
    return {
        "message": "This is an asynchronous route handler"
    }