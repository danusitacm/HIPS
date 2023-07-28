from django.shortcuts import render
from function.utils import execute_process, move_file_quarentine,search_string_in_file
from django.views.decorators.cache import never_cache
import subprocess
import os
import shutil
from django.contrib.auth.decorators import login_required
from function.logs import *
@login_required
# Create your views here.
def check_tmp_files(request):
        return render(request, "tmp_directory_check.html")

@login_required
def check_tmp_extension(request):
        """
        Verifica y pone en cuarentena archivos con extensiones no permitidas en el directorio /tmp.

        Args:
                request: La solicitud HTTP enviada por el usuario.

        Returns:
                Renderiza la página web "check_tmp_extension.html" con la información de los archivos sospechosos y un mensaje de cuarentena.
        """
        print("ACA ESTA EL REQUEST",request)
        values=[]
        extension_list=[".cpp", ".c", ".exe", ".sh", ".php", ".py"]
        if request.method == 'POST':
                quarantine_files = request.POST.getlist('quarantine_files')
                for file_name in quarantine_files:
                        file_path = os.path.join('/tmp', file_name)
                        move_file_quarentine(file_path)
                        log_prevention("Archivo Cuarentena","",f"El archivo {file_name} fue puesto en cuarentena: /hips/cuarentena por tener extensiones no permitidas")
                if quarantine_files:
                        quarantined_message = f"Se enviaron {len(quarantine_files)} archivo(s) a cuarentena."
                else:
                        quarantined_message = None
        else:
                quarantined_message = None
        
        for extension in extension_list:
                command=f"find /tmp -type f -name \"*{extension}\" | grep -v /tmp/pyright "
                output=execute_process(command)
                if(output):
                        for sussy_file in output:
                                file_dicc={
                                        'file_name':sussy_file
                                }
                                values.append(file_dicc) 
                                log_alarm("Archivo de extension prohibida","",f"Se encontro que en el archivo {sussy_file} con una extension prohibida en /tmp {extension}.")
        return render(request, "check_tmp_extension.html", {
        'sussy_files': values,
        'quarantined_message': quarantined_message,
        })
@login_required
def check_tmp_script(request):
        """
        Verifica y pone en cuarentena archivos de script presentes en el directorio /tmp.

        Args:
                request: La solicitud HTTP enviada por el usuario.

        Returns:
                Renderiza la página web "check_tmp_script.html" con la información de los archivos de script sospechosos y un mensaje de cuarentena.
        """
        command="find /tmp -type f"
        values=[]
        if request.method == 'POST':
                quarantine_files = request.POST.getlist('quarantine_files')
                for file_name in quarantine_files:
                        file_path = os.path.join('/tmp', file_name)
                        move_file_quarentine(file_path)
                        log_prevention("Archivo Cuarentena","",f"El archivo {file_name} fue puesto en cuarentena: /hips/cuarentena por ser un script ")
                if quarantine_files:
                        quarantined_message = f"Se enviaron {len(quarantine_files)} archivo(s) a cuarentena."
                else:
                        quarantined_message = None
        else:
                quarantined_message = None
        file_list=execute_process(command)  
        if(file_list):
            for file in file_list:
                if(search_string_in_file(f"{file}","#!")):
                        scripts={
                                'file_name':file,
                        }
                        log_alarm("Archivo Script en TMP","",f"Se encontro que en el archivo {file} con la linea inicial #!.")
                        values.append(scripts)
        return render(request, "check_tmp_script.html", {
        'scripts': values,
        'quarantined_message': quarantined_message,
        })
