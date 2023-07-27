# Hips 
## Acerca del proyecto
Proyecto final de la materia Sistemas Operativos II.
### Opciones
- Verificar las modificaciones realizadas en el archivo /etc/passwd y /etc/shadow.
- Verificar los usuarios conectados y su ip.
- Chequear sniffers.
- Examinar algunos archivos log.
- Verificar el tamaño de la cola mails del equipo.
- Verificar el consumo de recursos por parte de los procesos.
- Verificar directorio /tmp de archivos sospechos como scripts.
- Examinar archivos que estan ejecutandose como cron.

## Instalacion 
### Pre-requisitos
- Estar logeado como usuario root o usuario con privilegios sudo
- Correr en un sistema de Centos 7
- Utilizar Python3 
### Preparacion del sistema
```console
yum update
yum install net-tools
yum install postgresql-server
```
### Descargar el repo
Descargar el repositorio en directorio raiz /
```console
git clone https://github.com/danusitacm/hips.git
```
### Instalacion y configuracion de potsgresql
```console
sudo postgresql-setup --initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
create user <BD_USER> with password <BD_PASSWORD>;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO <BD_USER>;
sudo -u postgres createdb <BD_NAME>
alter database <BD_NAME> owner to <BD_USER>
```
### Creacion de carpetas
En la carpeta hips hay un script que crea, condece permisos a las carpetas que utilizaria el hips.
```console
python3 /hips/function/config.py 
```
### Entorno virtual
Creamos el entorno virutal para poder instalar las herramientas que necesitamos.
```console
virtualenv .venv
pip3 install -r requirements.txt
```
### Variables de entorno
```console
vi .env
```
```console
BD_PASSWORD="Constraseña del usuario dueño de la base de datos"
BD_USER="Nombre del usuario de la base de datos"
BD_NAME="Nombre de la base de datos"
BD_PORT="Puerto de potsgresql"
BD_HOST="Ip de la base de datos"
```
```console
chmod 700 .env
```
### Usuario
Comunicarse con el desarrollador para que le proporcione la constraña y para el usuario root del hips.
## Manual de Uso
Ejecutar el comando para poder encender el servidor en el puerto 80
```console
python3 manage.py runserver localhost:80
```
Al poner en link de nuestro navegador localhost:80 nos abrira este inicio.

![texto cualquiera por si no carga la imagen](https://github.com/danusitacm/hips/blob/main/doc/index.png)

Tendremos que pulsar en el boton que dice login e iniciar sesion.

![texto cualquiera por si no carga la imagen](https://github.com/danusitacm/hips/blob/main/doc/login.png)

Y si introducimos el usuario correcto nos mostrara el dashboard con los botones que queremos acceder.

![texto cualquiera por si no carga la imagen](https://github.com/danusitacm/hips/blob/main/doc/dashboard.png)

