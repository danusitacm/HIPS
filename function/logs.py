import datetime

def log_alarm(type_alarm,destination_ip, description):
    file_path = "/var/log/hips/alarmas.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}::{type_alarm}::{destination_ip}::{description}\n"
    
    with open(file_path, 'a') as file:
        file.write(log_entry)

def log_prevention(type_prevention, destination_ip, description):
    file_path = "/var/log/hips/prevencion.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}::{type_prevention}::{destination_ip}::{description}\n"
    
    with open(file_path, 'a') as file:
        file.write(log_entry)