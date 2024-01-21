#!/usr/bin/env python3

import os
import datetime

# Funcion que retorna el la fcha de la ultima modificación del archivo en timestamp
def get_last_modified_file(path, file_name):
  return os.path.getmtime(f"{path}/{file_name}")

# Funcion que convierte timestamp en formato fecha
def convert_timestamp_to_datetime(timestamp):
  return datetime.datetime.fromtimestamp(timestamp)

last_modified_file_timestamp = get_last_modified_file("./files" ,"example.txt")
print(f"La ultima fecha de modificación en timestamp del archivo fue => [{last_modified_file_timestamp}]")

print(f"La ultima fecha de modificación del archivo fue => [{convert_timestamp_to_datetime(last_modified_file_timestamp)}]")