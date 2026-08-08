from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session
from typing import Annotated
from fastapi import Depends

engine=create_engine(
    url="sqlite:///sqlite.db",
    echo=True,
    connect_args={
        "check_same_thread":False
    }
)

from models import Shipment
def create_db_table():
    
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(bing=engine) as session:
        yield session



Sessiondep=Annotated[Session,Depends(get_session)]