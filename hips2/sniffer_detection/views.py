from django.shortcuts import render
import subprocess
from function.utils import execute_process
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def sniffer_detection(request):
    return render(request, "sniffer_verification.html")
# ------------------- CHECK SNIFFER ------------------------------------------------
def get_sniffer_processes(tool_name):
    try:
        command = "sudo ps -uax | grep "+tool_name+" | grep -v grep | awk \'{print $1\" \"$2\" \"$11\"\"$12}\'"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, text=True)
        output = process.communicate()[0].split("\n")
        output.pop()
        return output
    except Exception as error:
        print("Error al ejecutar el comando ps: ", error)
@login_required   
def check_sniffer(request):
    try:
        values=[]
        packet_capture_tools = [
            "tcpdump",
            "wireshark",
            "tshark",
            "ngrep",
            "netsniff-ng",
            "dumpcap",
            "ettercap",
            "nmap",
            "nethogs",
            "netstat"
        ]
        for tool in packet_capture_tools:
            result_ps = get_sniffer_processes(tool)
            if result_ps:
                for process in result_ps:
                    process = process.split()
                    sniffer_dicc={
                        'sniffer_user':process[0],
                        'sniffer_pid':process[1],
                        'sniffer_command':process[2]
                    }
                    values.append(sniffer_dicc)
                    print("Sniffer activado","",f"El proceso {process[1]} fue activado por el user {process[0]}")
                    subprocess.run(f"kill -9 {process[1]}", shell=True)
                    print("Proceso desactivado","",f"El proceso {process[1]} se encuentra en la lista negra, fue desactivado por esta razon.")
        if values:
            return render(request, "check_sniffer_temp.html", {'sniffers': values})
        else: 
            message = "No se encontraron sniffers ejecutandose."
            return render(request, "check_sniffer_temp.html", {'message': message})
    except Exception as error:
        print("No se puede verificar si hay un sniffer: ", error)
    
# --------------------------- CHECK PROMISCUO -------------------------------------------

def check_net_interface(interface_name):
    command_interface=f"ip a show {interface_name} | grep -i promisc"
    ps=subprocess.Popen(command_interface,shell=True,stdout=subprocess.PIPE,text=True)
    output=ps.communicate()[0]
    if (output):
        return 1
    else:
        return 0
@login_required
def check_promiscuous(request):     
    command="grep -i \"entered promiscuous mode\" /var/log/messages | awk '{print $7}'"
    interface_list=execute_process(command)
    interface_list=list(set(interface_list))
    interface_status={
        'interface_name':'',
        'interface_status':'',
    }
    values=[]
    if(interface_list):
        for name in interface_list:
            if(check_net_interface(name)):
                print(f"La interface {name} se encuentra en modo promiscuo.")
                print("Interfaz modo promiscuo","",f"La interface {name} se encuentra en modo promiscuo.")
                subprocess.run(f"ifconfig {name} -promisc", shell=True, check=True)
                print("Modo promiscuo desactivado","",f"Se desactivo la interfaz {name} del modo promiscuo por medida de seguridad.")
                print(f"Se desactivo la interfaz {name} del modo promiscuo por medida de seguridad.")
                interface_status={
                    'interface_name':name,
                    'interface_status':'promiscuo',
                }
            else: 
                print("La interfaz: "+name+" no se encuentra en modo promiscuo ")
                interface_status={
                    'interface_name':name,
                    'interface_status':'no promiscuo',
                }
            values.append(interface_status)
        return render(request,"check_promisc_temp.html",{'interface_status':values})
    else:
        message = "El dispositivo se encuentra en modo promiscuo."
        return render(request,"check_promisc_temp.html", {'message': message})