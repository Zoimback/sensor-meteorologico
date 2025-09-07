from api.services.sensor_service import SensorService
from api.models.sensor import Sensor, SensorCreate
from typing import List

class SensorManager:
    @staticmethod
    def list_sensors() -> List[Sensor]:
        return SensorService.get_all()

    @staticmethod
    def get_sensor(sensor_id: int) -> Sensor:
        return SensorService.get_by_id(sensor_id)

    @staticmethod
    def add_sensor(sensor_data: SensorCreate) -> Sensor:
        return SensorService.create(sensor_data)
