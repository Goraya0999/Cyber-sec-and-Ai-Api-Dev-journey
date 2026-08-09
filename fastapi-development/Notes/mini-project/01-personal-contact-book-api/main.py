from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contacts

app = FastAPI(
    title="Contact Book API",
    description="A simple personal contact management API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.router)

@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "docs": "/docs"}