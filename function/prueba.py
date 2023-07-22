from utils import execute_process, create_dictionary
def check_user_connected():
    command="w -h | awk '{print $1,$2,$3}'"
    list_user=execute_process(command)
    user_list = []
    for user in list_user:
        user=user.split()
        if("tty" in user[1]):
            user[2]='localhost'
        user_dicc={
            'user_name':user[0],
            'user_terminal':user[1],
            'user_ip':user[2],
        }   
        user_list.append(user_dicc)
check_user_connected()