#!/usr/bin/env python3

import os

# Funcion que retorna el listado de archivos que hay dentro de un directorio solo si el directorio existe, de lo contrario generara error
def get_permissions(path):
    # Obtener la información de estado (stat) del directorio o archivo
    info_estado = os.stat(path)
    # Obtener el campo de permisos del objeto de información de estado
    permisos = info_estado.st_mode
    
    # Imprimir los permisos en formato octal
    print(f"Permisos de {path}: {oct(permisos)}")

# Consulta de permisos de un directorio
get_permissions("files")

# Consulta de permisos de un archivo
get_permissions("files/example.txt")