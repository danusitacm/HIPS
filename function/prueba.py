from utils import execute_process, create_dictionary
import subprocess
def check_net_interface(interface_name):
    command_interface=f"ip a show {interface_name} | grep -i promisc"
    output=execute_process(command_interface)
    if (output):
        return 1
    else:
        return 0   

command="grep -i \"entered promiscuous mode\" /var/log/messages | awk '{print $7}'"
interface_list=execute_process(command)
interface_list=list(set(interface_list))
interface_status={
    'interface_name':'',
    'interface_status':'',
}
values=[]
if(interface_list):
    print(interface_list)
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
    print(values)
else:
    print("El dispositivo no se encuentra en modo promiscuo.")