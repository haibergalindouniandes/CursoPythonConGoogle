#!/usr/bin/env python3

# Importamos la libreria psutil que nos permitira obtener la informacion del estado del CPU en un intervalo de tiempo
import psutil

print(psutil.cpu_percent(0.5))