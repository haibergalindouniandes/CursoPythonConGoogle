#!/bin/bash

# Imprimir los numero del 1 al 5
n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done

# Reintentos
n=0
# Accedemos al primer elemento enviado por la linea de comandos
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;

# En este caso se realizara la ejecucion de de los scripts hasta que se se cumpla con el loop while 
# Lanzar por consola el comando:
# ./12_bash_loops.sh ./11_random_exit.py