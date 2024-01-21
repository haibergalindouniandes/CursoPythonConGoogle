#!/usr/bin/env python3

import re
import sys

# Para obtener los argumentos enviados a traves de consola se hace a traves de la funcion argv de la libreria sys
logfile = sys.argv[1]
text_to_search = sys.argv[2]

# Permite iterar linea por linea un archivo hasta encontrar el valor buscado


# Funcion que permite obtener informacion a traves del regex
def search_logs_with_pattern(log_file, pattern):
    print("Archivo de log => [{}]".format(log_file))
    print("Regex => [{}]".format(pattern))
    with open(log_file) as file:
        logs = file.read()
        result = re.search(pattern, logs)
        if result == None:
            print("No se encontra nada con el regex ingresado")
        else:
            print(result[1])

# Funcion que permite iterar un archivo linea por linea hasta encontrar el texto deseado
def iterate_file_log(log_file, text_to_search):
    with open(log_file) as logs:
        for line in logs:
            if text_to_search not in line:
                continue
            print(line.strip())

#

# iterate_file_log(logfile, text_to_search)
# pattern = "USER \((\w+)\)$"
search_logs_with_pattern(logfile, text_to_search)