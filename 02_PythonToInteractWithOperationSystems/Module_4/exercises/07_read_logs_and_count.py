#!/usr/bin/env python3

import re
import sys

# Para obtener los argumentos enviados a traves de consola se hace a traves de la funcion argv de la libreria sys
logfile = sys.argv[1]
text_to_search = sys.argv[2]

# Funcion que permite obtener informacion a traves del regex y contar las incidencias encontradas guardando la informacion en un diccionario
def search_logs_with_pattern(log_file, text_to_search, pattern):
    usernames = {}
    with open(log_file) as f:
        for line in f:
            if text_to_search not in line:
                continue

            result = re.search(pattern, line)

            if result is None:
                continue
            name = result[1]
            usernames[name] = usernames.get(name, 0) + 1

    print(usernames)

search_logs_with_pattern(logfile, text_to_search, r"USER \((\w+)\)$")