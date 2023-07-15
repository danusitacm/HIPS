from dotenv import load_dotenv
import hashlib
import os
from database_manager import DatabaseManager
import logs
load_dotenv()
db_manager = DatabaseManager(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
    )

def get_files(path):
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

def verify_hash_file(path, db_manager):
    try:
        query_select = f"SELECT hash_value FROM hash_record WHERE file_name='{path}'"
        if os.path.exists(path):
            actual_hash = generate_file_hash(path)
            old_hash = db_manager.select_from_table(query_select)
            if actual_hash != old_hash[0][0]:
                print(f"El archivo '{path}' ha sido modificado.")
                logs.log_alarm(f"Archivo modificado","",f"El archivo '{path}' ha sido modificado, el hash actual no coincide con el antiguo.")
        else:
            raise ValueError(f"La dirección '{path}' no es válida.")
    except Exception as error:
        print(f"Error al verificar el archivo '{path}': {error}")

def save_hash_to_database(db_manager):
    try:
        values = []
        file_paths = []
        query_insert = "INSERT INTO public.hash_record (file_path, hash_value) VALUES (%s, %s);"
        file_paths = get_files('/bin')
        for path in file_paths:
            file_hash = generate_file_hash(path)
            values.append((path, file_hash))
        db_manager.executemany_query(query_insert, values)
    except Exception as error:
        print("Error al guardar los hashes en la base de datos:", error)

# Código de ejemplo para ejecutar las funciones
db_manager.connect()
# save_hash_to_database(db_manager)
verify_hash_file('/home/danusita/prueba/prueba.txt', db_manager)
db_manager.disconnect()