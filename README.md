# 📸 Media Collecter

Una herramienta ligera, eficiente y multiplataforma en Python para **buscar, recolectar y centralizar de forma recursiva archivos multimedia** (imágenes y videos) desde tu directorio de usuario hacia una carpeta organizada localmente.

---

## 🚀 Características

- **🔍 Escaneo Recursivo Rápido:** Utiliza `pathlib.Path.walk()` para explorar directorios a fondo de manera nativa.
- **📁 Jerarquía Aplanada y Organizada:** Organiza por usuario (`Media/<usuario>/`) y ubica todas las subcarpetas con contenido multimedia en un solo nivel descriptivo (ej. `Vacaciones - Playa`), sin anidaciones profundas innecesarias.
- **🛡️ Cero Duplicidad o Pérdida de Datos:** Preserva el contexto de origen mediante nombres referenciados y maneja colisiones de archivos automáticamente agregando sufijos incrementales (`foto_1.jpg`).
- **🚫 Exclusión de Archivos y Carpetas Ocultas:** Omite automáticamente directorios de configuración y caché (`.git`, `.cache`, `.config`, etc.) y archivos ocultos, optimizando al máximo la velocidad del escaneo.
- **🔄 Protección contra Bucles:** Si la carpeta de destino (`Media/`) se encuentra dentro de la ruta que se está escaneando, el script la detecta y la omite automáticamente para no re-copiar archivos.
- **🕒 Preservación de Metadatos:** Utiliza `shutil.copy2()`, conservando las fechas originales de creación, modificación y metadatos de las fotos/videos.
- **📦 Cero Dependencias Externas:** Funciona únicamente con la biblioteca estándar de Python (no necesitas instalar paquetes con `pip`).
- **💻 Multiplataforma:** Compatible con Linux, macOS y Windows.

---

## 📁 Estructura de Organización

El script organiza los archivos de forma limpia dentro de `Media/` utilizando una **jerarquía aplanada por usuario**:

```text
Media/
└── <usuario>/
    ├── foto_raiz.png                 <-- Archivos sueltos en el directorio del usuario
    ├── Descargas/                    <-- Carpetas directas
    │   └── video1.mp4
    ├── Viaje2024 - playa/            <-- Subcarpetas anidadas aplanadas con su referencia
    │   └── foto_playa.jpg
    └── Proyectos - App - assets/
        └── logo.png
```

- **Sin anidaciones innecesarias:** No tendrás que navegar a través de múltiples niveles de carpetas para llegar a tus archivos.
- **Contexto preservado:** Si una foto estaba en `Viaje2024/playa/`, la carpeta resultante se llama `Viaje2024 - playa/`, evitando confusiones y manteniendo claro su origen.
- **Solo carpetas con contenido:** Si un directorio no contiene imágenes ni videos, no se creará en el destino.

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

1. **Crea la carpeta de destino:** Si no existe, genera la carpeta `Media/<tu_usuario>/` dentro del directorio donde estás ejecutando el script.
2. **Escanea tu carpeta de usuario:** Comienza a buscar en `~` (por ejemplo `/home/usuario` en Linux o `C:\Users\Usuario` en Windows), ignorando carpetas ocultas.
3. **Filtra, organiza y copia:** Crea las carpetas aplanadas correspondientes y copia cada imagen o video encontrado.
4. **Resumen:** Al finalizar, muestra en la terminal la cantidad total de archivos copiados con éxito.

#### Ejemplo de salida en consola:

```text
Iniciando escaneo en: /home/andreeiv
Carpeta central de destino: /home/andreeiv/Projects/Media_Collecter/Media
Carpeta del usuario: /home/andreeiv/Projects/Media_Collecter/Media/andreeiv
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

- **Permisos del sistema:** Los archivos o carpetas que requieran permisos de administrador/superusuario serán omitidos de forma silenciosa para que el proceso no se interrumpa.
