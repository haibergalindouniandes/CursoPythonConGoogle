#!/usr/bin/env python3

# Funcion que valida si el username enviado es de tipo string, tiene un tamaño mayor a 1 y es mayor al numero de caracteres enviados
def validate_user(username, minlen):
  assert type(username) == str, "el nombre de usuario debe ser un string"
  if minlen < 1:
    raise ValueError("minlen debe ser al menos 1")

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True
