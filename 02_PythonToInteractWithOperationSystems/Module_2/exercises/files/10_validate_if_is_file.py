#!/usr/bin/env python3

import os

# Funcion que retorna la ruta absoluta del archivo
def validate_if_is_file(path, file_name):
    if os.path.isfile(f"{path}/{file_name}"):
        return f"[{path}/{file_name}] SI es un archivo"
    return f"[{path}/{file_name}] NO es un archivo o no existe"

print(validate_if_is_file("./files" ,"example.txt"))
print(validate_if_is_file("./files" ,"example.csv"))