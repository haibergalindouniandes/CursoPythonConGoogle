#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

# En la consola de comandos vamos crear un archivo redireccionando la entrada de la ejecución del archivo python, y posteriormente generamos un error de tipo ValueError:
# ./03_redirecting_streams_error.py > files/stdout_03_redirecting_streams_error.txt