from enum import Enum
from datetime import datetime


from sqlmodel import SQLModel, Field


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(SQLModel, table=True):  # type: ignore[call-arg]
    __tablename__ = "shipment"

    id: int  = Field(default=None, primary_key=True)
    content: str
    weight: float = Field(gt=0, le=25)
    destination: int
    status: ShipmentStatus = ShipmentStatus.placed
    estimated_delivery: datetime




