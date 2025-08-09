from flask import Blueprint, request, jsonify
from db import query_all, query_one, execute

api = Blueprint("api", __name__, url_prefix="/api")

# LISTAR con búsqueda opcional ?q=
@api.get("/alumnos")
def list_alumnos():
    q = request.args.get("q", "").strip()
    if q:
        like = f"%{q}%"
        sql = """SELECT * FROM alumno
                 WHERE nombre ILIKE %s OR apellido ILIKE %s
                 ORDER BY id;"""
        rows = query_all(sql, (like, like))
    else:
        rows = query_all("SELECT * FROM alumno ORDER BY id;")
    return jsonify(rows)

# OBTENER por id
@api.get("/alumnos/<int:aid>")
def get_alumno(aid):
    row = query_one("SELECT * FROM alumno WHERE id=%s;", (aid,))
    if not row:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify(row)

# CREAR
@api.post("/alumnos")
def create_alumno():
    data = request.get_json(force=True, silent=True) or {}
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    edad = data.get("edad")

    if not (nombre and apellido and isinstance(edad, int)):
        return jsonify({"error": "Datos inválidos"}), 400

    new_row = query_one(
        "INSERT INTO alumno (nombre, apellido, edad) VALUES (%s, %s, %s) RETURNING id;",
        (nombre, apellido, edad),
    )
    return jsonify({"message": "Creado", "id": new_row["id"]}), 201

# ACTUALIZAR
@api.put("/alumnos/<int:aid>")
def update_alumno(aid):
    data = request.get_json(force=True, silent=True) or {}
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    edad = data.get("edad")

    if not (nombre and apellido and isinstance(edad, int)):
        return jsonify({"error": "Datos inválidos"}), 400

    exists = query_one("SELECT id FROM alumno WHERE id=%s;", (aid,))
    if not exists:
        return jsonify({"error": "Alumno no encontrado"}), 404

    execute(
        "UPDATE alumno SET nombre=%s, apellido=%s, edad=%s WHERE id=%s;",
        (nombre, apellido, edad, aid),
    )
    return jsonify({"message": "Actualizado"})

# ELIMINAR
@api.delete("/alumnos/<int:aid>")
def delete_alumno(aid):
    exists = query_one("SELECT id FROM alumno WHERE id=%s;", (aid,))
    if not exists:
        return jsonify({"error": "Alumno no encontrado"}), 404

    execute("DELETE FROM alumno WHERE id=%s;", (aid,))
    return jsonify({"message": "Eliminado"})
