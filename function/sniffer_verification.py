import subprocess
import logs
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
import subprocess
""" Notas para mi yo 
Agregar una lista de usuarios y si el usuario ejecuto ese comando enviarlo a la cuarentena ese archivo"""
def get_sniffer_processes(tool_name):
    try:
        string='{print $1" "$2" "$11""$12}'
        command = f"sudo ps -uax | grep tcpdump | grep -v grep | awk '{string}'"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, text=True)
        output = process.communicate()[0].split("\n")
        output.pop()
        return output
    except Exception as error:
        print("Error al ejecutar el comando ps: ", error)

def check_sniffer():
    try:
        for tool in packet_capture_tools:
            result_ps = get_sniffer_processes(tool)
            if result_ps:
                for process in result_ps:
                    process = process.split()
                    logs.log_alarm("Sniffer activado","",f"El proceso {process[1]} fue activado por el user {process[0]}")
                    subprocess.run(f"kill -9 {process[1]}", shell=True)
                    logs.log_prevention("Proceso desactivado","",f"El proceso {process[1]} se encuentra en la lista negra, fue desactivado por esta razon.")
    except Exception as error:
        print("No se puede verificar si hay un sniffer: ", error)

    
check_sniffer()