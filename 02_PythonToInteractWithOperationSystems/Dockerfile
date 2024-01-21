# Usa la imagen base de Ubuntu
FROM ubuntu:latest

# Cambia al usuario root
USER root

# Actualiza los paquetes e instala las dependencias necesarias para Python
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip 

RUN apt-get install -y nano
RUN apt-get install -y vim
RUN apt-get install python3.10-venv
RUN apt-get install dos2unix
# Establece el directorio de trabajo
WORKDIR /app

# Copia el contenido del directorio actual al directorio de trabajo
COPY . /app

# Instala las dependencias del proyecto (si las tienes en un archivo requirements.txt)
# RUN pip3 install -r requirements.txt

# Comando por defecto para ejecutar cuando se inicie el contenedor
CMD ["bash"]
