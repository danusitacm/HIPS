from utils import *

def verify_hash_file(path, db_manager):
    # Verifica los hash de un archivo determinado.
    try:
        query_select = f"SELECT hash_value FROM hash_record WHERE file_name='{path}'"
        if os.path.exists(path):
            actual_hash = generate_file_hash(path)
            old_hash = db_manager.select_from_table(query_select)
            if actual_hash != old_hash[0][0]:
                print(f"El archivo '{path}' ha sido modificado.")
                log_alarm(f"Archivo modificado","",f"El archivo '{path}' ha sido modificado, el hash actual no coincide con el antiguo.")
        else:
            raise ValueError(f"La dirección '{path}' no es válida.")
    except Exception as error:
        print(f"Error al verificar el archivo '{path}': {error}")

# Código de ejemplo para ejecutar las funciones
db_manager.connect()
# save_hash_to_database(db_manager)
verify_hash_file('/home/danusita/prueba/prueba.txt', db_manager)
db_manager.disconnect()