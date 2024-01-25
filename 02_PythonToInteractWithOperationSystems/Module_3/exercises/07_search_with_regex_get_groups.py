#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex y grupos
def search_with_regex_get_groups(data, pattern):
    result = re.search(pattern, data)
    if result is None:
        print("No se encontro ningun coincidencia")
    print("Grupos => [{}]".format(result.groups()))
    print("Grupos [0] => [{}]".format(result[0]))
    print("Grupos [1] => [{}]".format(result[1]))
    print("Grupos [2] => [{}]".format(result[2]))
    print("Contaneración de grupo [2] y grupo [1] => [{} {}]\n".format(result[2], result[1]))
    
    
# Funcion que implementa expresión regular utilizada en la función rerange_name para que pueda coincidir con segundos nombres, iniciales del segundo nombre y apellidos dobles.
def search_with_regex_get_3_groups(data, pattern):
    # Updated regex to match names with optional middle names, middle initials, and double surnames
    result = re.search(pattern, data)
    print(type(result.groups()))
    if result is None:
        print("No se encontro ningun coincidencia")
    last_name = result.group(1)
    first_name = result.group(2)
    middle_name = result.group(3)
    if middle_name is None:
        middle_name = result.group(4)
    return "{} {}{}".format(first_name, middle_name or "", last_name)
    
# Regex que permite imprimir los grupos obtenidos
search_with_regex_get_groups("Lovelace, Ada", r"^(\w*), (\w*)$")
search_with_regex_get_groups("Ritchie, Dennis", r"^(\w*), (\w*)$")

search_with_regex_get_groups("Hopper, Grace M.", r"^([\w .-]*), ([\w .-]*)$")


print(search_with_regex_get_3_groups("Kennedy, John F.", r"^(\w+),\s?(\w+)(?:\s+(\w+|\w\.)|,\s?(\w+))?(\s\w+)?$"))

