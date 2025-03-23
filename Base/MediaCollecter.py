import os
import shutil

#! Definir las extensiones de imágenes y videos
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm']
all_extensions = image_extensions + video_extensions

#! Formatea la ruta a un estandar.
def formatRuta(ruta):
    newHome = ''

    for a in ruta:
        if a == '\\':
            newHome = newHome + '/'
        else :
            newHome = newHome + a
        
    return newHome

#! Obtenemos la ruta actual desde la ejecución del programa.
rutaActual = os.path.abspath(os.getcwd());
rutaActualFormat = formatRuta(rutaActual); 
destination_path = rutaActualFormat + '/Media';

#! Obtenemos la ruta de destino.
home_folder = os.path.expanduser('~')
newHomeFormat = formatRuta(home_folder) + '/';  #?  C:/Users/HP/

#! Crear la carpeta de destino si no existe.
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

#! Copia los archivos recursivamente desde la ruta raíz.
def copy_files(root_path, destination_path, extensions):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):

                source_file = os.path.join(root, file) #? Ruta completa del archivo a descargar.
                destination_file = os.path.join(destination_path, file) #? Ruta donde se descargarán los archivos.
                try:
                    shutil.copy2(source_file, destination_file)
                except Exception as e:
                    pass;

#! Inicializa el programa
copy_files(newHomeFormat, destination_path, all_extensions)