import streamlit as st
from vistas import submenu_agregar, submenu_export_import, submenu_listar
from database import (
    Base,
    engine,
)


def main():
    Base.metadata.create_all(bind=engine)

    st.title("Administrador de Tareas")

    listar, agregar, export_import = st.tabs(
        ["Ver Tareas", "Agregar Tarea", "Exportar/Importar"]
    )

    with listar:
        submenu_listar()

    with agregar:
        submenu_agregar()

    with export_import:
        submenu_export_import()


if __name__ == "__main__":
    main()
