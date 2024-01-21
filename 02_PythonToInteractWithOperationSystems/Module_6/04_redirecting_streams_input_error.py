#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

# En la consola de comandos vamos crear un archivo redireccionando la entrada de la ejecución del archivo python y generamos otro archivo
# con la descripcion del error generado:
# ./04_redirecting_streams_input_error.py < files/stdout_04_redirecting_streams_input.txt 2> files/stdout_04_redirecting_streams_error.txt

# Cabe recalcar que si no se presenta ningun error en la ejecución segenerar el archivo stdout_04_redirecting_streams_error.txt pero vacio