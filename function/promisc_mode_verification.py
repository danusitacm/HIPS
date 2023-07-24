import subprocess
import re
from utils import search_string_in_file

def extract_interface(log_line):
    pattern = r'device (\w+) entered promiscuous mode'
    match = re.search(pattern, log_line)
    if match:
        interface_name = match.group(1)       
    return interface_name

def check_promiscuos_mode():
    # Se verifica si el dispositivo esta en modo promiscuo con los archivos de auditoria
    # Y con el resultado de ip a 
    try:
        file_path="/var/log/messages"
        string ="entered promiscuous mode"
        log_lines=search_string_in_file(file_path,string)
        if(log_lines):
            for line in log_lines:
                interface_name=extract_interface(line)
                if(check_net_interface(interface_name)):
                    print(f"La interface {interface_name} se encuentra en modo promiscuo.")
                    print("Interfaz modo promiscuo","",f"La interface {interface_name} se encuentra en modo promiscuo.")
                    subprocess.run(f"ifconfig {interface_name} -promisc", shell=True, check=True)
                    print("Modo promiscuo desactivado","",f"Se desactivo la interfaz {interface_name} del modo promiscuo por medida de seguridad.")
                    print(f"Se desactivo la interfaz {interface_name} del modo promiscuo por medida de seguridad.")
        else:
            print("El sistema no entro en modo promiscuo.")    
    except Exception as error:
        print("No se pudo verificar que el dispositivo entro en modo promiscuo: ",error)

def check_net_interface(interface_name):
    command_interface=f"ip a show {interface_name} | grep -i promisc"
    ps=subprocess.Popen(command_interface,shell=True,stdout=subprocess.PIPE,text=True)
    output=ps.communicate()[0]
    if (output):
        return 1
    else:
        return 0

check_promiscuos_mode()
