from fastapi import FastAPI, HTTPException, Depends
from tortoise.exceptions import DoesNotExist
from models import Address
from database import init_db
from utils import calculate_distance
from typing import List, Dict, Any
from pydantic import BaseModel
from schemas import AddressCreate

app = FastAPI()

@app.post("/addresses/", response_model=Dict[str, Any])
async def create_address(address_data: AddressCreate):
    obj = await Address.create(**address_data.dict())
    return {"id": obj.id, "name": obj.name, "address": obj.address, "latitude": obj.latitude, "longitude": obj.longitude}

@app.get("/addresses/", response_model=List[Dict[str, Any]])
async def get_addresses():
    addresses = await Address.all()
    return [{"id": address.id, "name": address.name, "address": address.address, "latitude": address.latitude, "longitude": address.longitude} for address in addresses]

@app.get("/addresses/{address_id}", response_model=Dict[str, Any])
async def get_address(address_id: int):
    try:
        address = await Address.get(id=address_id)
        return {"id": address.id, "name": address.name, "address": address.address, "latitude": address.latitude, "longitude": address.longitude}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Address not found")

@app.put("/addresses/{address_id}", response_model=Dict[str, Any])
async def update_address(address_id: int, address_data: AddressCreate):
    try:
        await Address.filter(id=address_id).update(**address_data.dict())
        address = await Address.get(id=address_id)
        return {"id": address.id, "name": address.name, "address": address.address, "latitude": address.latitude, "longitude": address.longitude}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Address not found")

@app.delete("/addresses/{address_id}", response_model=Dict[str, str])
async def delete_address(address_id: int):
    deleted_count = await Address.filter(id=address_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted"}

@app.post("/addresses/query", response_model=List[Dict[str, Any]])
async def get_addresses_within_distance(latitude: float, longitude: float, distance: float):
    addresses = await Address.all()
    result = []
    for address in addresses:
        if calculate_distance((latitude, longitude), (address.latitude, address.longitude)) <= distance:
            result.append(address)
    return [{"id": addr.id, "name": addr.name, "address": addr.address, "latitude": addr.latitude, "longitude": addr.longitude} for addr in result]

init_db(app)
