#!/usr/bin/env python3

import sys
import os
import re

def error_search(log_file):
  """
  Para permitirnos buscar cualquier tipo de registro en todos los archivos de registro, haremos que nuestro script sea consistente y dinámico.
  Defina una función de entrada para recibir el tipo de ERROR que el usuario final desea buscar y asignar a una variable denominada error.
  La función input() toma la entrada del usuario y luego evalúa la expresión. Esto significa que Python identifica automáticamente si el usuario ingresó una cadena, un número o una lista. Si la entrada proporcionada no es correcta, Python generará un error de sintaxis o una excepción. El flujo del programa se detendrá hasta que el usuario haya dado una entrada.
  Más adelante en el script, iteraremos sobre esta entrada del usuario y el archivo de registro para producir resultados. Siguiendo la función de entrada, ahora inicialice la lista de errores_devueltos. Esto incluirá todos los registros de ERROR especificados por el usuario final a través de la función de entrada.
  """
  error = input("What is the error? ")
  returned_errors = []
  
  """
  Utilice los métodos de manejo del archivo Python para abrir el archivo de registro en modo de lectura y utilice la codificación 'UTF-8'.
  """
  with open(log_file, mode='r',encoding='UTF-8') as file:
    """
    Ahora leeremos cada registro por separado del archivo fishy.log usando el método readlines(). Como se mencionó anteriormente, iteraremos sobre la entrada del usuario para obtener los resultados de búsqueda deseados. Para esto, crearemos una lista para almacenar todos los patrones (entrada del usuario) que se buscarán. Esta lista se denomina error_patterns e inicialmente tiene un patrón 'error' para filtrar solo todos los registros de ERROR. Puede cambiar esto para ver otros tipos de registros, como INFORMACIÓN y ADVERTENCIA. También puede vaciar e inicializar la lista para recuperar todos los tipos de registros, independientemente de su tipo.
    Agregaremos toda la entrada del usuario a esta lista error_patterns.
    """
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

      """
      Ahora, usemos el método search() (presente en el módulo re) para verificar si el archivo fishy.log tiene el patrón definido por el usuario y, si está disponible, añádalo a la lista de errores_devueltos.
      """
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
        
    """
    A continuación, cierre el archivo fishy.log y devuelva los resultados almacenados en la lista de errores_devueltos.
    """
    file.close()
  return returned_errors


"""
Definamos otra función file_output que toma los errores devueltos, devueltos por una función anterior, como parámetro formal.
"""
def file_output(returned_errors):
  """
  Utilizando los métodos de manejo de archivos de Python, escriba devueltos_errors en el archivo errores_found.log abriendo el archivo en modo de escritura. Para definir el archivo de salida, usaremos el método os.path.expanduser ('
  '), que devuelve el directorio de inicio de la instancia de su sistema. Luego, concatenaremos esta ruta (al directorio de inicio) al archivo errores_found.log en el directorio /data.
  """
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    """
    A continuación, escriba todos los registros en el archivo de salida iterando sobre return_errors.
    """
    for error in returned_errors:
      file.write(error)
    """
    Y finalmente, cierre el archivo.
    """
    file.close()

if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
