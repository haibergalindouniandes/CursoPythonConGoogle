import re
from faker import Faker
import datetime
import random

faker = Faker()

# Función que genera un listado de nombres
def generate_random_usernames():
    users_to_generate = 20
    usernames_list = []
    for i in range(users_to_generate):
        usernames_list.append(faker.name())        
    return usernames_list

# print(generate_random_usernames())

# Función que gpermite obetner la fecha y hora fomateada
def get_current_datetime_fomated():
    # Obtener la fecha y hora actual
    # date_time = datetime.datetime.now()
    
    # Definir la fecha de inicio y fin
    init_date = datetime.datetime(2023, 12, 1, 0, 0, 0)
    final_date = datetime.datetime(2023, 12, 31, 23, 59, 59)
    
    # Calcular un número aleatorio de segundos dentro del rango
    random_seconds = random.randint(0, (final_date - init_date).total_seconds())

    # Sumar el número aleatorio de segundos a la fecha de inicio
    date_time = init_date + datetime.timedelta(seconds=random_seconds)

    # Formatear la fecha y hora según el formato deseado
    date_time_formateada = date_time.strftime("%b %d %H:%M:%S")

    return date_time_formateada

# print(get_current_datetime_fomated())

# Función que retorna un entero aleatorio
def get_random_int(init_int, final_int):
    return random.randint(init_int, final_int)

# Función que retorna un valor aleatorio con base a una lista
def get_random_value_from_list(data_list):
    return random.choice(data_list)

# Función que retorna un valor aleatorio con base a una lista y el porcentage de ocurrencia
def get_random_value_from_list_and_percentages(data_list, percentages_list, number_results):
    """
    Genera datos aleatorios basados en una lista y los porcentajes de ocurrencia.
    
    Args:
    - data_list: Lista de elementos para generar datos aleatorios.
    - percentages_list: Lista de porcentajes asociados a cada elemento de la lista.

    Returns:
    - Datos generados aleatoriamente.
    """
    if len(data_list) != len(percentages_list):
        raise ValueError("La longitud de la lista y los porcentajes debe ser la misma.")

    # Normalizar los porcentajes para que sumen 1
    normalized_percentages = [p / sum(percentages_list) for p in percentages_list]

    # Generar datos aleatorios según los porcentajes
    generated_data = random.choices(data_list, weights=normalized_percentages, k=number_results)  # Ajusta la cantidad según sea necesario

    return generated_data

# DATA_LIST = ["INFO: Created ticket [#XXXXXX] (USERNAME)", "ERROR: Connection to DB failed (USERNAME)", "ERROR: User request is invalid (USERNAME)",
#                "ERROR: The system could not process the request (USERNAME)", "ERROR: The Ticket could not be generated since the data sent does not comply with the requested structure (USERNAME)",
#                "ERROR: Could not connect to the internal ticket validation service (USERNAME)", "ERROR: The user does not have permissions to generate tickets (USERNAME)"]
# PERCENTAGES_LIST = [34, 11, 11, 11, 11, 11, 11]
# print(get_random_value_from_list_and_percentages(DATA_LIST, PERCENTAGES_LIST, 10))

# Funcion que permite agregar información al final de un archivo
def write_file(path_path, content):
    with open(path_path, "a") as file:
        file.write(content)

# Funcion que permite identificar y remplazar una lista de valores
def replace_values_from_dict_list(dict_list, data):   
    for element_dict in dict_list:
        for key, value in element_dict.items():
            if key in data:
                data = data.replace(key, value)
    
    return data

# dict_list = [{'#XXXXXX' : '1212233'}, {'USERNAME' : 'ZLAIFER'}]
# data = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#XXXXXX] (USERNAME)"
# data2 = "May 27 11:45:40 ubuntu.local ticky: ERROR: Connection to DB failed (USERNAME)"
# print(replace_values_from_dict_list(dict_list, data))
# print(replace_values_from_dict_list(dict_list, data2))

# Funcion que permite obtener informacion a traves del regex y contar las incidencias encontradas guardando la informacion en un diccionario
def count_logs_with_pattern(log_file, pattern):
    data_obtained = {}
    with open(log_file) as f:
        for line in f:
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[1].strip()
            data_obtained[name] = data_obtained.get(name, 0) + 1
    return data_obtained
    
# print(count_logs_with_pattern("../files/ticky_local.log", r"ERROR:\s(.*)\(", 1))

# Funcion que order un diccionario con base a su valor de forma descendente o ascendente
def sort_dict(dict, reverse=False):
    return sorted(dict.items(), key=lambda item: item[0], reverse=reverse)

# dict_to_order = {'The Ticket could not be generated since the data sent does not comply with the requested structure': 227, 'User request is invalid': 243, 'The system could not process the request': 221, 'Could not connect to the internal ticket validation service': 255, 'Connection to DB failed': 247, 'The user does not have permissions to generate tickets': 249}
# print(sort_dict(dict_to_order)) # Ordenar de forma descendente
# print(sort_dict(dict_to_order, True)) # Ordenar de forma ascendente

# Funcion que permite obtener informacion a traves del regex y contar las incidencias encontradas guardando la informacion en un diccionario
def get_logs_with_pattern_groups(log_file, pattern, order_group, count_by_group):
    data_obtained = {}
    with open(log_file) as f:
        for line in f:
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[order_group].strip()
            if name not in data_obtained:
                data_obtained[name] = {}
            sub_name = data_obtained[name] 
            sub_name[result[count_by_group]] = sub_name.get(result[count_by_group], 0) + 1
            data_obtained[name] = sub_name
    return data_obtained

ordered_list_of_usernames = sort_dict(get_logs_with_pattern_groups("../files/ticky_local.log", r":\s(\w+): (.*)\((.*)\)", 3, 1))
# for item in ordered_list_of_usernames:
#     print(item)
#     print(item[0])
#     print(item[1])
 