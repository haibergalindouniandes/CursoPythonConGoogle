import datetime
from utils import *

FILE_PATH = "../files/ticky_local.log"
NUMBER_OF_LOGS = 2000
USERNAMES_LIST = generate_random_usernames()
DATA_LIST = ["INFO: Created ticket [#XXXXXX] (USERNAME)", "ERROR: Connection to DB failed (USERNAME)", "ERROR: User request is invalid (USERNAME)",
               "ERROR: The system could not process the request (USERNAME)", "ERROR: The Ticket could not be generated since the data sent does not comply with the requested structure (USERNAME)",
               "ERROR: Could not connect to the internal ticket validation service (USERNAME)", "ERROR: The user does not have permissions to generate tickets (USERNAME)"]
PERCENTAGES_LIST = [34, 11, 11, 11, 11, 11, 11]

# Function que permite generar un archivo de log 
def generate_data_to_csv():
    init_date = datetime.datetime.now()
    print("<================================================================>")
    print(f"Fecha/hora de inicio de la generación de datos => [{init_date}]")
    # Logica de negocio
    for iterations in range(NUMBER_OF_LOGS):
        date_time_log = get_current_datetime_fomated()
        type_error = get_random_value_from_list_and_percentages(DATA_LIST, PERCENTAGES_LIST, 1)[0]
        username = get_random_value_from_list(USERNAMES_LIST)
        ticket_id = get_random_int(10000, 1000000)
        values_to_replace = [{"XXXXXX" : f"{ticket_id}"}, {"USERNAME" : f"{username}"}]
        log = f"{date_time_log} ubuntu.local ticky: {type_error}\n"
        log = replace_values_from_dict_list(values_to_replace, log)
        write_file(FILE_PATH, log)
    
    # Logica de negocio 
    final_date = datetime.datetime.now()
    time_process = final_date - init_date
    
    print(f"Fecha/hora de finlaización de la generación de datos => [{final_date}]")
    print(f"Se generarón => [{NUMBER_OF_LOGS}] registros")    
    print(f"La generación de data demoró => [{time_process.total_seconds()}]")
    print("<================================================================>")

generate_data_to_csv()    