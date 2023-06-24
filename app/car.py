from pydantic import BaseModel, Field
from typing import Optional

class Cars(BaseModel):
    vin: str
    plate: str
    state: str
    model: int
    owner_name: str
    owner_address: str
    owner_dl: str
    problem_description: str
    date_in: str
    date_out: str
    technician: str
    shop_id: int = Field(..., ge=0, le=48)
    shop_name: str
    shop_city: str
    shop_state: str


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