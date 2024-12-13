import json
import streamlit as st
from database import listar_tareas, Tarea, session, actualizar_tarea
import time


def create_json():
    tareas = listar_tareas()
    export_data = json.dumps(tareas, indent=4)
    return export_data


def subir_json(contenido_json):
    try:
        # Cargar el contenido JSON
        tareas = json.loads(contenido_json)

        if not isinstance(tareas, list):
            raise ValueError("El archivo JSON debe contener una lista de tareas.")

        for tarea in tareas:
            if "id" not in tarea or "titulo" not in tarea or "estado" not in tarea:
                raise KeyError(
                    "El JSON debe contener las claves 'id', 'titulo' y 'estado'."
                )

            tarea_objeto = Tarea(
                id=tarea["id"],
                titulo=tarea["titulo"],
                descripcion=tarea.get("descripcion", ""),
                estado=bool(tarea["estado"]),
            )
            session.merge(tarea_objeto)

        session.commit()
        print("Tareas importadas correctamente.")
    except json.JSONDecodeError:
        raise ValueError("El archivo JSON proporcionado no es válido.")
    except KeyError as e:
        raise ValueError(f"Falta el campo requerido: {e}.")
    except Exception as e:
        session.rollback()
        raise e


def form_actualizar(id: int, title: str, descrip: str, estado: bool):
    with st.form("Actualizar "):
        titulo = st.text_input("Título", value=title)
        descripcion = st.text_input("Descripción", value=descrip)
        subir_boton = st.form_submit_button("Actualizar")

        if subir_boton:
            actualizar_tarea(id, titulo, descripcion, estado)
            st.success("Tarea actualizada correctamente")
            time.sleep(1.2)
            st.rerun()
