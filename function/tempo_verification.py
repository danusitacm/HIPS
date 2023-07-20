from utils import execute_process,kill_process,file_to_list,search_string_in_file
import logs
import subprocess
import os
def check_ps():
    try:
        command="ps x | grep /tmp/ | grep -v grep | awk '{print $1\" \"$5\"\"$6}'"
        process_list=execute_process(command)
        if process_list:
            for process in process_list:
                process=process.split()
                print("Se detecto un processo ejecutandose desde /tmp.")
                kill_process(process)
                print("Se mato el proceso.")
                if (os.path.isfile(process[1])):
                    subprocess.run(f"mv {process[1]} /hips/cuarentena",shell=True)
                    print("Se puso en cuarentena el archivo que ejecutaba el proceso.")
        else:
            print("No se encontro proceso ejecutanse desde /tmp")
    except Exception as error:
        print("Error al verificar si hay un proceso ejecutandose desde /tmp",error)
    
def check_tmp_extension():
    try:
        extension_list=[".cpp", ".c", ".exe", ".sh", ".php", ".py"]
        for extension in extension_list:
            command=f"find /tmp -type f -name \"*{extension}\" | grep -v /tmp/pyright "
            output=execute_process(command)
            if(output):
                for sussy_file in output:
                    print("Se encontraron archivos sospechosos :",sussy_file)
                    logs.log_alarm("Archivos sospechosos en tmp","",f"Se detecto el archivo {sussy_file} con extension {extension}.")
                    subprocess.run(f"mv {sussy_file} /hips/cuarentena",shell=True)
                    logs.log_prevention("Archivo en cuarentena","","Se puso el archivo en cuarentena, ya que era una extension inusual en /tmp")
                    print("Se puso el archivo en cuarentena, ya que era una extension inusual en /tmp")
            else:
                print("No se encontro ningun archivo con extension: ",extension)
    except Exception as error:
        print('Error al verificar el directorio /tmp: ',error)
def check_tmp_script():
    try:
        command="find /tmp -type f"
        file_list=execute_process(command)
        if(file_list):
            for file in file_list:
                if(search_string_in_file(f"{file}","#!")):
                    print(f"Se encontro que en el archivo {file} con la linea inicial #!.")
                    #subprocess.run(f"mv {os.path.abspath(file)} /hips/cuarentena",shell=True)
                    print("Se puso el archivo en cuarentena, un script no puede estar en /tmp")
    except:
        print('Error al verificar si un archivo es un script.')
#check_ps()
#check_tmp_extension()
check_tmp_script()