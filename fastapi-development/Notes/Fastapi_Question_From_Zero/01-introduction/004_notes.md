## 005 - What does --reload do in Uvicorn?

The `--reload` flag is used when running a FastAPI app with Uvicorn.  
It makes the server watch your project files for changes.  
When you update or save your code, the server restarts automatically.  
This means you do not need to stop and run the server again.  
It saves time and makes development easier.  
It is mainly used during development, not in production.  
This feature helps developers test changes quickly.  

---

## 006 - Where does FastAPI generate API documentation?

FastAPI automatically creates interactive API documentation.  
You can open it in your browser at `/docs` (Swagger UI).  
Another documentation is available at `/redoc` (ReDoc).  
These pages show all your API endpoints clearly.  
You can also test your API directly from the browser.  
This feature is built-in, so no extra setup is needed.  


## 007 - What is ASGI and why FastAPI uses it?

ASGI stands for Asynchronous Server Gateway Interface.  
It allows handling multiple requests at the same time.  
FastAPI uses ASGI to support async (non-blocking) operations.  
This makes FastAPI very fast and efficient.  
It can handle many users or connections together.  
WSGI is older and works in a synchronous way.  
WSGI processes one request at a time and can block.  
ASGI is better for modern web apps and APIs.  

---

## 008 - What Python version is required for FastAPI?

FastAPI requires Python version 3.8 or higher.  
It uses modern Python features like type hints.  
Older versions of Python do not support these features well.  
Using the latest Python version gives better performance.  
It also ensures compatibility with FastAPI updates.  



## 009 - What is FastAPI() class?

FastAPI() is the main class used to create a FastAPI application.  
It is used at the start of your code to initialize the app.  
We usually assign it to a variable like `app`.  
This `app` variable is used to define routes (APIs).  
When FastAPI() is called, it returns an application object.  
This object is an ASGI application.  
It is used by servers like Uvicorn to run your app.  
All API endpoints are added to this app object.  
It acts as the core of your FastAPI project.  



## 010 - What is the purpose of @app.get()?

`@app.get()` is a decorator used in FastAPI.  
It is used to create a route for GET requests.  
A GET request is used to get data from the server.  
It connects a URL path to a Python function.  
When a user visits that URL, the function runs.  
FastAPI uses it to handle incoming requests.  
For example, `@app.get("/")` means homepage route.  
It helps organize API endpoints clearly.  