from pydantic import BaseModel, Field
from typing import Optional

class Shop(BaseModel):
    shopId: int = Field(..., ge=0, le=48)
    name: str
    city: str
    state: str

class Cars(BaseModel):
    VIN: str
    plate: str
    state: str
    Model: int
    owner_name: str
    owner_Address: str
    owner_DL: str
    problem_description: str
    date_in: str
    date_out: str
    technician: str
    city: str
    Zipcode: int
    shop: Shop


class ModifiedCar(BaseModel):
    VIN: Optional[str] = None
    plate: Optional[str] = None
    state: Optional[str] = None
    Model: Optional[int] = None
    owner_name: Optional[str] = None
    owner_Address: Optional[str] = None
    owner_DL: Optional[str] = None
    problem_description: Optional[str] = None
    date_in: Optional[str] = None
    date_out: Optional[str] = None
    technician: Optional[str] = None
    city: Optional[str] = None
    Zipcode: Optional[int] = None