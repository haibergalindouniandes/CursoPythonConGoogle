#!/usr/bin/env python3

import time
import os

# Funcion que crea un archivo con el contenido enviado, si se ejecuta la funcion varias veces, lo que hace es sobrescribir el archivo con el contenido enviado
def write_file(path, file_name, content):
    with open(f"{path}/{file_name}", "w") as file:
        file.write(content)
        
write_file("./files" ,"write_example_to_remove.txt", "It was a dark and stormy night - remove")   
print("write_file => Se creo archivo correctamente \n")

# Esperar 5 segunos para ejecutar la eliminacion
time.sleep(5)

# Funcion que elimina un archivo, si el archivo a eliminar no existe, generara un error
def remove_file(path, file_name):
    os.remove(f"{path}/{file_name}")

remove_file("./files" ,"write_example_to_remove.txt")   
print("remove_file => Se elimino archivo correctamente \n")
