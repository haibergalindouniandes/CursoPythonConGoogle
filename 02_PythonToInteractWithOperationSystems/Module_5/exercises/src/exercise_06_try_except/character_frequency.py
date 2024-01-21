#!/usr/bin/env python3

def character_frequency(filename):
  '''Cuenta la frecuencia de cada carácter en el archivo dado.'''
  # Primero intenta abrir el archivo
  try:
    f = open(filename)
  except OSError:
    return None

  # Ahora procesa el archivo
  characters = {}
  for line in f:
    for char in line:
      characters[char] = characters.get(char, 0) + 1
  f.close() 
  return characters