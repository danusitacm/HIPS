from utils import *
import shutil

def make_backup(source_files, destination_folder):
    try:
        print(source_files)
        for file_path in source_files:
            if not os.path.exists(file_path):
                shutil.copy(file_path, destination_folder)
        print(f"Se realizo correctamente el backup")
    except Exception as error:
        print(f"Error al realizar el backup: {error}")

source_files=get_files('/bin')
destination_folder = "/hips/backup"
make_backup(source_files, destination_folder)