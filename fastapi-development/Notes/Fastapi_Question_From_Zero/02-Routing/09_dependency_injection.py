# ==========================================================
# FASTAPI NOTES — #027 Router-Level Dependency Injection
# ==========================================================

from fastapi import FastAPI, APIRouter, Depends

app = FastAPI()


# ==========================================================
# Example Dependency
# ==========================================================
def get_db():
    """
    PURPOSE:
        Simulate a database session dependency.

    BEHAVIOR:
        - This function would normally create and yield a DB session
        - Automatically injected into routes that require it

    NOTE:
        In real-world apps, this is where you:
            - Open DB connection
            - Yield session
            - Close connection after request
    """
    db = "DB_SESSION"   # placeholder
    return db


# ==========================================================
# #027 Router-Level Dependency Injection
# ==========================================================
router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_db)]   # 👈 Applied to ALL routes in this router
)


@router.get("/")
def get_items():
    """
    PURPOSE:
        Retrieve all items.

    IMPORTANT:
        - get_db() is automatically executed
        - Even though it's not explicitly in function parameters

    WHY USE ROUTER-LEVEL DEPENDENCIES?
        - Avoid repeating dependencies in every route
        - Enforce global logic (auth, DB session, logging, etc.)
        - Keep code clean and DRY

    COMMON USE CASES:
        ✔ Database session injection
        ✔ Authentication / Authorization
        ✔ Request validation
        ✔ Logging / monitoring
    """
    return {"message": "All items fetched"}


@router.post("/")
def create_item():
    """
    Same dependency (get_db) is automatically applied here as well.
    """
    return {"message": "Item created"}


# Include router in main app
app.include_router(router)


# ==========================================================
# ADVANCED USAGE (Access Dependency Value)
# ==========================================================
router_with_access = APIRouter(prefix="/users", tags=["users"])


@router_with_access.get("/")
def get_users(db=Depends(get_db)):
    """
    IMPORTANT DISTINCTION:
        - Router-level dependencies → executed but NOT accessible directly
        - Function-level dependencies → accessible via parameters

    USE THIS WHEN:
        You need to actually USE the dependency (e.g., query DB)
    """
    return {"db": db}


app.include_router(router_with_access)


# ==========================================================
# SUMMARY (Quick Revision)
# ==========================================================
"""
Router-Level Dependency:
    router = APIRouter(dependencies=[Depends(dep)])

✔ Applied to ALL routes in router
✔ Good for global logic (auth, DB, logging)
❌ Cannot directly access return value inside route

Function-Level Dependency:
    def route(dep=Depends(dep)):
✔ Can access dependency value

PRO TIP:
Use BOTH together:
    - Router-level → enforcement
    - Function-level → usage
"""