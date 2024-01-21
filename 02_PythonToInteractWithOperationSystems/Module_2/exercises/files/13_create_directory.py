#!/usr/bin/env python3

import os

# Funcion permite la creación de un nuevo directorio
def create_directory(path, directory_name):
    return os.mkdir(f"{path}/{directory_name}")

new_directory = "directory_to_remove"
create_directory("./files", new_directory)
print(f"Se creo el nuevo directorio => [{new_directory}]")