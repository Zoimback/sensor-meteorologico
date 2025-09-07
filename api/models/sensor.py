from pydantic import BaseModel

class Sensor(BaseModel):
    id: int
    name: str
    value: float

class SensorCreate(BaseModel):
    name: str
    value: float
