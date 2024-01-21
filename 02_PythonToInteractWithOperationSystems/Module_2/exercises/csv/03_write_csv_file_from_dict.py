#!/usr/bin/env python3
import csv

# Funcion que permite escribir un archivo csv con todo el contenido
def write_csv_file_from_dic(path_file, data, keys):
    with open(path_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
 
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"] 
path_file = "./csv/by_department.csv"

write_csv_file_from_dic(path_file, users, keys)
print(f"Se escribio archivo [{path_file}] correctamente\n")