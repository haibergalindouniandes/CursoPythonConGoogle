#!/usr/bin/env python3

import subprocess

# Funcion que permite ejecutar acciones interactuando directamente a traves de comandos en linea con el sistema operativo
def example_subprocess():
    subprocess.run(["date"])
    subprocess.run(["sleep", "2"])
    result = subprocess.run(["ls", "files/test.log"])
    print(result.returncode)
    result = subprocess.run(["ls", "prueba.txt"])
    print(result.returncode)

example_subprocess()