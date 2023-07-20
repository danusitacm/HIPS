from utils import execute_process, kill_process
import logs
def check_process_consum(resource):
    #process[0]=PID #process[1]=%USO #process[2]=TIEMPO_EJECUCION
    command=f"ps -eo pid,{resource},time --sort=-{resource}| head -n 20"
    process_info_list=execute_process(command)
    process_info_list.pop(0)
    if(resource=="rcpu"):
        "cpu"
    else:
        "mem "
    for process in process_info_list:
        process=process.split()
        if (process[2]>="00:30:00"):
            logs.log_alarm("Consumo masivo de recursos","",f"Se detecto que un proceso se ejecuto {process[2]}, se considera un tiempo excesivo")
            kill_process(process[1])
            logs.log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por ejecutarse en mucho tiempo")
        if(process[1]>="80.0"):
            logs.log_alarm("Consumo masivo de recursos","",f"Se detecto que un proceso tiene un porcentaje {process[2]} en el recurso { resource }" )
            kill_process(process[1])
            logs.log_prevention("Matar proceso","",f"Se mato el proceso de PID {process[0]} por el excesivo uso de la { resource }")
            
    
check_process_consum("pmem")
check_process_consum("pcpu")