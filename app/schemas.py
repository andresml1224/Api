from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    carrera: Optional[str] = None
    semestre: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fecha_registro: datetime
    model_config = {"from_attributes": True}

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str

class AuthResponse(BaseModel):
    success: bool
    message: str
    user: Optional[UsuarioResponse] = None
    token: Optional[str] = None

class EmocionResponse(BaseModel):
    id_emocion: int
    nombre_emocion: str
    emoji: str
    nivel: int
    
    model_config = {"from_attributes": True}

class ActividadResponse(BaseModel):
    id_actividad: int
    nombre_actividad: str
    categoria: str
    icono: str
    
    model_config = {"from_attributes": True}

class RegistroEmocionalCreate(BaseModel):
    id_emocion: int
    nota: Optional[str] = None
    actividades: List[int] = []

class RegistroEmocionalResponse(BaseModel):
    id_registro: int
    id_usuario: int
    id_emocion: int
    fecha_registro: datetime
    nota: Optional[str]
    emocion: EmocionResponse
    actividades: List[ActividadResponse] = []
    
    model_config = {"from_attributes": True}