#!/bin/bash

# Validar si existe 127.0.0.1  en el archivo /etc/hosts
if grep "127\.0\.0\.1" /etc/hosts;
then 
    echo "Everything ok"
else 
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

# Validar si la varialbe de ambiente PATH no esta vacia
if [ -n "$PATH" ];
then 
    echo "Your path is not empty"
fi
