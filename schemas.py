from pydantic import BaseModel

class AddressCreate(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
