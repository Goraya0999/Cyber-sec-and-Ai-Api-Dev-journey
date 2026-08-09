from pydantic import (
    BaseModel,Field,EmailStr,field_validator,model_validator,computed_field
)
from typing import Optional,List
from datetime import datetime
from enum import Enum

#-----Enum-----------------------------------
class UserRole(str,Enum):
    admin="admin"
    editor="editor"
    viewer="viewer"
    
#-------Nested Models--------------
class Address(BaseModel):
    street:str
    city:str
    country:str
    zip_code:Optional[str]=None
    
#------Full user Model ----------
class UserCreate(BaseModel):
    name:str=Field(...,min_length=2,max_length=20)
    email:EmailStr
    age:int=Field(...,ge=18,le=30)
    role: UserRole=UserRole.viewer
    tags:list[str]=[]
    address:Optional[Address]=None
    password:str=Field(...,min_length=8)
    
#-----Field level validator ----------------
@field_validator("name")
@classmethod
def name_must_be_capitalized(cls,v: str) -> str:
    return v.strip().title()

#------cross field validator ----------
@model_validator(mode="after")
def check_admin_has_address(self) ->"UserCreate":
    if self.role==UserRole.admin and self.address is None:
        raise ValueError("Admin users must provide an address")
    return self

#------------Computed Fied ---------------
@computed_field
@property
def display_name(self) -> str :
    return f"{self.name} {self.role.value}"

#-------Seperate response model -----------
class responsemodel(BaseModel):
    id : int
    name: str
    email: EmailStr
    role: UserRole
    display_name:str
    created_at : datetime