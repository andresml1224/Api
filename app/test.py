from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración para XAMPP MySQL local
# Por defecto XAMPP usa:
# - Host: localhost
# - Puerto: 3306
# - Usuario: root
# - Password: "" (vacío por defecto en XAMPP)

# Intentar leer desde .env, sino usar configuración XAMPP por defecto
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:@localhost:3306/diario_emocional"
)

print(f"🔌 Conectando a MySQL: {DATABASE_URL.split('@')[1] if '@' in DATABASE_URL else 'localhost'}")

# Configuración del engine optimizado para XAMPP
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,      # Verificar conexión antes de usar
    pool_recycle=3600,       # Reciclar conexiones cada hora
    echo=False,              # Cambiar a True para ver queries SQL
    connect_args={
        "charset": "utf8mb4"  # Soporte completo de emojis 😊
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency para obtener sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    """Función para verificar la conexión a MySQL"""
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT VERSION()")
            version = result.fetchone()[0]
            print(f"✅ Conexión exitosa a MySQL {version}")
            print(f"✅ Base de datos: diario_emocional")
            return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        print("\n💡 Soluciones:")
        print("   1. Verifica que XAMPP esté ejecutando MySQL")
        print("   2. Abre phpMyAdmin: http://localhost/phpmyadmin")
        print("   3. Crea la base de datos 'diario_emocional'")
        print("   4. Verifica usuario/password en .env")
        return False