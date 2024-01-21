#!/usr/bin/env python3

"""
La funcion with open("file_name", "w"), recibe dos parametros, el primero el nombre del archivo y el segundo es el modo (que podriamos asimilar los permisos).

Por ejemplo:

- Solo lectura => [r] Este el metodo default
- Solo escricura => [x] Genera error si el archivo existe, de lo contrario exclusivamente lo crea
- Solo escricura => [w] Se debe tener claro que con este modo se crea el archio y se elimina todo el contenido del archivo una vez se abre
- Agregar => [a] Agrega contenido al final solo si existe el archivo, de lo contrario genera error
- Lectura y escricura => [r+] Lee el archivo y permite escribir sobre este 

"""

# Funcion que crea un archivo con el contenido enviado, si se ejecuta la funcion varias veces, lo que hace es sobrescribir el archivo con el contenido enviado
def write_file(path, file_name, content):
    with open(f"{path}/{file_name}", "w") as file:
        file.write(content)


# Funcion que crea un archivo y lo abre con una codificacion especifica
def write_file_with_specific_encoding(path, file_name, content, encoding):
    with open(f"{path}/{file_name}", "w", encoding=encoding) as file:
        file.write(content)

write_file("./files" ,"write_example.txt", "It was a dark and stormy night")   
print("write_file => Se creo archivo correctamente \n")

write_file_with_specific_encoding("./files" ,"write_example.txt", "It was a dark and stormy night con codificacion", "utf-8")   
print("write_file_with_specifi_encoding => Se creo archivo con la codificacion correctamente \n")