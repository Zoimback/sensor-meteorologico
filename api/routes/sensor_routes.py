from fastapi import APIRouter
from typing import List
from api.models.sensor import Sensor, SensorCreate
from api.resilience.sensor_resilience import SensorResilience

router = APIRouter()

@router.get("/sensors", response_model=List[Sensor])
def get_sensors():
    return SensorResilience.get_sensors()

@router.get("/sensors/{sensor_id}", response_model=Sensor)
def get_sensor(sensor_id: int):
    return SensorResilience.get_sensor(sensor_id)

@router.post("/sensors", response_model=Sensor)
def create_sensor(sensor: SensorCreate):
    return SensorResilience.create_sensor(sensor)
