from pydantic import BaseModel, Field 
from random import randint
from enum import Enum
from typing import Optional

class Status(Enum):
    PLACED = "placed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    IN_TRANSIT = "in transit"
    DELIVERED = "delivered"
    RETURNED = "returned"


class Shipment(BaseModel):
    content: str = Field(max_length=50)
    weight: float = Field(..., ge=1, le=25)
    status: Status =Field(default=Status.PLACED)
    destination:int | None = Field(default=randint(1100,119999))


class patched(BaseModel):
    content: str | None = None
    weight: float | None = Field(None, ge=1, le=25)
    status: str | None = None