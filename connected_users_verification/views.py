from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import subprocess

def verify_connected_users():
    try:
        list_user = subprocess.run("w", capture_output=True, text=True)
        connected_users_output = list_user.stdout
        return connected_users_output
    except Exception as error:
        connected_users_output = f"Error al ver los usuarios conectados: {error}"
    
def connected_users_view(request):
    connected_users_output = verify_connected_users()
    return render(request,"/connected_users.html", {'connected_users_output': connected_users_output})