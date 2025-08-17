# CRUD Alumnos – Flask + PostgreSQL + Frontend

Backend (Flask + PostgreSQL) y frontend (HTML/CSS/JS) separados.

---

## Backend rápido

```bash
cd backend
py -m pip install -r requirements.txt
py app.py  # http://127.0.0.1:5000
```
Variables en backend/.env
```bash
PG_HOST=localhost
PG_PORT=5432
PG_DB=alumnos_db
PG_USER=postgres
PG_PASSWORD=tu_clave
```
Endpoints
```bash
GET    /api/health
GET    /api/alumnos?q=texto
GET    /api/alumnos/:id
POST   /api/alumnos
PUT    /api/alumnos/:id
DELETE /api/alumnos/:id

```
Frontend
(ideal con Live Server para evitar bloqueos de fetch en algunos navegadores).

El frontend permite listar, agregar, editar, eliminar y buscar alumnos usando la API del backend.



Estructura del proyecto
```bash
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

```
 Notas
El id es autoincremental y puede tener huecos si se eliminan filas (comportamiento normal en SQL).


Driver de PostgreSQL: psycopg 3 con binarios para Windows (compatible con Python 3.13).

