from utils import execute_process
import logs
def check_user_cron():
    try:
        command_getuser="cat /etc/passwd | awk -F : '{print $1}'"
        list_user=execute_process(command_getuser)
        list_user.pop(0)
        if(list_user):
            for user in list_user:
                command_crontab=f"crontab -u {user} -l"
                list_cron=execute_process(command_crontab)
                if("no crontab for" in list_cron):
                    print(list_cron)
                else:
                    for cron in list_cron:
                        cron=cron.split()
                        print(f"Se detecto que el user {user} esta ejecutando el archivo {cron[6]} como cron.")
                        logs.log_alarm(f"Archivo cron","",f"Se detecto que el user {user} esta ejecutando el archivo {cron[6]} como cron.")
    except Exception as error:
        print('An exception occurred',error)
check_user_cron()