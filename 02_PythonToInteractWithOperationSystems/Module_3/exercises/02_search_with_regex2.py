#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    print(result)
    
# Funcion que imprime la informacion buscada haciendo uso de regex e ingorando mayusculas y minusculas
def search_with_regex_ignorecase(data, pattern):
    result = re.search(pattern, data, re.IGNORECASE)
    print(result)    
    
# Funcion que imprime la informacion buscada haciendo uso de regex e ingorando mayusculas y minusculas
def search_all_with_regex(data, pattern):
    result = re.findall(pattern, data)
    print(result)       

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade, this error was detected using python312. "
"Python is a programming lenguaje, very easy and powerful. This is a sentence with spaces. I like cats. I like dogs."

# Busqueda normal usando regex
search_with_regex(log, r"er")

# Busqueda usando el comodin . El cual retorna todas incidencias que inicien con la palabra buscada
search_with_regex(log, "m.comp")

# Busqueda usando el comodin ^ . El cual retorna todas las incidencias que inicien con la palabra buscada
search_with_regex(log, "^J")

# Busqueda ignorando mayusculas y minusculas
search_with_regex_ignorecase(log, r"er")

# Busqueda que no retorna ningun match
search_with_regex(log, r"Prueba")

# Busqueda que retorna la incidencia de la palabra buscada ya sea con con la P mayuscula o minuscula
search_with_regex(log, r"[Pp]ython")

# Busqueda que retorna la incidencia de la palabra buscada la cual debe ser una letra del alfabeto en minuscula
search_with_regex(log, r"[a-z]ython")

# Busqueda que retorna la incidencia de la palabra buscada la cual debe ser una letra del alfabeto en mayuscula
search_with_regex(log, r"[A-Z]ython")

# Busqueda que retorna la incidencia de la palabra buscada la cual puede ser letra del alfabeto ya sea minuscula o mayuscula o numerico
search_with_regex(log, r"python3[a-zA-Z0-9]")

# Busqueda que retorna la incidencia de la palabra buscada la cual puede contener espacios
search_with_regex(log, r"[^a-zA-Z]")

# Busqueda que retorna la incidencia de la palabra buscada la cual puede ser cat o dog
search_with_regex(log, r"cat|dog")

# Busqueda que retorna en una lista todas las palabras que tienen incidencias
search_all_with_regex(log, r"cat|dog")