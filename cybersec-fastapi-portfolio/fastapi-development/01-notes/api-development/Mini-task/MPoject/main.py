from fastapi import FastAPI, HTTPException, status,Depends
from scalar_fastapi import get_scalar_api_reference
from database import Database
from schema import ShipmentCreate, ShipmentRead, ShipmentUpdate,ShipmentStatus
from contextlib import asynccontextmanager
#from rich import print,panel 
from databasee.session import create_db_table
from databasee.session import Sessiondep
from databasee.models import Shipment
from datetime import datetime,timedelta
@asynccontextmanager
async def lifespan_handler(app:FastAPI):
    print("server started ...")
    create_db_table()
    yield
    print("...stopped!")

app = FastAPI(lifespan=lifespan_handler)
db=Database()

### Shipments datastore as dict
# shipments = {
#     12701: {"weight": 8.2, "content": "aluminum sheets", "status": "placed", "destination": 11002},
#     12702: {"weight": 14.7, "content": "steel rods", "status": "shipped", "destination": 11003},
#     12703: {"weight": 11.4, "content": "copper wires", "status": "delivered", "destination": 11002},
#     12704: {"weight": 17.8, "content": "iron plates", "status": "in transit", "destination": 11005},
#     12705: {"weight": 10.3, "content": "brass fittings", "status": "returned", "destination": 11008},
# }


###  a shipment by id
@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int,session:Session=Sessiondep):
    # Check for shipment with given id
    shipment=session.get(Shipment,id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipment


### Create a new shipment with content and weight
@app.post("/shipment", response_model=None)
def submit_shipment(shipment: ShipmentCreate,session:Sessiondep) -> dict[str, int]:
    new_shipment=Shipment(
        **shipment.model_dump(),
        status=ShipmentStatus.placed,
        estimated_delivery=datetime.now() + timedelta(days=3)
    )
    session.add(new_shipment)
    session.commit()
    session.refresh(new_shipment)
    # Return id for later use
    return {"id": new_shipment.id}


### Update fields of a shipment
@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, shipment_update: ShipmentUpdate,session:Sessiondep):
    # Update data with given fields
    update=shipment_update.model_dump(exclude_none=True)
    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided"
        )
    shipment=session.get(Shipment,id)
    shipment.sqlmodel_update(update)
    session.add(shipment)
    session.commit()
    session.refresh(shipment)
    return shipment


### Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int,session:Sessiondep) -> dict[str, str]:
    # Remove from datastore
    # db.delete(id)
    session.delete(
        session.get(Shipment,id)
    )
    session.commit()

    return {"detail": f"Shipment with id #{id} is deleted!"}


### Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
