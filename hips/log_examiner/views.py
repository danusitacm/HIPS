from django.shortcuts import render
import os
from function.utils import execute_process
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def log_examiner(request):
    return render(request,"log_examiner.html")

def block_ip(ip):
    command=f"route add -host {ip} reject"
    execute_process(command)

@login_required
def check_error_404(request):
    values=[]
    command="cat /var/log/httpd/acces.log | grep \"404\" | awk '{print $1}'"
    ip_list=execute_process(command)
    if(ip_list):
        ip_list=list(set(ip_list))
        for ip in ip_list: 
            commanda_2=f"cat /var/log/httpd/acces.log | grep -c {ip}"
            repeate_attemps=execute_process(commanda_2)
            repeate_attemps=repeate_attemps[0]
            if (int(repeate_attemps)>3):
                ip_amongus={
                    'ip_intruser':ip,
                    'attemps':repeate_attemps,
                }
                values.append(ip_amongus)
                block_ip(ip)
    return render(request,"check_error_404.html",{'sussy_ip':values})

