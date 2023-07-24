from django.shortcuts import render
from function.utils import execute_process
# Create your views here.
def check_queue_email_view(request):
    try:
        command_email = "mailq"
        output = execute_process(command_email)
        print(output)
        if "is empty" in output[0]:
            messages_status = "La cola de mails está vacía."
        elif len(output) > 100:
            messages_status = "La cola de mails tiene un número significativo de correos pendientes."
    except Exception as error:
        messages_status = f'Error al verificar la cola de mails: {error}'
    finally:
        return render(request, 'queue_mail_checker.html', {'messages_status': messages_status})