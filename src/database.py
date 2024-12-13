from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///tareas.db?timeout=10"


engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    estado = Column(Boolean, default=False)


def agregar_tarea(title: String, descrip: String, state: Boolean):
    if not title.strip():
        raise ValueError("El título no puede estar vacío.")
    if not isinstance(state, bool):
        raise ValueError("El estado debe ser un valor booleano.")

    nueva_tarea = Tarea(titulo=title, descripcion=descrip, estado=state)

    try:
        session.add(nueva_tarea)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def listar_tareas():
    try:
        tareas = session.query(Tarea).all()
        return [
            {
                "id": tarea.id,
                "titulo": tarea.titulo,
                "descripcion": tarea.descripcion,
                "estado": tarea.estado,
            }
            for tarea in tareas
        ]

    except Exception as e:
        raise e
    finally:
        session.close()


""" def actualizar_tarea(
    id: int, title: String, descrip: String, state: Boolean
) -> Boolean:
    
    try:
        tarea = session.query(Tarea).filter(Tarea.id == id).first()

        if tarea:
            tarea.titulo = title
            tarea.descripcion = descrip
            tarea.estado = state

            session.commit()
            return True
        else:
            return False
    except Exception as e:
        raise e 
    finally:
        session.close() """


def actualizar_tarea(id: int, title: str, descrip: str, state: bool) -> bool:
    if not title.strip():
        raise ValueError("El título no puede estar vacío.")
    if not isinstance(state, bool):
        raise ValueError("El estado debe ser un valor booleano.")

    try:
        tarea = session.query(Tarea).filter(Tarea.id == id).first()

        if tarea:
            tarea.titulo = title
            tarea.descripcion = descrip
            tarea.estado = state

            session.commit()
            return True

        return False

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()


def eliminar_tarea(id: int) -> bool:
    if not isinstance(id, int) or id <= 0:
        raise ValueError("El ID debe ser un entero positivo.")
    try:
        tarea = session.query(Tarea).filter(Tarea.id == id).first()

        if tarea:
            session.delete(tarea)
            session.commit()
            return True
        return False

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()
