from api.models.sensor import Sensor, SensorCreate
from fastapi import HTTPException
from typing import List

# Mock database
sensors_db = [
    Sensor(id=1, name="Temperature", value=23.5),
    Sensor(id=2, name="Humidity", value=60.2)
]

class SensorService:
    @staticmethod
    def get_all() -> List[Sensor]:
        return sensors_db

    @staticmethod
    def get_by_id(sensor_id: int) -> Sensor:
        for sensor in sensors_db:
            if sensor.id == sensor_id:
                return sensor
        raise HTTPException(status_code=404, detail="Sensor not found")

    @staticmethod
    def create(sensor_data: SensorCreate) -> Sensor:
        new_id = max([s.id for s in sensors_db], default=0) + 1
        sensor = Sensor(id=new_id, **sensor_data.dict())
        sensors_db.append(sensor)
        return sensor
