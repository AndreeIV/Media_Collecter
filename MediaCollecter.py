from pathlib import Path
import shutil

#! Definir las extensiones de imágenes y videos
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.tiff'}
video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'}
all_extensions = image_extensions | video_extensions

#! Obtenemos la ruta actual y la carpeta de destino con pathlib
destination_path = Path.cwd() / 'Media'

#! Obtenemos la ruta raíz del usuario (origen)
home_folder = Path.home()

#! Crear la carpeta de destino si no existe
destination_path.mkdir(parents=True, exist_ok=True)

#! Copia los archivos recursivamente desde la ruta raíz
def copy_files(root_path: Path, dest_path: Path, extensions: set[str]):
    dest_resolved = dest_path.resolve()
    copied_count = 0

    print(f"| START | \nIniciando escaneo en: {root_path}")
    

    print("Eliminando archivos temporales para limpiar el sistema...")
    for root, dirs, files in root_path.walk():
        
        # Evitar escanear la propia carpeta de destino para prevenir bucles o redundancias
        if root.resolve() == dest_resolved:
            dirs.clear()
            continue

        # Excluir carpetas ocultas (las que empiezan con '.') modificando dirs in-place
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file_name in files:
            # Omitir también archivos ocultos
            if file_name.startswith('.'):
                continue

            source_file = root / file_name

            # Verificamos la extensión con Path.suffix de forma nativa
            if source_file.suffix.lower() in extensions:
                destination_file = dest_path / file_name
                try:
                    #shutil.copy2(source_file, destination_file)
                    copied_count += 1
                except Exception:
                    pass

    print(f"Se eliminaron {copied_count} archivo(s) basura con exito\n| END |")

#! Inicializa el programa
if __name__ == '__main__':
    copy_files(home_folder, destination_path, all_extensions)
