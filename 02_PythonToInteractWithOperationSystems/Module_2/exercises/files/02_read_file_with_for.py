#!/usr/bin/env python3

# Funcion que abre el archivo, lo recorre linea por linea y lo convierte a mayuscula, pero al hacerlo linea por linea python agrega al final un salto de linea
def read_all_file_with_for_convert_upper(path_file):
    with open(path_file) as file:
        for line in file:
            print(line.upper())

# Funcion que abre el archivo, lo recorre linea por linea y lo convierte a mayuscula, agregando strip se elimina el salto de linea al final
def read_all_file_with_for_convert_upper_without_spaces(path_file):
    with open(path_file) as file:
        for line in file:
            print(line.strip().upper())
            
print("read_all_file_with_for_convert_upper => \n")
read_all_file_with_for_convert_upper("./files/example.txt")            

print("read_all_file_with_for_convert_upper_without_spaces => \n")
read_all_file_with_for_convert_upper_without_spaces("./files/example.txt")  