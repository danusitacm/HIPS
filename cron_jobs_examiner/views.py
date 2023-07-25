from django.shortcuts import render
from function.utils import execute_process
from django.contrib.auth.decorators import login_required
from function.logs import *
@login_required
def check_user_cron(request):
    command_getuser="cat /etc/passwd | awk -F : '{print $1}'"
    list_user=execute_process(command_getuser)
    list_user.pop(0)
    values=[]
    if(list_user):
        for user in list_user:
            command_crontab=f"crontab -u {user} -l"
            list_cron=execute_process(command_crontab)
            if not("no crontab for" in list_cron):
                for cron in list_cron:
                    cron=cron.split()
                    cron_dicc={
                        'cron_user':cron[5],
                        'cron_file':cron[6],
                    }   
                    values.append(cron_dicc)
                    log_alarm(f"Archivo cron","",f"Se detecto que el user {user} esta ejecutando el archivo {cron[6]} como cron.")

        return render(request, "cron_verification.html", {'crons': values})
    else:
        message = "No se encontraron usuarios conectados en este momento."
        return render(request, "cron_verification.html.html", {'message': message})