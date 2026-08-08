from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime


from databasee.models import ShipmentStatus


class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int =None


class ShipmentRead(BaseShipment):
    status: ShipmentStatus
    estimated_delivery:datetime

class ShipmentCreate(BaseShipment):
    pass
    

class ShipmentUpdate(BaseModel):
    content: str | None = Field(default=None)
    weight: float | None = Field(default=None, le=25)
    destination: int | None = Field(default=None)
    status: ShipmentStatus | None = Field(default=None)
    estimated_delivery:datetime | None = Field(default=None)