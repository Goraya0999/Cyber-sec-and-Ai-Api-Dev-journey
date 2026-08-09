# FastAPI Notes

---

## 014 - What happens when a route returns a Python dict?

When a FastAPI route returns a Python dictionary,  
FastAPI automatically converts it into JSON format.  
JSON is the standard format used in APIs.  
It also sets the correct response type.  
The Content-Type becomes `application/json`.  
This makes the response easy to use in browsers or apps.  
You do not need to manually convert the data.  
FastAPI handles everything automatically.  

---

## 015 - How to run app on custom host and port?

You can run your FastAPI app with a custom host and port.  
This is done using the uvicorn command.  
It allows you to control where the app runs.  

### Example:
```bash
uvicorn main:app --host 0.0.0.0 --port 9000