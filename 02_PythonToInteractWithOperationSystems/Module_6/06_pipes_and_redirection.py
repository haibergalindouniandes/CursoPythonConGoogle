#!/usr/bin/env python3

import sys

# Permite convertir las entrada en Capitalize
for line in sys.stdin:
    print(line.strip().capitalize())

# En la consola de comandos vamos sobreescribir el archivo archivo haiku.txt y convertir cada texto en Capitalize:
# cat files/haiku.txt | ./06_pipes_and_redirection.py 

# En la consola de comandos vamos leer la información que esta en el archivo haiku linea por linea, convertiremos cada linea en Capitalize
# y poesteriormente crearemos un nuevo archivo con los datos convertidos anteriormente:
# cat files/haiku.txt | ./06_pipes_and_redirection.py < files/new_haiku.txt