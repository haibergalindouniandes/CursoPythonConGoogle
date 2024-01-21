#!/usr/bin/env python3

# Funcion que abre el archivo, e imprime las primeras 3 lineas
def read_file_line_by_line(path_file):
    file = open(path_file)
    print(file.readline())
    print(file.readline())
    print(file.readline())
    file.close()

# Funcion que abre el archivo, e imprime la primera linea
def read_all_file(path_file):
    with open(path_file) as file:
        print(file.read())
    
# Ejecutar lectura del archivo
print("read_file_line_by_line => \n")
read_file_line_by_line("./files/example.txt")
print("read_all_file => \n")
read_all_file("./files/example.txt")

