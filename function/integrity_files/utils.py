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

def generate_file_hash(file_path):
    try:
        with open(os.path.abspath(file_path), 'rb') as f:
            data = f.read()
            hashed_string = hashlib.sha256(data).hexdigest()
        return hashed_string
    except Exception as error:
        print(f"Error al calcular el hash del archivo '{file_path}': {error}")