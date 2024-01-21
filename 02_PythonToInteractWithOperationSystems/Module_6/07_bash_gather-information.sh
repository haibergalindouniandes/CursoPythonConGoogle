#!/bin/bash

# Bash que permite debuguear la información del PC
echo "Inicio: $(date)"; echo

echo "Procesos corriendo"; ps; echo

echo "Cuanto tiempo ha estado el computador prendido"; uptime; echo

echo "Memoria libre "; free; echo

echo "Usuarios conectados actualmente"; who; echo

echo "Finishing at: $(date)"
