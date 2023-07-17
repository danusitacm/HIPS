import os 
import subprocess
import re
def search_string_in_file(file_path, search_string):
    matching_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if search_string in line.lower():
                    matching_lines.append(line.strip())
        return matching_lines
    except Exception as error:
        print("Ocurrió un error al leer el archivo: ",error) 

def extract_interface(log_line):
    pattern = r'device (\w+) entered promiscuous mode'
    match = re.search(pattern, log_line)
    if match:
        interface_name = match.group(1)
    return interface_name

def check_system_log_files():
    try:
        file_path_centOS="/var/log/messages"
        file_path_ubuntu ="/var/log/syslog"
        string ="entered promiscuous mode"
        log_lines=search_string_in_file(file_path_ubuntu,string)
        for line in log_lines:
            interface_name=extract_interface(line)
            if(check_net_interface(interface_name)):
                print(f"La interface {interface_name} esta en modo promiscuo")
                subprocess.run(f"ifconfig {interface_name} -promisc", shell=True, check=True)
                print(f"Se desactivo la interfaz {interface_name} del modo promiscuo")
            else:
                print("Dispositivo no modo promisc")         
    except Exception as error:
        print("No se pudo verificar que el dispositivo entro en modo promiscuo: ",error)


def check_net_interface(interface_name):
    command_interface=f"ip a show {interface_name} | grep -i promisc"
    result=subprocess.Popen(command_interface,shell=True,stdout=subprocess.PIPE)
    if (result.stdout.readline()).decode('utf-8'):
        return 1
    else:
        return 0

check_system_log_files()
