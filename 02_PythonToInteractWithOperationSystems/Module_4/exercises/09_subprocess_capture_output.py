#!/usr/bin/env python3

import subprocess

# Funcion que permite ejecutar acciones interactuando directamente a traves de comandos en linea con el sistema operativo y capturando toda la informacion de la ejecucion
def example_subprocess():
    # Proceso que se ejecuta de forma exitosa
    result = subprocess.run(["echo", "Hola mundo !"], capture_output=True)
    print("result => [{}]".format(result))
    print("result.returncode => [{}]".format(result.returncode))
    print("result.args => [{}]".format(result.args))
    print("result.stdout => [{}]".format(result.stdout))
    print("result.stderr => [{}]".format(result.stderr))
    print("result.stdout.decode().split() => [{}]\n".format(result.stdout.decode().split()))
    
    # Proceso que se ejecuta de forma exitosa
    result = subprocess.run(["mkdir", "files/dir_to_delete"], capture_output=True)
    print("result => [{}]".format(result))
    print("result.returncode => [{}]".format(result.returncode))
    print("result.args => [{}]".format(result.args))
    print("result.stdout => [{}]".format(result.stdout))
    print("result.stderr => [{}]".format(result.stderr))
    print("result.stdout.decode().split() => [{}]\n".format(result.stdout.decode().split()))
    
    # Proceso que se ejecuta de forma exitosa
    result = subprocess.run(["ls", "files/test.log"], capture_output=True)
    print("result => [{}]".format(result))
    print("result.returncode => [{}]".format(result.returncode))
    print("result.args => [{}]".format(result.args))
    print("result.stdout => [{}]".format(result.stdout))
    print("result.stderr => [{}]".format(result.stderr))
    print("result.stdout.decode().split() => [{}]\n".format(result.stdout.decode().split()))

    # Proceso que genera un error al ejecutarse    
    result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
    print("result => [{}]".format(result))
    print("result.returncode => [{}]".format(result.returncode))
    print("result.args => [{}]".format(result.args))
    print("result.stdout => [{}]".format(result.stdout))
    print("result.stderr => [{}]".format(result.stderr))
    print("result.stdout.decode().split() => [{}]\n".format(result.stdout.decode().split()))

example_subprocess()