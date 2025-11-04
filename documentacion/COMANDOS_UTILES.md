# 🎯 Comandos Útiles - Referencia Rápida

## 🚀 Scripts de Inicio

```bash
# Menú interactivo
./inicio_rapido.sh

# Verificar configuración
./verificar_entorno.sh

# Activar entorno virtual
source .venv/bin/activate
# o
./activate.sh
```

## 🌐 Servidor Flask

```bash
# Iniciar servidor de desarrollo
python run.py

# Iniciar con variables de entorno específicas
FLASK_ENV=development FLASK_DEBUG=1 python run.py

# Acceder al dashboard
open http://localhost:5000
```

## 🤖 Modelos de Machine Learning

```bash
# Modelo Base (BD original)
python modelos/modelo_desercion_escolar.py

# Modelo Nuevo (BD completa)
python modelos/modelo_desercion_nuevo.py

# Modelo Balanceado (75/25)
python modelos/modelo_desercion_balanceado.py

# Evaluador de modelos
python modelos/evaluador.py
```

## 📊 Base de Datos

```bash
# Inicializar base de datos
python init_db.py

# Ubicación de la base de datos
ls -lh instance/app.db

# Backup de la base de datos
cp instance/app.db instance/app.db.backup
```

## 📦 Gestión de Paquetes

```bash
# Listar paquetes instalados
pip list

# Verificar paquete específico
pip show nombre_paquete

# Actualizar pip
pip install --upgrade pip

# Instalar nuevo paquete
pip install nombre_paquete

# Guardar cambios en requirements
pip freeze > requirements_nuevo.txt
```

## 🔍 Verificación y Diagnóstico

```bash
# Verificar versión de Python
python --version

# Verificar que el entorno esté activado
which python
# Debería mostrar: .../proyecto_desercion/.venv/bin/python

# Probar importaciones
python -c "import flask, pandas, sklearn; print('OK')"

# Ver información del sistema
python -c "import platform; print(platform.platform())"
```

## 🧹 Limpieza

```bash
# Limpiar archivos de caché Python
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Limpiar archivos temporales
rm -rf catboost_info/

# Ver espacio usado por .venv
du -sh .venv
```

## 📝 Git (si usas control de versiones)

```bash
# Estado del repositorio
git status

# Ver cambios
git diff

# Agregar cambios
git add .

# Commit
git commit -m "Descripción del cambio"

# Push
git push origin main
```

## 🛠️ Mantenimiento del Entorno

```bash
# Recrear entorno virtual desde cero
rm -rf .venv
python3.9 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Reinstalar paquete específico para ARM64
pip uninstall -y nombre_paquete
pip install --no-cache-dir nombre_paquete
```

## 🎨 VS Code

```bash
# Abrir proyecto en VS Code
code .

# Abrir archivo específico
code archivo.py

# Instalar extensión desde terminal
code --install-extension ms-python.python

# Listar extensiones instaladas
code --list-extensions
```

## 📊 Análisis de Datos

```bash
# Abrir directorio de resultados
open resultados/

# Ver estructura de resultados
tree resultados/ -L 2

# Contar archivos CSV en resultados
find resultados/ -name "*.csv" | wc -l

# Ver últimos resultados generados
ls -lt resultados/modelo_balanceado/ | head
```

## 🔧 Troubleshooting

```bash
# Si XGBoost falla
brew install libomp

# Si hay problemas con Homebrew
brew update
brew doctor

# Si Python no se encuentra
which python3.9
/opt/homebrew/bin/python3.9 --version

# Verificar arquitectura
uname -m
# Debería mostrar: arm64

# Ver paquetes instalados con arquitectura
pip list -v | grep pandas
```

## 📖 Documentación

```bash
# Abrir documentación principal
open README.md

# Abrir índice de documentación
open documentacion/INDICE_DOCUMENTACION.md

# Abrir guía de setup
open SETUP_MAC_M1.md

# Listar toda la documentación
ls -la documentacion/
```

## 🎯 Atajos de Teclado en Terminal (macOS)

- `Ctrl + C`: Detener proceso actual
- `Ctrl + D`: Cerrar terminal/sesión
- `Cmd + K`: Limpiar pantalla
- `Cmd + T`: Nueva pestaña
- `Cmd + W`: Cerrar pestaña
- `↑` / `↓`: Navegar por historial de comandos
- `Tab`: Autocompletar

## 💡 Tips

1. **Siempre activa el entorno virtual antes de trabajar**:
   ```bash
   source .venv/bin/activate
   ```

2. **Usa el script de inicio rápido**:
   ```bash
   ./inicio_rapido.sh
   ```

3. **Verifica regularmente**:
   ```bash
   ./verificar_entorno.sh
   ```

4. **Si algo falla, reinstala el paquete para ARM64**:
   ```bash
   pip uninstall -y paquete
   pip install --no-cache-dir paquete
   ```

5. **Mantén VS Code actualizado** para mejor compatibilidad con Apple Silicon

---

**Última actualización**: 30 de octubre de 2025
