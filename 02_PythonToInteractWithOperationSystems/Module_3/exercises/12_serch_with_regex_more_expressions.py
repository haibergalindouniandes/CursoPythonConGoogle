#!/usr/bin/env python3

import re

"""
La función check_time verifica el formato de hora de un reloj de 12 horas, 
de la siguiente manera: la hora está entre 1 y 12, sin cero a la izquierda, seguida de dos puntos, 
luego minutos entre 00 y 59, luego un espacio opcional y luego AM o PM, en mayúsculas o minúsculas. 
"""

def validar_hora(hora):
    patron = re.compile(r"^(1[0-2]|0?[1-9]):([0-5][0-9]) ?([APap][Mm])$")

    if patron.match(hora):
        return True
    else:
        return False

# Ejemplos de uso:
hora1 = "3:45 PM"
hora2 = "10:30AM"
hora3 = "08:15am"
hora4 = "13:20 PM"

print(validar_hora(hora1))  # True
print(validar_hora(hora2))  # True
print(validar_hora(hora3))  # False (cero a la izquierda no permitido)
print(validar_hora(hora4))  # False (hora fuera del rango 1-12)



"""
La función contiene_acronym verifica la presencia de 2 o más caracteres o dígitos entre paréntesis en el texto, 
con al menos el primer carácter en mayúscula (si es una letra), y devuelve Verdadero si se cumple la condición, 
o Falso en caso contrario. Por ejemplo, 'La mensajería instantánea (IM) es un conjunto de tecnologías de comunicación 
utilizadas para la comunicación basada en texto' debería devolver Verdadero ya que (IM) satisface las condiciones de coincidencia'. 
"""
def contains_acronym(text):
  pattern = r"\([A-Z0-9][A-Za-z0-9]{1,}\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

"""
Estamos trabajando con un archivo CSV, que contiene información de los empleados. 
Cada registro tiene un campo de nombre, seguido de un campo de número de teléfono y un campo de función. 
El campo del número de teléfono contiene números de teléfono de EE. UU. y debe modificarse al formato internacional, con '+1-' delante del número de teléfono.
"""

def transform_record(record):
  new_record = re.sub(r'(\d{3}-\d+)', r'+1-\1', record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

"""
La función multi_vowel_words devuelve todas las palabras con 3 o más vocales consecutivas (a, e, i, o, u). Complete la expresión regular para hacer eso.
"""

def multi_vowel_words(text):
    pattern = r'(\w*[aeiou]{3}\w*)'
    result = re.findall(pattern, text)
    return result

# Ejemplos de uso:
print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []


"""
La función transform_comments convierte comentarios en un script de Python en aquellos que pueda utilizar un compilador de C. 
Esto significa buscar texto que comience con una almohadilla (#) y reemplazarlo con barras dobles (//), 
que es el indicador de comentario de una sola línea de C. Para los fines de este ejercicio, 
ignoraremos la posibilidad de que haya una marca de almohadilla incrustada dentro de un comando de 
Python y asumiremos que solo se usa para indicar un comentario. También queremos tratar las marcas hash repetitivas (##), (###), etc.
"""

import re
def transform_comments(line_of_code):
  result = re.sub(r'#+', r'//', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

"""
La función convert_phone_number busca un formato de número de teléfono de EE. UU.: XXX-XXX-XXXX (3 dígitos seguidos de un guión, 
3 dígitos más seguidos de un guión y 4 dígitos) y lo convierte a un formato más formal parecido a este: (XXX) XXX-XXXX. 
"""
def convert_phone_number(phone):
  result = re.sub(r'\s(\d{3})-(\d{3})-(\d{4})', r'(\1) \2-\3', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300