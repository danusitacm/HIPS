from dotenv import load_dotenv
import hashlib
import os
from  database_manager import *
from  logs import *
load_dotenv()

db_manager = DatabaseManager(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
    )

def get_files(path):
    # Obtener una lista de todos los archivos del bin
    try:
        file_paths = []
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_paths.append(os.path.join(root, name))
        file_paths.append("/etc/shadow")
        file_paths.append("/etc/passwd")
        return file_paths
    except Exception as error:
        print(f"Error al obtener los archivos del directorio '{path}': {error}")

def generate_file_hash(file_path):
    try:
        with open(os.path.abspath(file_path), 'rb') as f:
            data = f.read()
            hashed_string = hashlib.sha256(data).hexdigest()
        return hashed_string
    except Exception as error:
        print(f"Error al calcular el hash del archivo '{file_path}': {error}")