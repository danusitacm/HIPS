import subprocess
import logs
ip_white_list=["192.168.0.15","192.168.0.14"]
def get_dict(log):
    log=log.split()
    log_result={
        'uid': '',
        'tty': '',
        'ruser': '',
        'rhost': '',
        'user': ''
    }
    for word in log[9:]:
        for key in log_result:
            if key in word:
                log_result[key]=word.split("=")[1]           
    return log_result  

def check_failed_password_ssh():
    p=subprocess.Popen("grep")
    pass

def sshd_auth(dic_log):
    try:
        if not (dic_log["rhost"] in ip_white_list ):         
            logs.log_alarm("Ip intruso","","Se ha detectado un ip intruso "+dic_log["rhost"]+", tratando de ingresar como "+dic_log["user"]+".")   
    except Exception as error:
        print(error)

def login_auth(dic_log):
    
    pass

def su_auth(dic_log):
    
    pass 

def check_authentication_failure():
    command_auth="cat /var/log/secure | grep -i \":auth\" |grep -i \"authentication failure\" "
    p=subprocess.Popen(command_auth,shell=True,stdout=subprocess.PIPE,text=True)
    output=p.communicate()[0].split("\n")
    output.pop()
    for log in output:
        if "sshd:auth" in log:
            print("Autenticacion en ssh")
            sshd_auth(get_dict(log))
        elif "login:auth" in log:
            print("Autenticacion en login")
            login_auth(get_dict(log))
        elif "su-l:auth" in log:
            print("Autenticacion en su")
            su_auth(get_dict(log))
    pass

def check_access_httpd_error():
    pass
def check_massive_email():
    pass

check_authentication_failure()