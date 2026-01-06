# 🚀 Guía Rápida: XAMPP Setup

## 🎯 Inicio Ultra-Rápido (1 minuto)

### 1️⃣ Iniciar XAMPP
- Abre **XAMPP Control Panel**
- Click **Start** en MySQL (debe quedar verde)

### 2️⃣ Crear Base de Datos
- Abre: http://localhost/phpmyadmin
- Click **"Nueva"**
- Nombre: `diario_emocional`
- Click **"Crear"**

### 3️⃣ Configurar Proyecto
```bash
# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env (copiar el contenido de abajo)
```

**Archivo `.env`:**
```env
DATABASE_URL=mysql+pymysql://root:@localhost:3306/diario_emocional
```

### 4️⃣ Inicializar y Arrancar
```bash
# Crear tablas e insertar datos iniciales
python init_db.py

# Iniciar API
python start.bat  # Windows
# o
bash start.sh     # Mac/Linux
```

### 5️⃣ Verificar
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Test: http://localhost:8000/test-db
- phpMyAdmin: http://localhost/phpmyadmin

---

## 📱 Para Android

### Emulador Android Studio
```kotlin
private const val BASE_URL = "http://10.0.2.2:8000/"
```

### Dispositivo Físico
```bash
# 1. Obtén tu IP
ipconfig  # Windows
ifconfig  # Mac/Linux

# 2. Usa tu IP en Android
private const val BASE_URL = "http://192.168.1.X:8000/"

# 3. Inicia API expuesta a la red
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 🔧 Troubleshooting Rápido

### ❌ "Can't connect to MySQL"
- Verifica que MySQL esté en verde en XAMPP
- Reinicia MySQL en XAMPP Control Panel

### ❌ "Unknown database"
- Crea la base de datos en phpMyAdmin
- Nombre exacto: `diario_emocional`

### ❌ "Access denied"
- Verifica `.env`: `root:@localhost` (password vacío)
- Si cambiaste password: `root:tu_password@localhost`

### ❌ Android no conecta
- Emulador: usa `10.0.2.2:8000`
- Físico: usa tu IP local (ej: `192.168.1.10:8000`)
- Verifica firewall de Windows

---

## 💡 Comandos Útiles

```bash
# Verificar configuración
python test_xampp.py

# Ver datos
http://localhost/phpmyadmin

# Reiniciar base de datos
python init_db.py

# Iniciar en otro puerto
uvicorn app.main:app --reload --port 8001
```

---

## 📊 Ver Datos en Tiempo Real

**phpMyAdmin:** http://localhost/phpmyadmin
- Click en `diario_emocional`
- Explora las tablas
- Ejecuta queries SQL

**Swagger UI:** http://localhost:8000/docs
- Prueba endpoints
- Ver schemas
- Ejecutar requests

---

## 🎓 Ventajas de XAMPP

✅ Todo local, sin internet  
✅ phpMyAdmin incluido  
✅ Gratis y sin límites  
✅ Perfecto para desarrollo  
✅ Fácil de configurar  

---

## 🚀 Para Producción

Cuando estés listo para publicar:
1. Sigue el tutorial: **TUTORIAL.md**
2. Usa Railway + Render
3. Misma API, solo cambias la URL

---

**¿Problemas?** Ejecuta `python test_xampp.py` para diagnóstico completo.
