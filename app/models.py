from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime
import enum

class TipoEmisor(enum.Enum):
    usuario = "usuario"
    IA = "IA"

class Usuario(Base):
    __tablename__ = "usuarios"
    
    # CAMBIO: Agregar length a String para MySQL
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))  # ← Ahora con length
    correo = Column(String(150), unique=True, index=True)  # ← Ahora con length
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    foto_perfil = Column(Text, nullable=True)
    ultima_conexion = Column(DateTime, nullable=True)
    carrera = Column(String(150), nullable=True)  # ← Ahora con length
    semestre = Column(Integer, nullable=True)
    
    registros = relationship("RegistroEmocional", back_populates="usuario")
    chats = relationship("Chat", back_populates="usuario")
    estadisticas = relationship("Estadistica", back_populates="usuario")

class Emocion(Base):
    __tablename__ = "emociones"
    
    # CAMBIO: Agregar length a String para MySQL
    id_emocion = Column(Integer, primary_key=True, index=True)
    nombre_emocion = Column(String(50))  # ← Ahora con length
    emoji = Column(String(10))  # ← Ahora con length
    nivel = Column(Integer)
    
    registros = relationship("RegistroEmocional", back_populates="emocion")

class Actividad(Base):
    __tablename__ = "actividades"
    
    # CAMBIO: Agregar length a String para MySQL
    id_actividad = Column(Integer, primary_key=True, index=True)
    nombre_actividad = Column(String(100))  # ← Ahora con length
    categoria = Column(String(50))  # ← Ahora con length
    icono = Column(String(50))  # ← Ahora con length
    
    registros = relationship("RegistroActividad", back_populates="actividad")

class RegistroEmocional(Base):
    __tablename__ = "registros_emocionales"
    
    id_registro = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_emocion = Column(Integer, ForeignKey("emociones.id_emocion"))
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    nota = Column(Text)
    
    usuario = relationship("Usuario", back_populates="registros")
    emocion = relationship("Emocion", back_populates="registros")
    actividades = relationship("RegistroActividad", back_populates="registro")
    chats = relationship("Chat", back_populates="registro")

class RegistroActividad(Base):
    __tablename__ = "registro_actividad"
    
    id_registro = Column(Integer, ForeignKey("registros_emocionales.id_registro"), primary_key=True)
    id_actividad = Column(Integer, ForeignKey("actividades.id_actividad"), primary_key=True)
    
    registro = relationship("RegistroEmocional", back_populates="actividades")
    actividad = relationship("Actividad", back_populates="registros")

class Chat(Base):
    __tablename__ = "chats"
    
    id_chat = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_registro = Column(Integer, ForeignKey("registros_emocionales.id_registro"), nullable=True)
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)
    
    usuario = relationship("Usuario", back_populates="chats")
    registro = relationship("RegistroEmocional", back_populates="chats")
    mensajes = relationship("Mensaje", back_populates="chat")

class Mensaje(Base):
    __tablename__ = "mensajes"
    
    id_mensaje = Column(Integer, primary_key=True, index=True)
    id_chat = Column(Integer, ForeignKey("chats.id_chat"))
    emisor = Column(Enum(TipoEmisor))
    contenido = Column(Text)
    fecha_envio = Column(DateTime, default=datetime.utcnow)
    
    chat = relationship("Chat", back_populates="mensajes")

class Estadistica(Base):
    __tablename__ = "estadisticas"
    
    # CAMBIO: Agregar length a String para MySQL
    id_estadistica = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    emocion_predominante = Column(String(50))  # ← Ahora con length
    total_registros = Column(Integer)
    porcentaje_increible = Column(Float)
    porcentaje_bien = Column(Float)
    porcentaje_meh = Column(Float)
    porcentaje_mal = Column(Float)
    porcentaje_horrible = Column(Float)
    
    usuario = relationship("Usuario", back_populates="estadisticas")