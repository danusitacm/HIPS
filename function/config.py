import subprocess

def run_command(command):
    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando {command}: {e}")

# Bitacoras del sistema
# Directorio del Hips
run_command(["mkdir","/var/log/hips"])
run_command(["chmod", "700","/var/log/hips"])

# Para alarmas y prevencion
run_command(["touch", "/var/log/hips/alarmas.log"])
run_command(["chmod", "700","/var/log/hips/alarmas.log" ])

run_command(["touch", "/var/log/hips/prevencion.log"])
run_command(["chmod", "700","/var/log/hips/prevencion.log" ])

# Por el momento la carpeta del hips
run_command(["mkdir","/hips"])
run_command(["chmod", "700","/hips"])

run_command(["touch","/hips/ip_detected"])
run_command(["chmod", "700","/hips/ip_detected"]) 
# Para el backup
run_command(["mkdir","/hips/backup"])
run_command(["chmod", "700","/hips/backup"])

run_command(["mkdir","/hips/backup/system_file"])
run_command(["mkdir","/hips/backup/binary_file"])
# Para la cuarentena 
run_command(["mkdir","/hips/cuarentena"])
run_command(["chmod", "700","/hips/cuarentena"])