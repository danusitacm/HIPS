import subprocess
def verify_promisc_mode():
    try:
        subprocess.run("ifconfig eth0 -promisc")
    except Exception as error:
        print("Error",error)