from django.shortcuts import render
from function.utils import execute_process
from django.contrib.auth.decorators import login_required
from function.logs import *
# Create your views here.
@login_required
def check_queue_email_view(request):
    """Funciona la cola de emails si supera mas de 100 alerta al usuario

    Args:
        request : La solicitud HTTP enviada por el usuario.

    Returns:
        Retorna un mensaje 
        Si la cola de mails sobrepasa los 100 retorna un mensaje de alerta 
        Si la cola de mails esta vacia retorna un mensaje de que esta vacia.
    """
    try:
        command_email = "mailq"
        output = execute_process(command_email)
        print(output)
        if "is empty" in output[0]:
            messages_status = "La cola de mails está vacía."
        elif len(output) > 100:
            messages_status = "La cola de mails tiene un número MASIVOS de mails pendientes."
            log_alarm("Cola MASIVA","","Se detecto que la cola de mails se encuentra con una cantidad MASIVA de correos")
    except Exception as error:
        messages_status = f'Error al verificar la cola de mails: {error}'
    finally:
        return render(request, 'queue_mail_checker.html', {'messages_status': messages_status})