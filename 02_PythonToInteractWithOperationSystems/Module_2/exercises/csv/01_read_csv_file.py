#!/usr/bin/env python3
import csv

# Funcion que permite leer un csv e imprime todos los registros dentro de este
def read_data_into_csv(path_file):
    with open(path_file) as file:
        csv_f = csv.reader(file)
        for row in csv_f:
            id,	name, phone, email, rol = row
            print("ID: {}, Name: {}, Phone: {}, Email: {}, Rol: {}".format(id, name, phone, email, rol))
         
# Funcion que permite leer un csv e imprime todos los registros dentro de este exceptual el primer registro que se asume es el header del archivo
def read_data_into_csv_without_header(path_file):
    with open(path_file) as file:
        csv_f = csv.reader(file)
        for index, row in enumerate(csv_f):
            if index > 0:
                id,	name, phone, email, rol = row
                print("ID: {}, Name: {}, Phone: {}, Email: {}, Rol: {}".format(id, name, phone, email, rol))
         
print(f"read_data_into_csv => \n")
read_data_into_csv("./csv/mock_data_10_records.csv")

print(f"\nread_data_into_csv => \n")
read_data_into_csv_without_header("./csv/mock_data_10_records.csv")