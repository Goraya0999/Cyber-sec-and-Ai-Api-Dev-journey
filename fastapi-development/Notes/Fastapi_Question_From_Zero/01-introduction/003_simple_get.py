# from fastapi import class Fastapi
from fastapi import FastAPI

#make instance 
app=FastAPI(
    
)
#---routing --- get(/)----|
# "get" is used to get from server 
# ("/") is root endpoint
@app.get("/")
# define a function that run after get request 
def home():
    return {
        "message":"hello world"  # it is json format
    }
    
    
    # run it using this command
    # uvicorn 003_simple_get:app -p 8080
    # open link : http//127.0.0.1:8080  in browser
    
    # simple method2:
    # uvicorn 003_simple_get:app --reload