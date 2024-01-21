#!/usr/bin/env python3

import os
import sys

# Para obtener los argumentos enviados a traves de consola se hace a traves de la funcion argv de la libreria sys
filename = sys.argv[1]

# En este fragmento de codigo se recibira el nombre del archivo argv[1] y se creara un archivo nuevo. Si existe imprimira por pantalla y saldra de la aplicacion.
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    # Sys.exit(1) se utiliza para salir del proceso
    sys.exit(1)