#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    print(result)
    
# Regex para donde no se esta escapando el punto
search_with_regex("welcome", r".com")

# Regex para donde se esta escapando el punto
search_with_regex("mydomain.com", r"\.com")

# Regex que obtiene los caracteres (alfanumericos y underscore) antes del espacio
search_with_regex("This is an example", r"\w*")

search_with_regex("And_this_is_another", r"\w*")

# Regex para verificar si el texto pasado tiene al menos 2 grupos de caracteres alfanuméricos (incluidas letras, números y guiones bajos) separados por uno o más espacios en blanco.
search_with_regex("123  Ready Set GO", r"[\w*] [\w*]")