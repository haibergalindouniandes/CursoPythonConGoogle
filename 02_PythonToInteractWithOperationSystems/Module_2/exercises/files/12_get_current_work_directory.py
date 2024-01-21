#!/usr/bin/env python3

import os

# Funcion que retorna el directorio de trabajo actual
def get_current_work_directory():
    return os.getcwd()

currect_directory = get_current_work_directory()
print(f"El directorio de trabajo actual es => [{currect_directory}]")