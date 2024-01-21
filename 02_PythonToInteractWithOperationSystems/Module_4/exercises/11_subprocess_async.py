#!/usr/bin/env python3

import time
import subprocess

# Funcion que permite ejecutar acciones  de forma asincrona a traves de comandos de linea
def example_subprocess():
    process = subprocess.Popen(['sleep', '5'])
    message_1 = "El proceso se está ejecutando en segundo plano..."

    # Espere un par de segundos para demostrar el comportamiento asincrónico.
    # time.sleep(6)
    time.sleep(2)

    # Comprueba si el proceso ha finalizado
    if process.poll() is None:
        message_2 = "El proceso aún está ejecutandose"
    else:
        message_2 = "El proceso ha finalizado"

    print(message_1, message_2)

example_subprocess()