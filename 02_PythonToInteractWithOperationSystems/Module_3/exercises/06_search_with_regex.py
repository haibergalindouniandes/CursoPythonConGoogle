#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    print(result)
    
# Regex que permite un numero telefonico con este forma 111-222-3333
search_with_regex("111-222-3333", r"\d{3}-\d{3}-\d{4}")
# Regex que permite un numero telefonico con este forma 111-222-3333. Este retgorna None ya que no coincide con el regex
search_with_regex("1234567890", r"^\d{3}-\d{3}-\d{4}")

# Regex que permite validar numeros positivo o negativos con decimal o no
search_with_regex("1222334.99", r"^-?\d*(\.\d+)?$")

# Regex que permite validar el nombre de un archivo
search_with_regex("ruta/directorio/subdirectorio/archivo.txt", r"^(.+)/([^/]+)$")

