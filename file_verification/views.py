import hashlib
from django.shortcuts import render, redirect
from . import models
from function.utils import get_files
from django.contrib.auth.decorators import login_required
import os,shutil
from function.logs import *
@login_required
def file_verification(request):
    """Función que muestra la página de opciones para la verificación de la integridad de archivos.
    Args:
        request : La solicitud HTTP enviada por el usuario.
    Returns:
        Una página web que permite al usuario realizar la verificación de archivos.
    """
    return render(request,"file_verification.html")

@login_required  
def create_hashes(request):
    """Funcion que genera hashes a los archivos binarios y del sistema para poder almacenarlos en una base de datos
    Args:
        request: La solicitud HTTP enviada por el usuario.
    Returns:
       Retorna un mensaje de confirmación para el usuario de que se crearon y guardaron los hashes en la base de datos.
    """
    #Obtenemos la lista de archivos
    files_to_hash = get_files('/bin')
    files_to_hash.append('/etc/passwd')
    files_to_hash.append('/etc/shadow')
    for file_name in files_to_hash:
        #Recorremos la lista de los archivos y abrimos para leer su contenido
        if os.path.isfile(file_name):
            with open(file_name, 'rb') as file:
                file_contents = file.read()

            # Crear el hash sha256 del contenido del archivo
            hash_value=hashlib.sha256(file_contents).hexdigest()

            # Guardar el hash en la base de datos
            hash_record, created = models.HashRecord.objects.update_or_create(
                file_name=file_name,
                defaults={'hash_value': hash_value}
            )
    #Se manda un registro al log prevencion.log de la medida preventiva que se tomo 
    log_prevention("Creacion de hashes","","Se crearon hashes para los archivos binarios y de sistema.")
    #Se crea el mensaje de confirmacion de la operacion exitosa
    success_message = 'Los hashes se han creado y guardado correctamente.'
    #Se envia a la pagina para que el usuario pueda verla
    return render(request, 'create_hashes.html', {'success_message': success_message})

@login_required

def check_files(request):
    """Funcion que verifica si se produjo modificacion en los archivos binarios y del sistema por comparacion de hashes

    Args:
        request : La solicitud HTTP enviada por el usuario.

    Returns:
        Retorna la lista de archivos modificados a la pagina web para que el usuario pueda verla.
    """
    # Obtenemos la lista de los path de los archivos.
    values=[]
    files_list= get_files('/bin')
    files_list.append('/etc/passwd')
    files_list.append('/etc/shadow')
    
    error_message=""
    # Recorremos la lista de archivos
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
                # Creamos un diccionario para guardar los datos que queremos enviar a la pagina web
                file_dicc={
                    'file_path':hash_record.file_name,
                }
                #Se manda un registro al log prevencion.log de la medida preventiva que se tomo 
                log_alarm("File Verification Failure","",f"Se detecto que se modifico el archivo {hash_record.file_name}.")
                values.append(file_dicc)
    # Retorna a la pagina web los datos a ser visualizados.
    return render(request,"check_files.html",{'files_list': values})

@login_required
def create_backup(request):
    """Funcion que crea un backup de los archivos binarios y del sistema.

    Args:
        request : La solicitud HTTP enviada por el usuario.

    Returns:
        Si se creo de forma exitosa el backup se manda un mensaje de que se creo de forma exitosa el backup
        Si no se creo de forma exitosa el backup se manda un mensaje de alerta para advertir al usaurio
    """
    # Obtenemos la lista de los path de los archivos.
    files_list = get_files('/bin')
    files_list.append('/etc/passwd')
    files_list.append('/etc/shadow')
    error_messages=""
     # Recorremos la lista de archivos
    for file_path in files_list:
        # Verificamos si es un archivo la direccion
        if os.path.isfile(file_path):
            backup_file_path = "/hips/backup"
            try:
                # copiamos el archivo 
                shutil.copy(file_path, backup_file_path)
                
            except Exception as e:
                # creamos el mensaje de error si es que ocudrre un error
                error_messages=f"Failed to create backup for. Error: {str(e)}"
     # Creamos un mensaje de confirmacion

    success_messages="Backup created successfully."
    #Se manda un registro al log prevencion.log de la medida preventiva que se tomo 
    log_prevention("BackUp realizado","","Se realizo un backup de los archivos /bin y los archivos del sistema /etc/passwd y /etc/shadow.")
    return render(request, 'create_backup.html', {'success_messages': success_messages,
                                                  'error_messages':error_messages,})