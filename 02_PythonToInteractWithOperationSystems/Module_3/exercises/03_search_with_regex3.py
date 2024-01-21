#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    print(result)
    
# Busqueda normal usando regex
search_with_regex("goldfish", r"o+l+")

search_with_regex("woolly", r"o+l+")

search_with_regex("boil", r"o+l+")

search_with_regex("Pygmalion", r"Py.*n")

search_with_regex("Python Programming", r"Py.*n")

search_with_regex("Python Programming", r"Py[a-z]*n")

search_with_regex("Pyn", r"Py[a-z]*n")


# Regex para validar si se encuentra la palabra peach o each ya que el comodin ? es opcional
search_with_regex("To each their own", r"p?each")

search_with_regex("I like peaches", r"p?each")

# Regex para validar si la letra "a" minuscula o mayuscula se repite al menos dos veces
search_with_regex("Animal Kingdom", r"[Aa].*[Aa]")

