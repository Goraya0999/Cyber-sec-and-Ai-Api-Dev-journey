from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import time

# Initialize FastAPI application instance
app = FastAPI()


# Custom middleware for logging request details and measuring response time
class SimpleMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        """
        Intercepts every incoming HTTP request before it reaches the route handler.

        Args:
            request: Incoming HTTP request object
            call_next: Function to forward the request to the next handler (route)

        Returns:
            Response object after processing
        """

        # Record the start time to measure processing duration
        start_time = time.time()

        # Log incoming request method and URL (useful for debugging & monitoring)
        print(f"Incoming request: {request.method} {request.url}")

        # Forward the request to the actual route handler
        response = await call_next(request)

        # Calculate total time taken to process the request
        process_time = time.time() - start_time

        # Log response processing time
        print(f"Completed in {process_time:.4f} seconds")

        # Add custom header to response (useful for performance tracking)
        response.headers["X-Process-Time"] = str(process_time)

        # Return the final response back to the client
        return response


# Register the custom middleware with the FastAPI app
app.add_middleware(SimpleMiddleware)


# Root endpoint (basic test route)
@app.get("/")
async def home():
    """
    Health check endpoint to verify API is running.
    """
    return {"message": "hello world"}


# Endpoint to simulate a slow API response
@app.get("/slow")
async def slow_api():
    """
    Simulates a slow response to demonstrate middleware timing.
    NOTE: time.sleep() blocks the event loop (not recommended for async apps).
    """
    time.sleep(5)  # Blocking call (should use asyncio.sleep in production)
    return {"message": "Slow"}