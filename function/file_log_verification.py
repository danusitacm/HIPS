import subprocess
ip_white_list=["192.168.0.15"]
def get_dict(log):
    log=log.split()
    log_result={
        'uid': log[9].split("=")[1],
        'tty': log[11].split("=")[1],
        'ruser': log[12].split("=")[1],
        'rhost': log[13].split("=")[1],
        'user': log[14].split("=")[1]
    }
    for word in log[9:]:
        for key in log_result:
            if key in word:
                log_result[key]=word.split("=")[1]
    print(log_result)
    return log_result  
def check_failed_password_ssh():
    p=subprocess.Popen("grep")
    pass
def sshd_auth(log):
    try:
        for ip in ip_white_list:
            print(f"rhost={ip}" in log)
            if not f"rhost={ip}" in log:
                print("Ip desconocido esta tratando de acceder al sistema por ssh")         
    except Exception as error:
        print(error)
def login_auth():
    pass
def su_auth():
    pass 
def check_authentication_failure():
    command_auth="cat /var/log/secure | grep -i \":auth\" |grep -i \"authentication failure\" "
    p=subprocess.Popen(command_auth,shell=True,stdout=subprocess.PIPE,text=True)
    output=p.communicate()[0].split("\n")
    output.pop()
    for log in output:
        
        if "sshd:auth" in log:
            print("Autenticacion en sshd")
            get_dict(log)
        elif "login:auth" in log:
            print("Autenticacion en login")
            get_dict(log)
        elif "su-l:auth" in log:
            print("Autenticacion en su")
            get_dict(log)
    pass

def check_access_httpd_error():
    pass
def check_massive_email():
    pass

check_authentication_failure()