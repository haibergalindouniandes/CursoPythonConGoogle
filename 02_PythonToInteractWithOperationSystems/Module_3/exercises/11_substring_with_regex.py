#!/usr/bin/env python3

import re

# Funcion que permite crear un nuevo string haciendo un substring y remplazando el valor con base al regex enviado
def substring_with_regex(pattern, value_to_replace, data):
    result = re.sub(pattern, value_to_replace, data)
    if result is None:
        print(data)
    else:
        print(result)

# Regex que permite reemplazar un valor del text enviado con base el regex
substring_with_regex(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com") # Received an email for [REDACTED]

# Regex que permite identificar dos grupos y posteriormente reemplazarlos en un orden inverso
substring_with_regex(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada") # Ada Lovelace


print(re.split(r"the|a", "One sentence. Another one? And the last one!"))