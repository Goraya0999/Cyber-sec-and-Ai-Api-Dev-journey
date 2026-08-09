from fastapi import FastAPI , APIRouter

app = FastAPI()
sub_app = FastAPI()
admin_router=APIRouter()
user_router=APIRouter()
@admin_router.get("/admin")
def admin():
    return {
        "Message":"Admin pannel is running."
    }
@user_router.get("/user")
def user():
    return {
        "Message":"User panel is running"
    }
@sub_app.get("/")
def sub_home():
    return {"message": "This is sub app"}

# Mount sub app
app.mount("/subapi", sub_app)
sub_app.include_router(admin_router,prefix="/hide")
app.include_router(user_router,prefix="/client")