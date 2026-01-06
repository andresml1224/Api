from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_usuario_by_email(db: Session, correo: str):
    return db.query(models.Usuario).filter(models.Usuario.correo == correo).first()

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    # NO hashear password por ahora (solo desarrollo)
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        carrera=usuario.carrera,
        semestre=usuario.semestre
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_emociones(db: Session):
    return db.query(models.Emocion).all()

def get_actividades(db: Session):
    return db.query(models.Actividad).all()

def crear_registro_emocional(db: Session, registro: schemas.RegistroEmocionalCreate, usuario_id: int):
    db_registro = models.RegistroEmocional(
        id_usuario=usuario_id,
        id_emocion=registro.id_emocion,
        nota=registro.nota,
        fecha_registro=datetime.utcnow()
    )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    
    # Agregar actividades si existen
    for actividad_id in registro.actividades:
        db_actividad = models.RegistroActividad(
            id_registro=db_registro.id_registro,
            id_actividad=actividad_id
        )
        db.add(db_actividad)
    
    db.commit()
    return db_registro