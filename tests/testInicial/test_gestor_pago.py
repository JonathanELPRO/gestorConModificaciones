import unittest


class TestInicial(unittest.TestCase):

    def setUp(self):
        print("Configurando el entorno de las pruebas...")

    def test_inicial(self):
        print("Probando la validación de los datos...")
        pass

    def tearDown(self):
        print("Limpiando el entorno de las pruebas...")
