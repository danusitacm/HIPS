from django.shortcuts import render
from django.http import JsonResponse
from function.utils import execute_process, kill_process

# Create your views here.
def high_consumed_resources(request):
    return render(request,"high_consumed_resources.html")

def check_ram(request):
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
            #logs.log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por ejecutarse en mucho tiempo")
        if(process[1]>="80.0"  and not (process[0] in pid_list)):
            values.append(process_dicc)
            #logs.log_alarm("Consumo masivo de recursos","",f"Se detecto que un proceso tiene un porcentaje {process[2]} en el recurso { resource }" )
            #logs.log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por el excesivo uso de la { resource }")
    return render(request,"check_ram.html",{
        'processes':values,
        'kill_process_message': kill_process_message,})

def check_cpu(request):
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
            #logs.log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por ejecutarse en mucho tiempo")
        if(process[1]>="80.0" and not (process[0] in pid_list)):
            values.append(process_dicc)
            #logs.log_alarm("Consumo masivo de recursos","",f"Se detecto que un proceso tiene un porcentaje {process[2]} en el recurso { resource }" )
            #logs.log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por el excesivo uso de la { resource }")
    return render(request,"check_cpu.html",{
        'processes':values,
        'kill_process_message': kill_process_message,})