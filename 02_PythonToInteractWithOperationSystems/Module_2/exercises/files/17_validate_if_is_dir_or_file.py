#!/usr/bin/env python3

import os

# Funcion que retorna el listado el path parcial del archivo
def get_list_of_path_files(directory_name):
    for file_name in os.listdir(directory_name):
        full_name = os.path.join(directory_name, file_name)
        if os.path.isdir(full_name):
            print(f"{full_name} es un [directorio]")
        else:
            print(f"{full_name} es un [archivo]")

# Funcion que retorna el listado de archivos que hay dentro de un directorio solo si el directorio existe, de lo contrario generara error
def get_list_of_full_path_files(directory_name):
    current_directory = os.getcwd()
    for file_name in os.listdir(directory_name):
        full_path = os.path.join(current_directory, directory_name, file_name)
        if os.path.isdir(full_path):
            print(f"{full_path} es un [directorio]")
        else:
            print(f"{full_path} es un [archivo]")

print("get_list_of_path_files => \n")
get_list_of_path_files("files")
                                    
print("\nget_list_of_full_path_files => \n")
get_list_of_full_path_files("files")
