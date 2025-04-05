import unittest
from Modelo.G_inventario.Producto import *

class TestProducto(unittest.TestCase):
    def setUp(self):
        self.producto = Producto(
            nombre="Aretes de Oro",
            modelo="A20000",
            marca="Nivea",
            stock="8",
            material="Oro",
            color="Amarillo",
            piedra="Diamante",
            precio=1000
        )

    def tearDown(self):
        self.producto = None

    def test_get_nombre(self):
        self.assertEqual(self.producto.get_nombre(), "Aretes de Oro")

    def test_get_modelo(self):
        self.assertEqual(self.producto.get_modelo(), "A20000")

    def test_get_marca(self):
        self.assertEqual(self.producto.get_marca(), "Nivea")

    def test_get_stock(self):
        self.assertEqual(self.producto.get_stock(), "8")

    def test_get_material(self):
        self.assertEqual(self.producto.get_material(), "Oro")

    def test_get_color(self):
        self.assertEqual(self.producto.get_color(), "Amarillo")

    def test_get_piedra(self):
        self.assertEqual(self.producto.get_piedra(), "Diamante")

    def test_get_precio(self):
        self.assertEqual(self.producto.get_precio(), 1000)

    def test_set_stock(self):
        self.producto.set_stock("9")
        self.assertEqual(self.producto.get_stock(), "9")

    def test_str(self):
        expected_str = (
            "Nombre: Aretes de Oro\n"
            "Modelo: A20000\n"
            "Marca: Nivea\n"
            "Stock: 8\n"
            "Material: Oro\n"
            "Color: Amarillo\n"
            "Piedra: Diamante\n"
            "Precio: 1000"
        )
        self.assertEqual(str(self.producto), expected_str)
