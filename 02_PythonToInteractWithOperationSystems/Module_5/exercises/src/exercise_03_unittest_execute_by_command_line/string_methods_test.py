#!/usr/bin/env python3
import unittest

# Clase que contiene los casos de pruebas de metodos del tipo string
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): 
            s.split(2)


if __name__ == '__main__':
    unittest.main()

# La interfaz de línea de comandos le permite interactuar con una aplicación o programa a través de la línea de comandos, 
# terminal o consola de su sistema operativo comenzando su código con un comando de texto. Cuando desee ejecutar pruebas en Python, 
# puede usar el módulo unittest desde la línea de comando para ejecutar pruebas desde módulos, clases o incluso métodos de prueba individuales. 
# Esto también le permite ejecutar varios archivos a la vez.  

# Para llamar a un módulo completo: python3 -m unittest test_module1 test_module2
# Para llamar a una clase de prueba: python3 -m unittest string_methods_test.TestStringMethods
# Para llamar a un método de prueba: python3 -m unittest string_methods_test.TestStringMethods.test_split
# Los módulos de prueba también se pueden llamar usando una ruta de archivo, como se escribe a continuación: python3 -m unittest tests/string_methods_test.py