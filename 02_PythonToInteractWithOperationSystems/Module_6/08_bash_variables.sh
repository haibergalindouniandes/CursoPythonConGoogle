#!/bin/bash

# Bash que permite debuguear la información del PC

# Creacion y asignación de variable
separator="----------------------------------------------"

echo "Inicio: $(date)"; echo $separator

echo "Procesos corriendo"; ps; echo $separator

echo "Cuanto tiempo ha estado el computador prendido"; uptime; echo $separator

echo "Memoria libre "; free; echo $separator

echo "Usuarios conectados actualmente"; who; echo $separator

echo "Finishing at: $(date)"