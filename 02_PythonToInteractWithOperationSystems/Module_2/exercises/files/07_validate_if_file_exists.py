#!/usr/bin/env python3

import os

# Funcion que valida si un archivo existe
def validate_if_exists_file(path, file_name):
    full_path_file = f"{path}/{file_name}"
    if os.path.exists(full_path_file):
        print(f"El archivo [{full_path_file}] => [SI existe]")
    else:
        print(f"El archivo [{full_path_file}] => [NO existe]")
        
validate_if_exists_file("./files" ,"write_example.txt")
validate_if_exists_file("./files" ,"temporal_file.txt")