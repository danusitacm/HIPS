from django.shortcuts import render
import os
from function.utils import execute_process
from django.contrib.auth.decorators import login_required
from function.logs import *

@login_required
def log_examiner(request):
    return render(request,"log_examiner.html")

def block_ip(ip):
    """Funcion que bloquea ip

    Args:
        ip : direccion de ip a bloquear
    """
    command=f"route add -host {ip} reject"
    execute_process(command)

@login_required
def check_error_404(request):
    """Funcion que verifica los errores de acceso a una pagina web e identifica si una ip se repitio mas de 3 veces 

    Args:
        request : La solicitud HTTP enviada por el usuario.

    Returns:
        Retorna las ip que se repitieron mas de 3 veces en el log y luego las bloquea
    """
    values=[]
    command="cat /var/log/httpd/acces.log | grep \"404\" | awk '{print $1}'"
    ip_list=execute_process(command)
    if(ip_list):
        ip_list=list(set(ip_list))
        for ip in ip_list: 
            commanda_2=f"cat /var/log/httpd/acces.log | grep -c {ip}"
            repeate_attemps=execute_process(commanda_2)
            repeate_attemps=repeate_attemps[0]
            if (int(repeate_attemps)>3):
                ip_amongus={
                    'ip_intruser':ip,
                    'attemps':repeate_attemps,
                }
                values.append(ip_amongus)
                log_alarm("ERROR 404 repetitivos","",f"Se detecto que la ip {ip} intento muchas veces acceder a la pagina.")
                block_ip(ip)
                log_prevention("Se bloqueo la ip","",f"Se bloqueo la ip {ip} por actuar de forma sospechosa.")
    return render(request,"check_error_404.html",{'sussy_ip':values})

