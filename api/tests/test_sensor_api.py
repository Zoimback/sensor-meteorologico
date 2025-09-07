import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_sensors():
    response = client.get("/sensors")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0
    if data:
        assert "id" in data[0]
        assert "name" in data[0]
        assert "value" in data[0]

def test_get_sensor():
    # Primero obtenemos un sensor existente
    response = client.get("/sensors/1")
    if response.status_code == 200:
        sensor = response.json()
        assert sensor["id"] == 1
        assert "name" in sensor
        assert "value" in sensor
    else:
        assert response.status_code == 404

def test_create_sensor():
    new_sensor = {"name": "Pressure", "value": 101.3}
    response = client.post("/sensors", json=new_sensor)
    assert response.status_code == 200
    sensor = response.json()
    assert sensor["name"] == "Pressure"
    assert sensor["value"] == 101.3
    assert "id" in sensor
