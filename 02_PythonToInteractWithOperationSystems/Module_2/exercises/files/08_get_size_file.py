#!/usr/bin/env python3

import os

# Funcion que retorna el tamaño de un archivo en bytes
def get_size_file(path, file_name):
  return os.path.getsize(f"{path}/{file_name}")

file_size = get_size_file("./files" ,"example.txt")
print(f"El tamaño del archivo es => [{file_size}] bytes")