# 🚀 Guía Completa de Despliegue - Sistema de Predicción de Deserción Escolar

**Fecha:** 3 de noviembre de 2025  
**Proyecto:** Sistema de Predicción de Deserción Escolar  
**Plataformas:** GitHub + Render/Vercel

---

## 📋 Tabla de Contenidos

1. [Preparación del Proyecto](#preparación)
2. [Subir a GitHub](#github)
3. [Despliegue en Render](#render) ⭐ **Recomendado**
4. [Despliegue en Vercel](#vercel) (Alternativa)
5. [Configuración Post-Despliegue](#post-despliegue)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Preparación del Proyecto {#preparación}

### Archivos Creados para Despliegue:

✅ **Procfile** - Le dice a la plataforma cómo ejecutar la app
```
web: gunicorn run:app
```

✅ **runtime.txt** - Especifica la versión de Python
```
python-3.9.6
```

✅ **requirements-production.txt** - Dependencias optimizadas para producción
- Incluye gunicorn (servidor WSGI para producción)
- Solo paquetes necesarios para ejecutar la app

✅ **.gitignore** - Ya configurado correctamente

---

## 📦 PASO 1: Subir el Proyecto a GitHub {#github}

### 1.1 Inicializar Git en el Proyecto

```bash
# En la terminal, desde la carpeta del proyecto
cd /Users/alexandervargas/Trabajo_Grado/proyecto_desercion

# Inicializar repositorio git
git init

# Verificar archivos que se van a subir
git status
```

### 1.2 Configurar Git (primera vez)

```bash
# Configurar tu nombre y email (solo la primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@ejemplo.com"
```

### 1.3 Agregar Archivos al Repositorio

```bash
# Agregar todos los archivos (excepto los del .gitignore)
git add .

# Verificar qué se va a subir
git status

# Hacer el primer commit
git commit -m "Initial commit: Sistema de Predicción de Deserción Escolar"
```

### 1.4 Crear Repositorio en GitHub

**Opción A: Desde la Web (Más Fácil)**

1. Ve a https://github.com
2. Haz clic en el botón **"+"** (arriba derecha) → **"New repository"**
3. Configura el repositorio:
   - **Repository name:** `prediccion-desercion-escolar`
   - **Description:** "Sistema de predicción de deserción escolar con Machine Learning"
   - **Visibility:** 
     - ✅ **Public** (para trabajo de grado)
     - ⚠️ Private (si prefieres privado)
   - **NO marques:** "Initialize with README" (ya tienes uno)
4. Clic en **"Create repository"**

**Opción B: Desde GitHub CLI (si la tienes instalada)**

```bash
gh repo create prediccion-desercion-escolar --public --source=. --remote=origin
```

### 1.5 Conectar y Subir a GitHub

```bash
# Copiar el comando que GitHub te muestra, será algo como:
git remote add origin https://github.com/TU_USUARIO/prediccion-desercion-escolar.git

# Cambiar la rama principal a 'main'
git branch -M main

# Subir el código a GitHub
git push -u origin main
```

**⚠️ Si te pide autenticación:**
- Usa tu token de acceso personal (PAT) en lugar de tu contraseña
- Crear token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token

---

## 🌐 PASO 2: Despliegue en Render {#render}

### ⭐ **Render es RECOMENDADO porque:**
- ✅ Mejor para aplicaciones Flask
- ✅ Base de datos PostgreSQL gratis
- ✅ 750 horas gratis al mes
- ✅ Fácil configuración
- ✅ Logs accesibles

### 2.1 Crear Cuenta en Render

1. Ve a https://render.com
2. Clic en **"Get Started"**
3. Regístrate con tu cuenta de GitHub (más fácil)

### 2.2 Crear Web Service

1. En el Dashboard de Render, clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub:
   - Si es la primera vez, autoriza a Render a acceder a GitHub
   - Busca `prediccion-desercion-escolar`
   - Clic en **"Connect"**

### 2.3 Configurar el Web Service

**Configuración Básica:**
```
Name: prediccion-desercion-escolar
Region: Oregon (US West) o el más cercano
Branch: main
Root Directory: (dejar vacío)
Runtime: Python 3
Build Command: pip install -r requirements-production.txt
Start Command: gunicorn run:app
```

**Plan:**
- Selecciona **"Free"** (0 USD/mes)

**Variables de Entorno:**
Agregar estas en la sección "Environment Variables":
```
SECRET_KEY = tu-clave-secreta-super-segura-aqui
FLASK_ENV = production
DATABASE_URL = (si usas PostgreSQL, Render lo genera automático)
```

### 2.4 Desplegar

1. Clic en **"Create Web Service"**
2. Render automáticamente:
   - Clona tu repositorio
   - Instala dependencias
   - Inicia la aplicación
3. ⏱️ Espera 5-10 minutos (primera vez)
4. ✅ Tu app estará en: `https://prediccion-desercion-escolar.onrender.com`

### 2.5 Configurar Base de Datos (si es necesario)

Si usas base de datos:

1. En Render Dashboard → **"New +"** → **"PostgreSQL"**
2. Configurar:
   ```
   Name: desercion-db
   Database: desercion
   User: desercion_user
   Region: Same as Web Service
   Plan: Free
   ```
3. Clic en **"Create Database"**
4. Copiar el **"External Database URL"**
5. En tu Web Service → **Environment** → Agregar:
   ```
   DATABASE_URL = (pegar la URL de PostgreSQL)
   ```
6. Guardar y redesplegar

---

## 🔷 PASO 3: Despliegue en Vercel (Alternativa) {#vercel}

### ⚠️ **Nota:** Vercel es mejor para frontend, pero puede funcionar con Flask

### 3.1 Crear vercel.json

Primero, necesitas crear un archivo de configuración:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "run.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "run.py"
    }
  ]
}
```

### 3.2 Modificar run.py para Vercel

Agregar al final de `run.py`:

```python
# Para Vercel
app = create_app()

if __name__ == '__main__':
    app.run()
```

### 3.3 Desplegar en Vercel

1. Ve a https://vercel.com
2. Regístrate con GitHub
3. Clic en **"Add New"** → **"Project"**
4. Importa tu repositorio
5. Configuración automática (Vercel detecta Python)
6. Clic en **"Deploy"**

**Limitaciones de Vercel:**
- ⚠️ No soporta bien apps con ML pesadas
- ⚠️ Límite de tiempo de ejecución (10 seg)
- ⚠️ No tiene base de datos incluida

---

## ⚙️ PASO 4: Configuración Post-Despliegue {#post-despliegue}

### 4.1 Verificar que Todo Funciona

1. **Visita tu URL:**
   ```
   https://tu-app.onrender.com  (Render)
   https://tu-app.vercel.app    (Vercel)
   ```

2. **Prueba las rutas principales:**
   - `/` - Página de inicio/login
   - `/dashboard` - Dashboard principal
   - `/health` - Endpoint de salud (si lo tienes)

### 4.2 Configurar Dominio Personalizado (Opcional)

**En Render:**
1. Web Service → **Settings** → **Custom Domains**
2. Agregar tu dominio
3. Configurar DNS según instrucciones

**En Vercel:**
1. Project → **Settings** → **Domains**
2. Agregar dominio
3. Configurar DNS

### 4.3 Habilitar HTTPS

- ✅ Render: HTTPS automático
- ✅ Vercel: HTTPS automático

### 4.4 Monitoreo

**Render:**
- Dashboard → Tu servicio → **Logs**
- Ver logs en tiempo real
- Monitorear uso de recursos

**Vercel:**
- Project → **Deployments** → Ver logs
- Analytics disponible

---

## 🔧 PASO 5: Actualizar la Aplicación {#actualizar}

### Cada vez que hagas cambios:

```bash
# 1. Hacer cambios en tu código local

# 2. Probar localmente
python run.py

# 3. Agregar cambios a git
git add .
git commit -m "Descripción de los cambios"

# 4. Subir a GitHub
git push origin main

# 5. Render/Vercel se actualiza automáticamente
```

---

## 🐛 Troubleshooting {#troubleshooting}

### Problema: "Application failed to start"

**Solución:**
1. Verifica los logs en Render/Vercel
2. Asegúrate de que `gunicorn` esté en requirements
3. Verifica que `run.py` exporta correctamente `app`

### Problema: "Module not found"

**Solución:**
1. Verifica que todas las dependencias están en `requirements-production.txt`
2. Usa `pip freeze > requirements.txt` localmente
3. Redeploy

### Problema: "Database connection failed"

**Solución:**
1. Verifica que `DATABASE_URL` está configurado
2. En desarrollo local, usa SQLite
3. En producción, usa PostgreSQL de Render

### Problema: "Modelos .pkl no se cargan"

**Solución:**
1. Asegúrate de que los archivos `.pkl` están en el repositorio
2. Si son muy grandes (>100MB), considera:
   - Git LFS (Large File Storage)
   - Almacenamiento externo (AWS S3, Google Cloud)

### Problema: "App se duerme (Render Free)"

**Explicación:**
- El plan gratuito de Render "duerme" la app después de 15 min de inactividad
- Primera petición después de dormir tarda 30-60 seg

**Solución:**
- Actualizar a plan paid ($7/mes)
- O aceptar el delay en la primera carga

---

## 📊 Comparación: Render vs Vercel

| Característica | Render | Vercel |
|---------------|--------|--------|
| **Mejor para** | Backend/Full-stack | Frontend/Serverless |
| **Flask Support** | ✅ Excelente | ⚠️ Limitado |
| **Base de Datos** | ✅ PostgreSQL gratis | ❌ No incluida |
| **Tiempo CPU** | ✅ Ilimitado (Free) | ⚠️ 10 seg límite |
| **ML Models** | ✅ Soporta | ⚠️ Limitado |
| **Horas gratis** | 750 hrs/mes | Ilimitado |
| **Deploy automático** | ✅ Sí | ✅ Sí |
| **Custom domain** | ✅ Sí | ✅ Sí |
| **HTTPS** | ✅ Gratis | ✅ Gratis |
| **Logs** | ✅ Accesibles | ✅ Accesibles |

**🏆 Recomendación: Usar RENDER para este proyecto**

---

## 📝 Checklist Final

Antes de desplegar, verifica:

- [ ] ✅ `.gitignore` configurado correctamente
- [ ] ✅ `Procfile` creado
- [ ] ✅ `runtime.txt` con Python 3.9.6
- [ ] ✅ `requirements-production.txt` con todas las dependencias
- [ ] ✅ Variables de entorno configuradas
- [ ] ✅ Código probado localmente
- [ ] ✅ Base de datos configurada (si aplica)
- [ ] ✅ Archivos `.pkl` de modelos incluidos o accesibles
- [ ] ✅ README actualizado con URL de la app

---

## 🎯 Próximos Pasos Después del Despliegue

1. ✅ Probar todas las funcionalidades en producción
2. ✅ Configurar monitoreo de errores
3. ✅ Documentar la URL en tu trabajo de grado
4. ✅ Hacer demo para la presentación
5. ✅ Considerar CI/CD para deploys automáticos

---

## 📞 Recursos Adicionales

- **Render Docs:** https://render.com/docs
- **Vercel Docs:** https://vercel.com/docs
- **Flask Deployment:** https://flask.palletsprojects.com/en/3.0.x/deploying/
- **Gunicorn Docs:** https://docs.gunicorn.org/

---

**¡Tu aplicación estará en línea y accesible desde cualquier lugar! 🚀**

**Fecha:** 3 de noviembre de 2025  
**Proyecto:** Sistema de Predicción de Deserción Escolar  
**Estado:** Listo para despliegue ✅
