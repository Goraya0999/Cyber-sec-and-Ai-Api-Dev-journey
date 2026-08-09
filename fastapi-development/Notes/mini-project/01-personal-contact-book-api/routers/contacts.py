from fastapi import APIRouter, HTTPException, Query, Path, status
from typing import List, Optional
from models import ContactCreate, ContactUpdate, ContactResponse
import database

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.get("/", response_model=List[ContactResponse])
def list_contacts(
    skip:   int           = Query(0, ge=0),
    limit:  int           = Query(10, le=100),
    search: Optional[str] = Query(None, min_length=1)
):
    return database.get_all(search=search, skip=skip, limit=limit)


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int = Path(..., ge=1)):
    contact = database.get_by_id(contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail=f"Contact #{contact_id} not found")
    return contact


@router.post("/", response_model=ContactResponse, status_code=201)
def create_contact(data: ContactCreate):
    return database.create(data.model_dump())


@router.patch("/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, data: ContactUpdate):
    updated = database.update(contact_id, data.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail=f"Contact #{contact_id} not found")
    return updated


@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: int = Path(..., ge=1)):
    if not database.delete(contact_id):
        raise HTTPException(status_code=404, detail=f"Contact #{contact_id} not found")