from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from schema import Shipment, patched

app = FastAPI()


shipments = {
    12701: {"weight": 1.2, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.3, "content": "books", "status": "shipped"},
    12703: {"weight": 1.5, "content": "electronics", "status": "delivered"},
    12704: {"weight": 3.5, "content": "furniture", "status": "in transit"},
    12705: {"weight": 2.0, "content": "clothing", "status": "returned"},
    12706: {"weight": 4.0, "content": "appliances", "status": "processing"},
    12707: {"weight": 1.8, "content": "toys", "status": "placed"},
}


# -------------------------------
# Get Shipment
# -------------------------------
@app.get("/shipment")
def get_shipment(id: int):

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found."
        )

    return shipments[id]


# -------------------------------
# Create Shipment
# -------------------------------
@app.post("/shipment",status_code=status.HTTP_201_CREATED)
def create_shipment(item: Shipment):

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = item.model_dump()

    return {
        "message": "Shipment created successfully.",
        "id": new_id
    }


# -------------------------------
# Replace Shipment (PUT)
# -------------------------------
@app.put("/shipment")
def update_shipment(id: int, item: Shipment):

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found."
        )

    shipments[id] = item.model_dump()

    return shipments[id]


# -------------------------------
# Partially Update Shipment (PATCH)
# -------------------------------
@app.patch("/shipment")
def patch_shipment(id: int, item: patched):

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found."
        )

    # Existing shipment
    shipment = shipments[id]

    # Only the fields provided by the client
    updated_fields = item.model_dump(exclude_unset=True)

    # Merge with existing data
    shipment.update(updated_fields)

    shipments[id] = shipment

    return shipment


# -------------------------------
# Scalar Documentation
# -------------------------------
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )