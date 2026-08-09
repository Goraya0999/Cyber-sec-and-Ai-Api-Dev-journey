

## 012 - Can you define a FastAPI route handler as async?

Yes, you can define a FastAPI route handler using `async def`.  
This makes the function asynchronous.  
It allows FastAPI to handle multiple requests at the same time.  
Async functions are useful for I/O operations.  
Examples include database queries or API calls.  
FastAPI can wait for these operations without blocking others.  
This improves performance and speed.  
It is best for modern and scalable applications.  

### Example:

```python
@app.get("/items")
async def get_items():
    return []



---

## 013 - What HTTP methods can be used in FastAPI?

FastAPI supports different HTTP methods using decorators.  
These decorators are used to handle different types of requests.  
Each method is used for a specific purpose.  

- `@app.get()` → Get data from server  
- `@app.post()` → Send data to server  
- `@app.put()` → Update full data  
- `@app.patch()` → Update partial data  
- `@app.delete()` → Delete data  
- `@app.head()` → Get headers only  
- `@app.options()` → Show allowed methods  
- `@app.trace()` → Debug request  

These methods help build complete APIs.  