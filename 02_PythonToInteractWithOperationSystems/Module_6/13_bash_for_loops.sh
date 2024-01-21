#!/bin/bash

# Recorre todos los archivos con la extensión '.HTM' en el directorio actual. 
# Para cada archivo, extrae el nombre del archivo sin la extensión y genera el nuevo nombre de archivo con la extensión '.html'. 
# Finalmente, imprime el comando mv que cambiaría el nombre del archivo original al nuevo nombre de archivo.
# for file in *.HTM; do
#   name=$(basename "$file" .HTM)
#   echo mv "$file" "$name.html" 
# done



# Recorre todos los archivos tipo log y procesarlos. 
# Analiza cada archivo de log en el directorio /var/log y muestra los 5 mensajes más frecuentes junto con sus recuentos.
for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done


# Lanzar por consola el comando:
# ./13_bash_for_loops.sh