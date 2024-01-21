#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada sin hacer uso de regex. El problema con esa forma de obtener la informacion es que no conocemos el numero de caracteres que tendra este []
def search_without_regex(data, pattern):
    index = data.index(pattern)
    print(data[index+1:index+6])

# Funcion que imprime la informacion buscada haciendo uso de regex
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    print(result[1])

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

search_without_regex(log, "[")

regex = r"\[(\d+)\]"
search_with_regex(log, regex)