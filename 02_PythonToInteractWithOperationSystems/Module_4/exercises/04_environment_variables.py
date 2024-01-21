#!/usr/bin/env python3

import os

# Las variables de ambiente son valores dinamicos que proporcionan informacion sobre el entorno en que se ejecutan los programas

# Al ejecutarse por primera vez, solo se imprimira por pantalla la variable HOME en linux, ya que esta variable existe
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# Para agegar las variables SHELL y FRUIT se debe crear la variable de ambiente de la siguiente manera (LINUX):
# export SHELL=SELL
# export FRUIT=Pineapple

# Una vez creadas las variables de ambiente ejecutamos nuevamente la clase y ya obtendremos la informacion de dichas variables