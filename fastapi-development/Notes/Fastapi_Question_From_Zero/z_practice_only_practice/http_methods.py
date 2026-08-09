from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Api"
)

# in-memory "database" for demo
fake_db: dict[int, dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@gmail.com"},
    2: {"id": 2, "name": "Ali", "email": "ali@gmail.com"},
}

# ------------- GET: Retrieve all items ------
@app.get("/users", tags=["Users"])
def get_all_users():
    return list(fake_db.values())

# ------ GET: Retrieve single item -------
@app.get("/users/{id}", tags=["Users"])
def get_user(id: int):
    if id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return fake_db[id]
#------Create new item ---------
class UserCreate(BaseModel):
    name:str
    email:str

@app.post("/users",status_code=201,tags=["Users"])
def user_create(user:UserCreate):
    new_id=max(fake_db.keys(),default=0) +1
    fake_db[new_id]={"id":new_id,**user.model_dump()}
    return fake_db[new_id]

#------Put full update -----
@app.put("/users/{id}",tags=["Users"],status_code=200)
def update_user(id: int,user: UserCreate):
    if id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail="User not Found"
        )
    fake_db[id]={"id":id,**user.model_dump()}    
    return fake_db[id]

# ─── PATCH: Partial update ─────────────────────────────────────────────────────
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

@app.patch("/users/{user_id}", tags=["Users"])
def partial_update_user(user_id: int, user: UserUpdate):
    """Partially update a user's data."""
    if user_id not in fake_db:
        return {"error": "User not found"}
    existing = fake_db[user_id]
    update_data = user.model_dump(exclude_unset=True)
    fake_db[user_id] = {**existing, **update_data}
    return fake_db[user_id]


# ─── DELETE: Remove item ───────────────────────────────────────────────────────
@app.delete("/users/{user_id}", status_code=204, tags=["Users"])
def delete_user(user_id: int):
    """Delete a user."""
    if user_id not in fake_db:
        return {"error": "User not found"}
    del fake_db[user_id]