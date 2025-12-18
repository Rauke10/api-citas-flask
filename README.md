# API de Citas con Flask y MongoDB

API sencilla para gestionar usuarios, centros y citas médicas usando Flask, JWT y MongoDB.

## CI/CD Pipeline

Este proyecto implementa un pipeline de integración y despliegue continuo usando GitHub Actions.

### Flujo automático

Cada vez que se hace push a la rama `main`:

1. ✅ **Tests unitarios**: Se ejecutan 18 tests que verifican:
   - Endpoints de autenticación (login, register)
   - Endpoints de centros médicos
   - Endpoints de citas
   - Validación de tokens JWT
   - Tests con MongoDB mockeado

2. ✅ **Despliegue automático**: Si los tests pasan, se despliega automáticamente a:
   - Servidor: `103.23.61.152`
   - Ruta: `/var/www/alumnos/rhernandez/flask_app/api-citas-flask`
   - Apache se recarga automáticamente

### Ejecutar tests localmente

````bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest -v tests

# Ejecutar tests con cobertura
pytest --cov=application tests/
````

## Requisitos previos

    Python 3.10 o superior
    MongoDB en ejecución y accesible
    (Opcional) Entorno virtual para aislar dependencias

## Configuración del entorno

Clona el repositorio y entra en la carpeta del proyecto.

Crea y activa un entorno virtual (recomendado):

```bash
python3 -m venv venv
source venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Variables de entorno

Configura la conexión a MongoDB y Flask (usa los valores por defecto si no las defines):

```bash
export MONGODB_URI="mongodb://localhost:27017/"
export MONGODB_DB="Clinica"
export FLASK_APP=application.py
export FLASK_ENV=development
```

## Ejecución de migraciones

Ejecuta el script de migración para crear las colecciones, índices y centros de ejemplo:

```bash
python migrations/001_init_clinica.py
```

El script usa MONGODB_URI y MONGODB_DB para conectarse.

## Iniciar la API

Arranca el servidor de desarrollo en la red local:

```bash
flask run --host=0.0.0.0 --port=5000
```

La documentación Swagger estará disponible en http://localhost:5000/apidocs.

## Flujos básicos

    Registro: POST /register con username, password y datos del usuario.
    Login: POST /login devuelve un token JWT.
    Centros: GET /centers requiere token en el encabezado Authorization: Bearer <token>.
    Citas: Endpoints /date/create, /date/getByDay, /date/getByUser, /date/delete y /dates para gestionar citas.

## Tests

El proyecto incluye tests unitarios e integración que cubren:
- Autenticación y autorización
- Gestión de centros médicos
- Gestión de citas
- Validación de JWT

Para ejecutar los tests:

```bash
pytest -v tests
```

## Despliegue

El despliegue se realiza automáticamente mediante GitHub Actions cuando se hace push a `main`.

### Requisitos del servidor:
- Apache2 con mod_wsgi
- Python 3.12
- MongoDB
- Entorno virtual configurado en `/var/www/alumnos/rhernandez/flask_app/venv/`

## Notas

    Ejecuta el script de migración cada vez que montes un entorno nuevo.
    Asegúrate de que MongoDB esté en marcha antes de iniciar la API.
    Utiliza herramientas como Postman o curl para probar los endpoints.

## Autor

Proyecto desarrollado para la asignatura de Puesta en Producción.
