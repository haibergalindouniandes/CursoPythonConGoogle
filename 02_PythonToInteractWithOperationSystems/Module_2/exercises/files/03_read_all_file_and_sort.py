#!/usr/bin/env python3

# Funcion que abre el archivo, lo lee todo linea por linea y lo ordena
def read_all_file_line_by_line_and_sort(path_file):
    file = open(path_file)
    lines = file.readlines()
    file.close()
    lines.sort()
    print(lines)
            
print("read_all_file_line_by_line_and_sort => \n")
read_all_file_line_by_line_and_sort("./files/example.txt")   