from fastapi import FastAPI
from api.routes.sensor_routes import router as sensor_router

app = FastAPI(title="Sensor API")
app.include_router(sensor_router)

# Pequeño ejemplo de uso
# Ejecuta: uvicorn api.main:app --reload
# Prueba: curl http://localhost:8000/sensors
