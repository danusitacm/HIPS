from django.shortcuts import render
from django.http import JsonResponse
from function.utils import execute_process, kill_process
from django.contrib.auth.decorators import login_required
from function.logs import *
# Create your views here.
@login_required
def high_consumed_resources(request):
    return render(request,"high_consumed_resources.html")
@login_required
def check_ram(request):
    """Funcion que verifica los procesos que consumen alto porcentaje de ram o si utilizan mucho tiempo la ram 

    Args:
        request La solicitud HTTP enviada por el usuario.

    Returns:
        Retorna la lista de procesos que consumen un 80% o se ejecuto ms de 3 minutos
    """
    pid_list=[]
    if request.method == 'POST':
        pid_list = request.POST.getlist('pid_list')
        if pid_list:
            for pid_process in pid_list:
                kill_process(pid_process)
            kill_process_message = f"Se detuvieron {len(pid_list)} procesos."
        else:
            kill_process_message = None
    else:
        kill_process_message = None           
    values=[]
    command="ps -eo pid,pmem,time,comm --sort=-pmem| head -n 20"
    process_info_list=execute_process(command)
    process_info_list.pop(0)
    for process in process_info_list:
        process=process.split()
        process_dicc={
            'processes_pid':process[0],
            'processes_pmem':process[1],
            'processes_time':process[2],
            'processes_comm':process[3],
        }
        if (process[2]>="00:03:00"  and not (process[0] in pid_list)):
            values.append(process_dicc)
            log_alarm("Consumo masivo de recursos", "", "Se detectó que un proceso se ejecutó durante un largo período de tiempo y utilizó una gran cantidad de memoria RAM.")
            log_prevention("Matar proceso", "", f"Se terminó el proceso de PID {process[0]} debido a que se ejecutó durante un tiempo prolongado y consumió muchos recursos.")
        if(process[1]>="80.0"  and not (process[0] in pid_list)):
            values.append(process_dicc)
            log_alarm("Consumo masivo de recursos","",f"Se detecto que un proceso tiene un porcentaje {process[1]} de uso alto en la memoria ram" )
            log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por el excesivo uso de la ram")
    return render(request,"check_ram.html",{
        'processes':values,
        'kill_process_message': kill_process_message,})
@login_required
def check_cpu(request):
    """Funcion que verifica los procesos que consumen alto porcentaje de cpu o si utilizan mucho tiempo la cpu 

    Args:
        request La solicitud HTTP enviada por el usuario.

    Returns:
        Retorna la lista de procesos que consumen un 80% o se ejecuto mas de 3 minutos
    """
    pid_list=[]
    if request.method == 'POST':
        pid_list = request.POST.getlist('pid_list')
        if pid_list:
            for pid_process in pid_list:
                kill_process(pid_process)
            kill_process_message = f"Se detuvieron {len(pid_list)} procesos."
        else:
            kill_process_message = None
    else:
        kill_process_message = None           
    values=[]
    command="ps -eo pid,pcpu,time,comm --sort=-pcpu| head -n 20"
    process_info_list=execute_process(command)
    process_info_list.pop(0)
    for process in process_info_list:
        process=process.split()
        process_dicc={
            'processes_pid':process[0],
            'processes_pcpu':process[1],
            'processes_time':process[2],
            'processes_comm':process[3],
        }
        if (process[2]>="00:03:00" and not (process[0] in pid_list)):
            values.append(process_dicc)
            log_alarm("Consumo masivo de recursos", "", "Se detectó que un proceso se ejecutó durante un largo período de tiempo y utilizó una gran cantidad CPU.")
            log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por ejecutarse en mucho tiempo")
        if(process[1]>="80.0" and not (process[0] in pid_list)):
            values.append(process_dicc)
            log_alarm("Consumo masivo de recursos","",f"Se detecto que un proceso tiene un porcentaje {process[1]} alto de uso de CPU." )
            log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por el excesivo uso de la CPU.")
    return render(request,"check_cpu.html",{
        'processes':values,
        'kill_process_message': kill_process_message,})