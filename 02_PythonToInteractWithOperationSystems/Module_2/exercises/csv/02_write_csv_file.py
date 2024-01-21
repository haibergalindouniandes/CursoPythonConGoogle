#!/usr/bin/env python3
import csv

# Funcion que permite escribir un archivo csv con todo el contenido
def write_csv_file(path_file, data):
    with open(path_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)
 
# Funcion que permite escribir un archivo csv registro por registro
def write_csv_file_row_by_row(path_file, data):
    with open(path_file, 'w') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
   
hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]         
path_file = "./csv/hosts.csv"

write_csv_file(path_file, hosts)
print(f"Se escribio archivo [{path_file}] correctamente\n")

path_file = "./csv/hosts_row_by_row.csv"
write_csv_file_row_by_row(path_file, hosts)
print(f"Se escribio archivo [{path_file}] correctamente")