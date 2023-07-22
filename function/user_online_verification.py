import os
import subprocess 
def verify_connected_users():
    try:
        list_user=subprocess.run("w | awk '{print $1,$2,$3}'", capture_output=True, text=True)
        print(list_user.stdout)
        print(type(list_user.stdout))
    except Exception as error:
        print("Error al ver los usuarios conectados: ",error)
verify_connected_users()