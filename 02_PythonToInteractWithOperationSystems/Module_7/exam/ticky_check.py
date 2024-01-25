#!/usr/bin/env python3

import csv
import re

FILE_PATH = "syslog.log"
error_count_info = {}
user_errors = {}

# with open(FILE_PATH) as f:
#     for line in f:
#         result = re.search(r"ERROR:\s(.*)\(", line)
#         if result is None:
#             continue
#         name = result[1].strip()
#         if name not in error_count_info:
#             error_count_info[name] = {}
#         sub_name = error_count_info[name] 
#         sub_name[result[1]] = sub_name.get(result[1], 0) + 1
#         error_count_info[name] = sub_name

def sort_dict(dict, reverse=False):
    return sorted(dict.items(), key=lambda item: item[0], reverse=reverse)

def count_logs_with_pattern(log_file, pattern):
    with open(log_file) as f:
        for line in f:
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[1].strip()
            error_count_info[name] = error_count_info.get(name, 0) + 1
    return error_count_info

def get_logs_with_pattern_groups(log_file, pattern, order_group, count_by_group):
    with open(log_file) as f:
        for line in f:
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[order_group].strip()
            if name not in user_errors:
                user_errors[name] = {"INFO" : 0, "ERROR" : 0}
            sub_name = user_errors[name]
            sub_name[result[count_by_group].strip()] = sub_name.get(result[count_by_group].strip(), 0) + 1
            user_errors[name] = sub_name
    return user_errors

# Funcion que permite escribir un archivo csv con todo el contenido
def write_csv_file_from_dic(path_file, data, keys):
    with open(path_file, 'w') as file:
        # Crear el objeto DictWriter
        writer = csv.DictWriter(file, fieldnames=keys)
        # Escribir la cabecera
        writer.writeheader()
        # Escribir los datos
        if isinstance(data, dict):
            for error, count in data.items():
                writer.writerow({'Error': error, 'Count': count})
        else:
            for username, error_info_dict in data:
                # Añadir el nombre de usuario a cada diccionario
                error_info_dict['Username'] = username
                writer.writerow(error_info_dict)

error_count_info_filename = "error_message.csv"
keys = ["Error", "Count"] 
data = count_logs_with_pattern(FILE_PATH, r"ERROR\s(.*)\(")
print(data)
print(type(data))
write_csv_file_from_dic(error_count_info_filename, data, keys)

error_count_info_filename = "user_statistics.csv"
keys = ["Username", "INFO", "ERROR"] 
data = sort_dict(get_logs_with_pattern_groups(FILE_PATH, r"(\s[A-Z]+\s)(.*)\((.*)\)", 3, 1))
print(data)
print(type(data))
write_csv_file_from_dic(error_count_info_filename, data, keys)