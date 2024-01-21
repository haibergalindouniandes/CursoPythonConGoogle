#!/usr/bin/env python3

import re

# Funcion que permite dividir y obtener en una lista los valores que coincidan con el regex enviado
def split_with_regex(data, pattern):
    result = re.split(pattern, data)
    if result is None:
        print(data)
    else:
        print(result)

# Regex que permite obtener una lista con los valores que coinciden excluyendo los caracteres como . ? y !
split_with_regex("One sentence. Another one? And the last one!", r"[.?!]") # ['One sentence', ' Another one', ' And the last one', '']

# Regex que permite obtener una lista con los valores que coinciden incuyendo los caracteres como . ? y !
split_with_regex("One sentence. Another one? And the last one!", r"([.?!])") # ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
