#!/usr/bin/env python3

# Input Output Streams es la forma en que el programador o cualquier usuario en general interactua con una aplicacion 
# Input (enviando algun tipo de estimulo, como ingresar letras de un teclado, haciendo clic con un mouse, etc) y Output (recibiendo informacion, ya sea por pantalla, audito, etc)
data = input("Esto viene desde el STDIN (STANDAR INPUT): ")
print("Ahora escribimos esto como STDOUT (STANDAR OUTPUT):  " + data)
print("Ahora gemeramos un error STDERR (STANDAR ERROR):  " + data + 1)