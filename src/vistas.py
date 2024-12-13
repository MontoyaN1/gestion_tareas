import streamlit as st
from funcion import create_json, subir_json, form_actualizar
from database import (
    listar_tareas,
    agregar_tarea,
    actualizar_tarea,
    eliminar_tarea,
)


def submenu_listar():
    st.header("Tareas")
    tareas = listar_tareas()

    if "success_message" in st.session_state:
        st.toast(st.session_state.success_message, icon="✅")
        del st.session_state.success_message

    if tareas:
        encabezado()

        iterar_columnas(tareas)

    else:
        st.info("No hay tareas disponibles.")


def encabezado():
    encabezados = st.columns([3, 1.5, 1.2, 1.3])
    with encabezados[0]:
        st.subheader("Título y descripción")
    with encabezados[1]:
        st.subheader("Estado")

    with encabezados[2]:
        st.subheader("Eliminar")

    with encabezados[3]:
        st.subheader("Actualizar")


def iterar_columnas(tareas):
    for tarea in tareas:
        cols = st.columns([3, 1.5, 1, 1])
        with cols[0]:
            st.write(f"**{tarea['titulo']}**\n{tarea['descripcion']}")

        with cols[1]:
            estado_actual = tarea["estado"]
            if estado_actual:
                estado = "Completada"
            else:
                estado = "Pendiente"

            marcado = st.checkbox(
                estado,
                value=tarea["estado"],
                key=f"completada-{tarea['id']}",
            )

            if marcado != tarea["estado"]:
                actualizar_tarea(
                    tarea["id"],
                    tarea["titulo"],
                    tarea["descripcion"],
                    marcado,
                )
                st.rerun()
                return

        with cols[2]:
            eliminar_key = f"eliminar-{tarea['id']}"
            if st.button("🗑️", key=eliminar_key):
                if eliminar_tarea(tarea["id"]):
                    st.session_state.success_message = "Tarea eliminada correctamente"
                    st.rerun()
                    return

        with cols[3]:
            actualizar_key = f"actualizar-{tarea['id']}"
            if st.button("✏️", key=actualizar_key):
                ver_actualiar(
                    tarea["id"],
                    tarea["titulo"],
                    tarea["descripcion"],
                    tarea["estado"],
                )


def submenu_agregar():
    st.header("Agregar Nueva Tarea")

    if "success_message" in st.session_state:
        st.toast(st.session_state.success_message)
        del st.session_state.success_message

    with st.form("add_task_form", clear_on_submit=True):
        title = st.text_input("Título")
        description = st.text_area("Descripción")
        submitted = st.form_submit_button("Agregar")

        if submitted:
            if title.strip() and description.strip():
                agregar_tarea(title, description, False)
                st.session_state.success_message = "Tarea agregada exitosamente."
                st.rerun()

            else:
                st.error("Por favor, completa todos los campos.")


def submenu_export_import():
    st.header("Exportar e Importar Tareas")

    tareas = listar_tareas()
    st.subheader("Exportar Tareas")
    if tareas:
        export_data = create_json()
        st.download_button(
            label="Descargar JSON",
            data=export_data,
            file_name="tareas.json",
            mime="application/json",
        )
    else:
        st.info("No hay tareas para exportar.")

    st.subheader("Importar Tareas")

    if "success_message" in st.session_state:
        st.toast(st.session_state.success_message)
        del st.session_state.success_message

    uploaded_file = st.file_uploader("Subir archivo JSON", type="json")
    if uploaded_file:
        try:
            content = uploaded_file.read().decode("utf-8")
            subir_json(content)
            st.session_state.success_message = "Tarea importada exitosamente."
            st.session_state.uploaded_file = uploaded_file

            if st.button("Importar"):
                st.rerun()

                return

        except Exception as e:
            st.error(f"Error al importar tareas: {e}")


@st.dialog("Actualizar tareas")
def ver_actualiar(id: int, title: str, descrip: str, estado: bool):
    form_actualizar(id, title, descrip, estado)
