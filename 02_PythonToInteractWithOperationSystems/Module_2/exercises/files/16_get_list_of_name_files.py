#!/usr/bin/env python3

import os

# Funcion que retorna el listado de archivos que hay dentro de un directorio solo si el directorio existe, de lo contrario generara error
def get_list_of_files(directory_name):
    return os.listdir(directory_name)

# Consulta exitosa
print(get_list_of_files("./files"))

# Error al consulta directorio
print(get_list_of_files("./files01"))