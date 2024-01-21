#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex
def search_with_regex(data, pattern):
    result = re.search(pattern, data)
    print(result)
    
# Regex que permite validar si un el texto inicia con A y termina con a
search_with_regex("Australia", r"^A.*a$")
# Regex que permite validar si un el texto inicia con A y termina con a. Este retgorna None ya que no coincide con el regex
search_with_regex("Azerbaijan", r"^A.*a$")


# Regex que permite validar si un el texto inicia con dos grupos especificos, el primero solo letras de la a Z incluyendo _. Y el grupo final alfanumerico incluyendo _
search_with_regex("_this_is_a_valid_variable_name", r"^[a-zA-Z_][a-zA-Z0-9_]*$")
search_with_regex("my_variable1", r"^[a-zA-Z_][a-zA-Z0-9_]*$")

# Regex que permite validar si un el texto inicia con dos grupos especificos, el primero solo letras de la a Z incluyendo _. Y el grupo final alfanumerico incluyendo _. 
# Este retorna None ya que no coincide con el regex
search_with_regex("123_this_is_a_valid_variable_name", r"^[a-zA-Z_][a-zA-Z0-9_]*$")

# Regex para verificar si el texto pasado se parece a una oración estándar, lo que significa que comienza con una letra mayúscula, 
# seguida de al menos algunas letras minúsculas o un espacio, y termina con un punto, un signo de interrogación o un signo de exclamación.
search_with_regex("Is this is a sentence!", r"^[A-Z][a-z\s]+[.!?]$")
