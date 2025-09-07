from api.managers.sensor_manager import SensorManager
from api.models.sensor import Sensor, SensorCreate

class SensorResilience:
    @staticmethod
    def get_sensors():
        return SensorManager.list_sensors()

    @staticmethod
    def get_sensor(sensor_id: int):
        return SensorManager.get_sensor(sensor_id)

    @staticmethod
    def create_sensor(sensor_data: SensorCreate):
        return SensorManager.add_sensor(sensor_data)
