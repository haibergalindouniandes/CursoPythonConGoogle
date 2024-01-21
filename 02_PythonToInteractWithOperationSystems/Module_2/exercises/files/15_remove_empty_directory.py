#!/usr/bin/env python3

import os
import time

# Funcion que permite la creación de un nuevo directorio
def create_directory(path, directory_name):
    return os.mkdir(f"{path}/{directory_name}")

# Funcion que permite eliminar el directorio solo si esta vacio, de lo contrario generara error
def remove_directory(path, directory_name):
    return os.rmdir(f"{path}/{directory_name}")

new_directory = "directory_temporal"
create_directory("./files", new_directory)
print(f"Se creo el nuevo directorio => [{new_directory}]")

# Esperar 5 segunos para ejecutar la eliminacion
time.sleep(5)

remove_directory("./files", new_directory)
print(f"Se elimino el directorio correctamente")