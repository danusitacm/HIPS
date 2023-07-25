from django.shortcuts import render
from function.utils import execute_process, move_file_quarentine,search_string_in_file
from django.views.decorators.cache import never_cache
import subprocess
import os
import shutil
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def check_tmp_files(request):
        return render(request, "tmp_directory_check.html")

@login_required
def check_tmp_extension(request):
        print("ACA ESTA EL REQUEST",request)
        values=[]
        extension_list=[".cpp", ".c", ".exe", ".sh", ".php", ".py"]
        if request.method == 'POST':
                quarantine_files = request.POST.getlist('quarantine_files')
                for file_name in quarantine_files:
                        file_path = os.path.join('/tmp', file_name)
                        move_file_quarentine(file_path)
                        print(f"El archivo {file_name} fue puesto en cuarentena: /hips/cuarentena")
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
        return render(request, "check_tmp_extension.html", {
        'sussy_files': values,
        'quarantined_message': quarantined_message,
        })
@login_required
def check_tmp_script(request):

        command="find /tmp -type f"
        values=[]
        if request.method == 'POST':
                quarantine_files = request.POST.getlist('quarantine_files')
                for file_name in quarantine_files:
                        file_path = os.path.join('/tmp', file_name)
                        move_file_quarentine(file_path)
                        print(f"El archivo {file_name} fue puesto en cuarentena: /hips/cuarentena")
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
                        print(f"Se encontro que en el archivo {file} con la linea inicial #!.")
                        scripts={
                                'file_name':file,
                        }
                        values.append(scripts)
        return render(request, "check_tmp_script.html", {
        'scripts': values,
        'quarantined_message': quarantined_message,
        })
