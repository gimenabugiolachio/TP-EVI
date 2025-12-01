# TP – Entornos Virtualizados (EVI)
### Alumna: Gimena Bugiolachio  
### Año: 2025  
### Carrera: Tecnicatura Universitaria en Tecnologías de la Información – UTN

---

# Descripción del proyecto
Implementé una API RESTful completa para la gestión de tareas (ToDo, Doing, Done) utilizando:

- Flask (framework web)
- SQLAlchemy (ORM)
- PostgreSQL (base de datos)
- Docker + Docker Compose (orquestación de contenedores)
- Adminer (cliente web SQL)

El sistema permite:
✔ Crear tareas
✔ Listar tareas
✔ Modificar tareas
✔ Eliminar tareas
✔ Persistir los datos en PostgreSQL
✔ Administrar la base mediante Adminer

---

# Docker Compose

El proyecto se ejecuta usando Docker Compose.

## Levantar el entorno

docker compose up --build

Esto crea y levanta los contenedores:
- tp_api
- tp_db
- tp_adminer

---

## Detener contenedores

docker compose down

---

# Endpoints de la API
* Healthcheck
    GET /health
    Respuesta: {"status": "ok"}

* Listar tareas
    GET /tasks

*Crear tarea
    POST /tasks
    Body JSON:
    {
    "title": "Comprar harina",
    "description": "Ir al super"
    }

* Modificar tarea
    PUT /tasks/<id>
    Ejemplo:
    {
    "status": "Doing"
    }

* Eliminar tarea
    DELETE /tasks/<id>

    ---

# Pruebas con PowerShell / curl

Crear:
curl -Method POST -Uri "http://localhost:5000/tasks" -Body '{"title":"Comprar harina","description":"Ir al super"}' -ContentType "application/json"

Listar:
curl http://localhost:5000/tasks

Modificar:
curl -Method PUT -Uri "http://localhost:5000/tasks/1" -Body '{"status":"Doing"}' -ContentType "application/json"

Eliminar:
curl -Method DELETE -Uri "http://localhost:5000/tasks/1"

---

# Conexión a Adminer

Abrir en navegador:
http://localhost:8080

Datos de acceso:
Motor: PostgreSQL
Servidor: db
Usuario: tareas_user
Contraseña: superseguro123
Base de datos: tareas_db

---

## Estructura del proyecto

```text
TP-EVI/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── .env
└── README.md
```


---

# Tecnologías utilizadas

- Python 3.12
- Flask
- SQLAlchemy
- PostgreSQL 16 (alpine)
- Adminer
- Docker
- Docker Compose

