import os
import shutil

# Ruta donde se va a organizar los archivos.
path = 'C:/Users/Desktop/OS'

# Lista de las extensiones de los archivos que queremos organizar.
fotos_extensions =  [".png", ".jpg", ".jpeg", ".gif", ".ico", ".bmp"]
videos_extensions = [".mp4", ".flv", ".avi",  ".mkv", ".wmv", ".mov"]
audio_extensions =  [".mp3", ".wav", ".wma",  ".mp4", ".flac"]
text_extensions = [".ppt", ".pptx", ".xlsx", ".xlsm", ".docx", ".pdf"]
executable_extensions = [".exe", ".msi"]

# Función para orgarnizar los archivos.
def move_file(archivo, extensions):
    for i in fotos_extensions:
        if extensions == i:
            shutil.move(f"{path}/{archivo}", path + '/' + "fotos")
    
    for i in videos_extensions:
        if extensions == i:
            shutil.move(f"{path}/{archivo}", path + '/' + "videos")

    for i in audio_extensions:
        if extensions == i:
            shutil.move(f"{path}/{archivo}", path + '/' + "musica")

    for i in text_extensions:
        if extensions == i:
            shutil.move(f"{path}/{archivo}", path + '/' + "office")

    for i in executable_extensions:
        if extensions == i:
            shutil.move(f"{path}/{archivo}", path + '/' + "program")


def main():
    print("Iniciando Movimiento De Los Archivos...")
    for archivo in os.listdir(path):
        nombre_archivo, extensions = os.path.splitext(archivo)
        move_file(archivo, extensions)

    print("\nProceso Terminado")


if __name__ == "__main__":
    main()

