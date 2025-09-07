## DDBB - Sensor Meteorológico

### Descripción
Esquema de base de datos para auditoría, despliegues y datos de sensores meteorológicos.

### Estructura de tablas
| Tabla        | Campos principales                                   |
|--------------|------------------------------------------------------|
| audit        | id, Aplication, Date, Repository, End, Branch        |
| despliegues  | id, Aplication, Date, Repository, Ends, Branch, Path, ServerName |
| data         | id, Temperatura, Posicion, Nombre, Fecha             |
| sensor       | Name, Batery, Estado                                 |

### Mejoras sugeridas
- Normalizar nombres de columnas/tablas
- Añadir campos created_at y updated_at
- Documentar migraciones y scripts
