import os
import subprocess
def get_user_online():
    try:
        list_user=subprocess.run("w", capture_output=True, text=True)
        print(list_user.stdout)
    except Exception as error:
        print("Error al ver los usuarios conectados: ",error)
get_user_online()