#!/usr/bin/env python3
# Importamos la libreria shutil que nos permitira obtener la informacion de almacenameinto
import shutil

du = shutil.disk_usage('/')
print(du)
# Imprimir el espacio libre en GB
print(du.free/du.total*100)
