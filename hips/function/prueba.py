from utils  import *
command="cat /var/log/httpd/acces.log | grep \"404\" | awk '{print $1}'"
ip_list=execute_process(command)
if(ip_list):
    ip_list=list(set(ip_list))
    for ip in ip_list: 
        commanda_2=f"cat /var/log/httpd/acces.log | grep -c {ip}"
        repeate_attemps=execute_process(commanda_2)
        print(repeate_attemps)