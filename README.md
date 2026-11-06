# 📸 Media Collecter

Una herramienta ligera, eficiente y multiplataforma en Python para **buscar, recolectar y centralizar de forma recursiva archivos multimedia** (imágenes y videos) desde tu directorio de usuario hacia una carpeta organizada localmente.

---

## 🚀 Características

- **🔍 Escaneo Recursivo Rápido:** Utiliza `pathlib.Path.walk()` para explorar directorios a fondo de manera nativa.
- **🛡️ Exclusión de Archivos y Carpetas Ocultas:** Omite automáticamente directorios de configuración y caché (`.git`, `.cache`, `.config`, etc.) y archivos ocultos, optimizando drasticamente la velocidad del escaneo.
- **🔄 Protección contra Bucles:** Si la carpeta de destino (`Media/`) se encuentra dentro de la ruta que se está escaneando, el script la detecta y la omite automáticamente para no re-copiar archivos.
- **🕒 Preservación de Metadatos:** Utiliza `shutil.copy2()`, conservando las fechas originales de creación, modificación y metadatos de las fotos/videos.
- **📦 Cero Dependencias Externas:** Funciona únicamente con la biblioteca estándar de Python (no necesitas instalar paquetes con `pip`).
- **💻 Multiplataforma:** Compatible con Linux, macOS y Windows.

---

## 📂 Formatos Soportados

| Tipo | Extensiones |
| :--- | :--- |
| **Imágenes** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| **Videos** | `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.wmv`, `.webm` |

*(La verificación no distingue entre mayúsculas y minúsculas: detecta tanto `.jpg` como `.JPG`).*

---

## 📋 Requisitos

- **Python 3.12** o superior (recomendado para soporte nativo de `Path.walk()`).

Para verificar tu versión actual de Python:

```bash
python3 --version
```

---

## 🛠️ Instalación y Configuración

1. **Clonar o descargar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/Media_Collecter.git
   cd Media_Collecter
   ```

2. No es necesario crear un entorno virtual ni instalar dependencias adicionales.

---

## 📖 Manual de Uso

### 1. Ejecutar el script

Para iniciar el proceso de recolección, simplemente ejecuta:

```bash
python3 MediaCollecter.py
```

En Windows:
```cmd
python MediaCollecter.py
```

### 2. ¿Qué hace el programa al ejecutarse?

1. **Crea la carpeta de destino:** Si no existe, genera automáticamente la carpeta `Media/` dentro del directorio donde estás ejecutando el script.
2. **Escanea tu carpeta de usuario:** Comienza a buscar en `~` (por ejemplo `/home/usuario` en Linux o `C:\Users\Usuario` en Windows).
3. **Filtra y copia:** Copia cada imagen o video encontrado a la carpeta `Media/`.
4. **Resumen:** Al finalizar, muestra en la terminal la cantidad total de archivos copiados con éxito.

#### Ejemplo de salida en consola:

```text
Iniciando escaneo en: /home/andreeiv
Carpeta de destino: /home/andreeiv/Projects/Media_Collecter/Media
Copia completada. Se copiaron 142 archivo(s).
```

---

## ⚙️ Personalización

Puedes editar fácilmente [`MediaCollecter.py`](MediaCollecter.py) para adaptarlo a tus necesidades:

### Cambiar la carpeta de origen
Si solo quieres escanear una carpeta específica (por ejemplo `Descargas` o `Documentos` en lugar de todo tu usuario):

```python
# En lugar de Path.home():
home_folder = Path.home() / 'Downloads'
```

### Agregar nuevas extensiones
Simplemente añade la extensión deseada a los conjuntos correspondientes:

```python
# Ejemplo: agregar formato RAW o WebP
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.raw'}
```

---

## ⚠️ Consideraciones

- **Archivos con el mismo nombre:** Si existen dos archivos con el mismo nombre en diferentes carpetas (por ejemplo `Descargas/foto.jpg` y `Documentos/foto.jpg`), el último sobreescribirá al anterior en la carpeta `Media/`.
- **Permisos del sistema:** Los archivos o carpetas que requieran permisos de administrador/superusuario serán omitidos de forma silenciosa para que el proceso no se interrumpa.
