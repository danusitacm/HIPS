from dotenv import load_dotenv
import os
from database_manager import DatabaseManager
load_dotenv()
def verify_hash_system_file():
    #verifica los hashes de los archivos /etc/shadow y /etc/passwd
    pass
def verify_hash_binary_file():
    #verifica los hashes de los archivos binarios
    pass
def generate_file_hash():
    #Asigna los hash para los archivos
    pass
def save_hash_to_database():
    #Guardo los hash en la base de datos
    pass
if __name__ == "__main__":
    db_manager = DatabaseManager(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )
    db_manager.connect()
    db_manager.disconnect()