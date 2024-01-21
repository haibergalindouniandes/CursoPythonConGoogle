#!/usr/bin/env python3

import time
import os

# Funcion que crea un archivo con el contenido enviado, si se ejecuta la funcion varias veces, lo que hace es sobrescribir el archivo con el contenido enviado
def write_file(path, file_name, content):
    with open(f"{path}/{file_name}", "w") as file:
        file.write(content)
        
write_file("./files" ,"write_example_to_rename.txt", "It was a dark and stormy night - rename")   
print("write_file => Se creo archivo correctamente \n")

# Funcion que renombra un archivo si existe, si no existe generara error
def rename_file(path, file_name, new_file_name):
    os.rename(f"{path}/{file_name}", f"{path}/{new_file_name}")
    
# Esperar 5 segunos para ejecutar la eliminacion
time.sleep(5)

rename_file("./files" ,"write_example_to_rename.txt", "file_rename_success.txt")
print("rename_file => Se renombro archivo correctamente \n")