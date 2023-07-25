import hashlib
from django.shortcuts import render, redirect
from . import models
from function.utils import get_files
# Create your views here.
def file_verification(request):
    return render(request,"file_verification.html")
    
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
    success_message = 'Los hashes se han creado y guardado correctamente.'
    return render(request, 'create_hashes.html', {'success_message': success_message})

def check_files(request):
    values=[]
    files_list= get_files('/bin')
    files_list.append('/etc/passwd')
    files_list.append('/etc/shadow')
    for file_path in files_list:
        # Leer el contenido del archivo
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
            values.append(file_dicc)
    return render(request,"check_files.html",{'files_list': values})