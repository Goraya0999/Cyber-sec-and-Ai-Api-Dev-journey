# Import FastAPI class to create the web application
from fastapi import FastAPI

# Import asynccontextmanager to manage startup and shutdown lifecycle
from contextlib import asynccontextmanager


# Define a lifespan function that controls app startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):

    # -------------------- STARTUP PHASE --------------------
    # This code runs BEFORE the application starts serving requests
    # Use this section to initialize resources like database connections,
    # load ML models, cache data, etc.
    print("App starting")

    # yield splits startup and shutdown logic
    # Everything above yield = startup
    # Everything below yield = shutdown
    yield

    # -------------------- SHUTDOWN PHASE --------------------
    # This code runs WHEN the application is stopping
    # Use this section to close database connections,
    # release resources, stop background tasks, etc.
    print("App stopping")


# Create FastAPI application instance
# lifespan=lifespan tells FastAPI to use this function
# for handling startup and shutdown events
app = FastAPI(lifespan=lifespan)