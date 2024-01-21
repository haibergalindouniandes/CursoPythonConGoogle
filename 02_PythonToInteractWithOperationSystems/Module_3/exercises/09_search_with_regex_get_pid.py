#!/usr/bin/env python3

import re

# Funcion que imprime la informacion buscada haciendo uso de regex y grupos
def search_with_regex_get_groups(data, pattern, group):
    result = re.search(pattern, data)
    if result is None:
        print("No se encontro ningun coincidencia")
    else:
        print(result[group])

# Regex que permite obtener el PID
search_with_regex_get_groups("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade", r"\[(\d+)\]", 1) # 12345
search_with_regex_get_groups("July 31 07:51:48 mycomputer bad_process[cage]: ERROR Performing package upgrade", r"\[(\d+)\]", 1) # No se encontro ningun coincidencia


import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)