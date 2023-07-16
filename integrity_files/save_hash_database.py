from utils import *

def save_hash(db_manager):
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