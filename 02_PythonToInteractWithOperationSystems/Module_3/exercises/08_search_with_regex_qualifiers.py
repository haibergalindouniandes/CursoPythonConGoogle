#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex y grupos
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    if result is None:
        print("No se encontro ningun coincidencia")
    print(result)

# Funcion que imprime todas la incidencias con base al math realizado por el regex
def search_all_with_regex(data, pattern):
    result = re.findall(pattern, data)
    if result is None:
        print("No se encontro ningun coincidencia")
    print(result)
    
# Regex que permite imprimir la informacion que coincida {5} numero de veces que se repite 
search_with_regex("a ghost", r"[a-zA-Z]{5}") # <_sre.SRE_Match object; span=(2, 7), match='ghost'>
search_with_regex("a scary ghost appeared", r"[a-zA-Z]{5}") # <_sre.SRE_Match object; span=(2, 7), match='scary'>

# Regex que permite imprimir la informacion que coincida {5} numero de veces que se repite y corta hasta cumplir con este numero de caracteres
search_all_with_regex("A scary ghost appeared", r"[a-zA-Z]{5}") # ['scary', 'ghost', 'appea']
# Regex que permite imprimir la informacion que coincida {5} numero de veces que se repite exactamente
search_all_with_regex("A scary ghost appeared", r"\b[a-zA-Z]{5}\b") # ['scary', 'ghost']
# Regex que permite imprimir la informacion que coincida en un rango de 5 a 10 caracteres (ya sea numero o letras)
search_all_with_regex("I really like strawberries", r"\w{5,10}") # ['really', 'strawberri']
# Regex que permite imprimir la informacion que coincida en un rango de 5 caracteres minimo hasta el siguiente espacio en blanco
search_all_with_regex("I really like strawberries", r"\w{5,}") # ['really', 'strawberries']
# Regex que permite imprimir la informacion que que inicia con la letra "s" y en un rango de 0 caracteres a 20 caracteres
search_all_with_regex("I really like strawberries", r"s\w{,20}") # ['strawberries']