#!/usr/bin/env python3

from validate_user import validate_user

try:
    # Se ejecuta correctamente, no lanza ninguna excepcion
    print(validate_user("zlaifer", 6)) # minlen debe ser al menos 1
except Exception as e:
    print("TypeError => [{}]".format(type(e)))
    print("Error => [{}]".format(e))

try:
    # Lanza una excepcion con base al assert type(username) == str
    print(validate_user([3], 1)) # el nombre de usuario debe ser un string
except Exception as e:
    print("TypeError => [{}]".format(type(e)))
    print("Error => [{}]".format(e))

try:
    # Lanza una excepcion con base a la validación minlen < 1
    print(validate_user("zlaifer", 0)) # minlen debe ser al menos 1
except Exception as e:
    print("TypeError => [{}]".format(type(e)))
    print("Error => [{}]".format(e))
