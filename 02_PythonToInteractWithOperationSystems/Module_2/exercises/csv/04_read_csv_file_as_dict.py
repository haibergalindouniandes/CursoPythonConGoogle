#!/usr/bin/env python3
import csv

# Funcion que permite leer un archivo csv como si fuera un diccionario
def read_csv_file_as_dict(path_file):
    with open(path_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Name: {}, Username: {}, Department: {}".format(row["name"], row["username"],row["department"]))
 
path_file = "./csv/by_department.csv"

read_csv_file_as_dict(path_file)