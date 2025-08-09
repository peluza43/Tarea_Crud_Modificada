// Cambia esto si el backend corre en otra URL
const API = "http://127.0.0.1:5000/api/alumnos";

const $ = s => document.querySelector(s);
const tbody   = $("#tabla tbody");
const form    = $("#form");
const buscar  = $("#buscar");
const msg     = $("#msg");

function esc(s){ return String(s).replace(/"/g,'&quot;').replace(/'/g,"&#39;"); }
function setMsg(text, ok=true){ msg.textContent = text || ""; msg.className = ok ? "ok" : "err"; }

async function listar(q = "") {
  try {
    const url = q ? `${API}?q=${encodeURIComponent(q)}` : API;
    const res = await fetch(url);
    const data = await res.json();
    tbody.innerHTML = data.map(a => `
      <tr>
        <td>${a.id}</td>
        <td>${a.nombre}</td>
        <td>${a.apellido}</td>
        <td>${a.edad}</td>
        <td>
          <button onclick="editar(${a.id}, '${esc(a.nombre)}', '${esc(a.apellido)}', ${a.edad})">Editar</button>
          <button onclick="eliminar(${a.id})">Eliminar</button>
        </td>
      </tr>
    `).join("");
    if (!data.length) setMsg("Sin resultados", true);
    else setMsg("");
  } catch(e) {
    setMsg("Error listando alumnos", false);
    console.error(e);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const id = $("#id").value.trim();
  const payload = {
    nombre: $("#nombre").value.trim(),
    apellido: $("#apellido").value.trim(),
    edad: Number($("#edad").value)
  };
  if (!payload.nombre || !payload.apellido || !Number.isInteger(payload.edad)){
    setMsg("Completa nombre, apellido y edad válida", false);
    return;
  }

  const method = id ? "PUT" : "POST";
  const url = id ? `${API}/${id}` : API;

  try {
    const res = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const body = await res.json().catch(()=> ({}));
    if (!res.ok) throw new Error(body.error || res.statusText);
    setMsg(id ? "Actualizado" : "Creado", true);
    limpiar();
    listar(buscar.value);
  } catch (e) {
    setMsg("Error al guardar: " + e.message, false);
  }
});

async function eliminar(id){
  if(!confirm("¿Eliminar alumno?")) return;
  try {
    const res = await fetch(`${API}/${id}`, { method: "DELETE" });
    const body = await res.json().catch(()=> ({}));
    if (!res.ok) throw new Error(body.error || res.statusText);
    setMsg("Eliminado", true);
    listar(buscar.value);
  } catch (e) {
    setMsg("Error al eliminar: " + e.message, false);
  }
}

function editar(id, nombre, apellido, edad){
  $("#id").value = id;
  $("#nombre").value = nombre;
  $("#apellido").value = apellido;
  $("#edad").value = edad;
  setMsg("Editando registro " + id, true);
}

function limpiar(){
  form.reset();
  $("#id").value = "";
}

$("#cancelar").onclick   = limpiar;
$("#btnBuscar").onclick  = () => listar(buscar.value);
$("#btnLimpiar").onclick = () => { buscar.value=""; listar(); };

// carga inicial
listar();
