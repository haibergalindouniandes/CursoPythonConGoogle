#!/usr/bin/env python3

import os
import subprocess

# Funcion que permite ejecutar acciones interactuando directamente a traves de comandos en linea con el sistema operativo y capturando toda la informacion de la ejecucion
def example_subprocess():
    my_env = os.environ.copy()
    print("Current environ configuration => [{}]".format(my_env))
    print("Current environ [PATH] configuration => [{}]".format(my_env["PATH"]))
    my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
    print("Environ [PATH] configuration changed => [{}]".format(my_env["PATH"]))
    result = subprocess.run(["myapp"], env=my_env)
    print("Result of execution command => [{}]".format(result))

example_subprocess()