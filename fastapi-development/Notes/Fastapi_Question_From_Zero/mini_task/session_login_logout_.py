from fastapi import FastAPI, Response, Cookie, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


class AuthService:

    def authenticate(self, username: str, password: str):
        # Simulating a database lookup
        return username == "goraya" and password == "123456"

    def create_session(self):
        return str(uuid.uuid4())

    def login(self, data: LoginRequest, response: Response):

        if not self.authenticate(data.username, data.password):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        session_id = self.create_session()

        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True,
            secure=False,      # True in production (HTTPS)
            samesite="Lax",
            max_age=3600
        )

        return {
            "message": "Login successful",
            "session_id": session_id
        }

    def logout(self, response: Response):

        response.delete_cookie(
            key="session_id"
        )

        return {
            "message": "Logout successful"
        }

    def get_current_user(self, session_id: str | None):

        if not session_id:
            raise HTTPException(
                status_code=401,
                detail="Please login first"
            )

        return {
            "username": "goraya",
            "session_id": session_id
        }


auth_service = AuthService()


@app.post("/login")
def login(data: LoginRequest, response: Response):
    return auth_service.login(data, response)


@app.post("/logout")
def logout(response: Response):
    return auth_service.logout(response)


@app.get("/profile")
def profile(
    session_id: str | None = Cookie(None)
):
    return auth_service.get_current_user(session_id)