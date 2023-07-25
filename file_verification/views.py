import hashlib
from django.shortcuts import render, redirect
from . import models
from function.utils import get_files
from django.contrib.auth.decorators import login_required
import os,shutil
from function.logs import *
@login_required
def file_verification(request):
    return render(request,"file_verification.html")
@login_required  
def create_hashes(request):
    # Código para crear y guardar los hashes
    # Por ejemplo, asumiendo que tienes una lista de archivos a los cuales quieres generar hashes:
    files_to_hash = get_files('/bin')
    files_to_hash.append('/etc/passwd')
    files_to_hash.append('/etc/shadow')
    for file_name in files_to_hash:
        # Leer el contenido del archivo
        with open(file_name, 'rb') as file:
            file_contents = file.read()

        # Crear el hash MD5 del contenido del archivo
        hash_value=hashlib.sha256(file_contents).hexdigest()

        # Guardar el hash en la base de datos
        hash_record, created = models.HashRecord.objects.update_or_create(
            file_name=file_name,
            defaults={'hash_value': hash_value}
        )
    log_prevention("Creacion de hashes","","Se crearon hashes para los archivos binarios y de sistema.")
    success_message = 'Los hashes se han creado y guardado correctamente.'
    return render(request, 'create_hashes.html', {'success_message': success_message})

@login_required

def check_files(request):
    values=[]
    files_list= get_files('/bin')
    files_list.append('/etc/passwd')
    files_list.append('/etc/shadow')
    error_message=""
    for file_path in files_list:
        # Leer el contenido del archivo
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_contents = file.read()

            # Calcular el hash MD5 del contenido del archivo
            hash_value = hashlib.sha256(file_contents).hexdigest()

            # Verificar si el archivo está en la base de datos y si el hash ha cambiado
            hash_record = models.HashRecord.objects.get(file_name=file_path)
            if hash_value != hash_record.hash_value:
                # Si el hash ha cambiado, actualizar el registro en la base de datos
                file_dicc={
                    'file_path':hash_record.file_name,
                }
                log_alarm("File Verification Failure","",f"Se detecto que se modifico el archivo {hash_record.file_name}.")
                values.append(file_dicc)
    return render(request,"check_files.html",{'files_list': values})

@login_required
def create_backup(request):
    files_list = get_files('/bin')
    files_list.append('/etc/passwd')
    files_list.append('/etc/shadow')
    error_messages=""
    for file_path in files_list:
        if os.path.isfile(file_path):
            backup_file_path = "/hips/backup"
            try:
                shutil.copy(file_path, backup_file_path)
                
            except Exception as e:
                error_messages=f"Failed to create backup for. Error: {str(e)}"
    success_messages="Backup created successfully."
    log_prevention("BackUp realizado","","Se realizo un backup de los archivos /bin y los archivos del sistema /etc/passwd y /etc/shadow.")
    return render(request, 'create_backup.html', {'success_messages': success_messages,
                                                  'error_messages':error_messages,})