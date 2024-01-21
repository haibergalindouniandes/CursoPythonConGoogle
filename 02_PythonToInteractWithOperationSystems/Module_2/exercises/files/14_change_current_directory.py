#!/usr/bin/env python3

import os

# Funcion permite cambiar el directorio actual por otro
def change_current_directory(new_directory):
    return os.chdir(new_directory)

new_directory = "directory_to_remove"
print(f"Directorio actual => [{os.getcwd()}]")

change_current_directory(f"/app/Module_2/exercices/files/{new_directory}")
print(f"Directorio cambiada => [{os.getcwd()}]")