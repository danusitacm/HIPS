import subprocess
from pathlib import Path
import os
def create_files(path_list):
    try:
        for path in path_list:
            if not os.path.exists(path):
                subprocess.run(["mkdir","path"])
            else:
                print(f"El archivo {path} ya fue creado.")
    except Exception as error:
        print(f"Error al crear el archivo: {error}")

path_list_log=["/var/log/hips","/var/log/hips/alarmas.log"]
path_list_hips=["/hips","/hips/ip_detected","/var/log/hips","/hips/backup","/hips/backup/system_file","/hips/backup/binary_file","/hips/cuarentena"]

create_files(path_list_log)
create_files(path_list_hips)

