# CRUD Alumnos (Flask + PostgreSQL + Frontend vanilla)

Proyecto dividido en **backend** (API REST con Flask y PostgreSQL) y **frontend** (HTML/CSS/JS puro) que consume la API por `fetch`.

## Requisitos

- Python 3.11+ (probado con 3.13)
- PostgreSQL 14+ (probado con 17)
- (Opcional) VS Code + extensión **Live Server** para servir el frontend

---

## 1) Backend

### Instalar dependencias
```bash
cd backend
py -m pip install -r requirements.txt


Variables de entorno
Crear backend/.env (no se sube).
Usa backend/.env.example como referencia:

Variables de entorno
Crear backend/.env (no se sube).
Usa backend/.env.example como referencia:

Base de datos
Crear DB alumnos_db y ejecutar backend/sql/init.sql (pgAdmin o psql):

Base de datos
Crear DB alumnos_db y ejecutar backend/sql/init.sql (pgAdmin o psql):

Ejecutar API
cd backend
py app.py
# -> http://127.0.0.1:5000

Endpoints
GET /api/health → {"status":"ok"}

GET /api/alumnos → lista todos, admite búsqueda ?q=texto

GET /api/alumnos/<id>

POST /api/alumnos → {"nombre":"Ana","apellido":"Lopez","edad":20}

PUT /api/alumnos/<id> → mismo body que POST

DELETE /api/alumnos/<id>

Ejemplos (Windows PowerShell)
powershell
Copiar
Editar

# Crear
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/alumnos" `
  -Method POST -ContentType "application/json" `
  -Body '{"nombre":"Ana","apellido":"Lopez","edad":20}'

# Listar
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/alumnos"

# Actualizar
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/alumnos/1" `
  -Method PUT -ContentType "application/json" `
  -Body '{"nombre":"Ana","apellido":"Lopez","edad":21}'

# Eliminar
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/alumnos/1" -Method DELETE

2) Frontend
Contenido en /frontend:

index.html

styles.css

app.js

Cómo abrir
Con Live Server: clic derecho en index.html → Open with Live Server

O abre index.html con doble clic.

⚠ Si el navegador bloquea fetch, usa Live Server.

El frontend permite listar, agregar, editar, eliminar y buscar alumnos usando la API del backend.

backend/
  app.py
  routes.py
  db.py
  requirements.txt
  .env.example
  sql/
    init.sql
frontend/
  index.html
  styles.css
  app.js
.gitignore
README.md

Notas
El id es autoincremental y puede tener “huecos” si se eliminan filas (comportamiento normal de SQL).

No subas backend/.env (está ignorado por .gitignore).

Driver de Postgres: psycopg 3 con binarios para Windows (compatible con Python 3.13).

