#!/usr/bin/env python3

import os

# Funcion que retorna la ruta absoluta del archivo
def get_absolute_path_of_file(path, file_name):
    return os.path.abspath(f"{path}/{file_name}")

absolute_path_file = get_absolute_path_of_file("./files" ,"example.txt")
print(f"La ruta absoluta del archivo es => [{absolute_path_file}]")