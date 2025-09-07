## API - Sensor Meteorológico

### Descripción
API REST para gestión de sensores meteorológicos. Implementada en FastAPI, estructura modular (routes, services, managers, resilience).

### Endpoints principales
| Método | Endpoint         | Descripción           |
|--------|------------------|----------------------|
| GET    | /sensors         | Listar sensores      |
| GET    | /sensors/{id}    | Consultar sensor     |
| POST   | /sensors         | Crear sensor         |

### Estructura de carpetas
- routes: Definición de endpoints
- managers: Abstracción de lógica
- resilience: Resiliencia y fallback
- services: Acceso a datos/mock
- models: Esquemas Pydantic
- tests: Pruebas unitarias

### Ejemplo de uso
```bash
uvicorn api.main:app --reload
curl http://localhost:8000/sensors
```

### Mejoras sugeridas
- Integrar base de datos real
- Añadir logging y validaciones
- Automatizar pruebas en CI/CD
