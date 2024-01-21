import unittest
import os
import shutil

# Funcion a probar
def simple_addition(a, b):
	return a + b

# Rutas para operaciones de archivos
ORIGINAL_FILE_PATH = "./files/init/original_test_file.txt"
COPIED_FILE_PATH = "./files/final/copied_test_file.txt"


# Las pruebas pueden llevar mucho tiempo, pero hay formas de optimizar el proceso de prueba. Los siguientes métodos y módulos le permiten definir 
# instrucciones que se ejecutan antes y después de cada método de prueba:
# setUp() se puede llamar automáticamente con cada prueba que se ejecuta para configurar el código.
# TearDown() ayuda a limpiar después de ejecutar la prueba.

# Este método se ejecutará una vez antes de cualquier prueba o clase de prueba.
def setUpModule():
    global COUNTER
    COUNTER = 0
    
    # Crea un archivo en /tmp
    with open(ORIGINAL_FILE_PATH, 'w') as file:
        file.write("Test Results:\n")

# Este método se ejecutará una vez después de todas las pruebas y clases de prueba.    
def tearDownModule():    
    # Copiar el archivo a otro directorio
    shutil.copy2(ORIGINAL_FILE_PATH, COPIED_FILE_PATH)
    
    # Eliminar el archivo original
    os.remove(ORIGINAL_FILE_PATH)
    
    
class TestSimpleAddition(unittest.TestCase):

    # Este método se ejecutará antes de cada prueba individual.
    def setUp(self):
        global COUNTER
        COUNTER += 1    
        
    # Este método se ejecutará después de cada prueba individual.
    def tearDown(self):
        # Agregar el resultado de la prueba al archivo
        with open(ORIGINAL_FILE_PATH, 'a') as file:
            result = "PASSED" if self._outcome.success else "FAILED"
            file.write(f"Test {COUNTER}: {result}\n")

    def test_add_positive_numbers(self):
        self.assertEqual(simple_addition(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(simple_addition(-3, -4), -7)

# Ejecutando las pruebas
suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleAddition)
runner = unittest.TextTestRunner()
runner.run(suite)

# Leer el archivo copiado para mostrar los resultados.
with open(COPIED_FILE_PATH, 'r') as result_file:
    test_results = result_file.read()

print(test_results)		        