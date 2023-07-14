from dotenv import load_dotenv
import hashlib
import os
from database_manager import DatabaseManager
load_dotenv()
def verify_hash_system_file():
    #verifica los hashes de los archivos /etc/shadow y /etc/passwd
    pass
def verify_hash_binary_file():
    #verifica los hashes de los archivos binarios
    pass
def generate_file_hash(file_path):
    try:
        with open(os.path.abspath(file_path), 'rb') as f:
            data = f.read()
            hashed_string = hashlib.sha256(data.encode('utf-8')).hexdigest()
        return hashed_string
    except Exception as error:
        print("Error al calcular el hash del archivo:", error)
        raise
def save_hash_to_database(db_manager):
    try:
        values=[]
        file_path=[]
        query_insert="INSERT INTO public.hash_record (file_name, hash_value) VALUES(%s,%s);"
        for root, files in os.walk("/bin", topdown=False):
            for name in files:
                file_path.append(os.path.join(root, name))
        file_path.append("/etc/shadow")
        file_path.append("/etc/passwd")
        print("Generando Hashes")
        for path in file_path:
            hash=generate_file_hash(path)
            values.append((path,hash))
        db_manager.executemany_query(query_insert,values)
    except Exception as error:
        print("Error al guardar en la base de datos.")
        raise
if __name__ == "__main__":
    print("hola xd")
    db_manager = DatabaseManager(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )
    db_manager.connect()
    save_hash_to_database(db_manager)
    db_manager.disconnect()