from utils import *
import shutil

def make_backup_binary_files(source_files, destination_folder):
    try:
        
        print(source_files)
        for file_path in source_files:
            if not os.path.exists(file_path):
                shutil.copy(file_path, destination_folder)
        print(f"Se realizo correctamente el backup")
    except Exception as error:
        print(f"Error al realizar el backup de los archivos binarios : {error}")

def make_backup_system_files(source_files, destination_folder):
    try:
        for file_path in source_files:
            if os.path.exists(file_path):
                shutil.copy(file_path, destination_folder)
        print(f"Se realizo correctamente el backup")
    except Exception as error:
        print(f"Error al realizar el backup de los archivos del sistema: {error}")

def restore_backup_binary_files(source_files, destination_folder):
    try:
        pass
    except Exception as error:
        print(f"Error al restaurar el backup de los archivos binarios: {error}")


def restore_backup_system_files(source_files, destination_folder):
    try:
        for file_path in source_files:
           shutil.copy(file_path, destination_folder) 
    except Exception as error:
        print(f"Error al restaurar el backup de los archivos del sistema: {error}")
        

""" source_files=get_files('/bin')
destination_folder = "/hips/backup/binary_files"
make_backup_binary_files(source_files, destination_folder) """
""" source_files=["/etc/passwd","/etc/shadow"]
destination_folder = "/hips/backup/system_file"
make_backup_system_files(source_files, destination_folder) """
source_files=get_files("/hips/backup/system_files/")
destination_folder = "/etc"
restore_backup_system_files(source_files,destination_folder)
