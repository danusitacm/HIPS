from utils import execute_process
import logs
def check_queue_email():
    try:
        command_email="mailq"
        output=execute_process(command_email)
        if "is empty" in output:
            print("La cola de mails esta vacia.")
        elif len(output)>100:
            logs.log_alarm("COLA DE MAILS SATURADA","",f"se encontraron {len(output)} mails en la cola")
    except Exception as error:
      print('Error al verificar la colas de mails',error)
    
        
