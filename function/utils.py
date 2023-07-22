import hashlib
import os
from  function.logs import *
import subprocess

def get_files(path):
    # Obtener una lista de todos los archivos del bin
    try:
        file_paths = []
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_paths.append(os.path.join(root, name))
        return file_paths
    except Exception as error:
        print(f"Error al obtener los archivos del directorio {path}: {error}")

def generate_file_hash(file_path):
    try:
        with open(os.path.abspath(file_path), 'rb') as f:
            data = f.read()
            hashed_string = hashlib.sha256(data).hexdigest()
        return hashed_string
    except Exception as error:
        print(f"Error al calcular el hash del archivo '{file_path}': {error}")
        
def write_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text successfully written to {file_path}.")
    except Exception as e:
        print(f"Error writing to the file: {e}")
    
def execute_process(command):
    p=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,text=True,stderr=subprocess.PIPE)
    output, outerr =p.communicate()
    print(outerr)
    output=output.split("\n")
    output.pop()
    return output

def file_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        print(f"Error reading the file: {e}")
        return []
    
def search_string_in_file(file_path, search_string):
    matching_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if search_string in line.lower():
                    matching_lines.append(line.strip())
        return matching_lines
    except Exception as error:
        print("Ocurrió un error al leer el archivo: ",error) 

def kill_process(PID):
    try:
        subprocess.run(f"kill -9 {PID}", shell=True)
    except:
        print('An exception occurred')
        
def create_dictionary(dicc_struct,output_command):
    try:
        for word in output_command:
            for key in dicc_struct:
                    dicc_struct[key]=word           
        return dicc_struct 
    except Exception as error:
        print("Error al crear el diccionario: ",error)
    