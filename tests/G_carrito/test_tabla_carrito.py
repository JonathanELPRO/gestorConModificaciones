import unittest
from unittest.mock import MagicMock

from Modelo.G_carrito import Carrito
from Modelo.G_carrito.TablaCarritos import TablaCarritos


class TestTablaCarritos(unittest.TestCase):
    def setUp(self):
        self.tablaCarritos = TablaCarritos()
        self.tablaCarritos.carritos = []

    def tearDown(self):
        self.tablaCarritos.carritos = []

    def test_guardar_carrito(self):
        carritoMock = MagicMock(spec=Carrito)
        self.tablaCarritos.guardar_carrito(carritoMock)
        self.assertIn(carritoMock, self.tablaCarritos.carritos)

    def test_obtener_ultimo_carrito(self):
        carritoMock1 = MagicMock()
        carritoMock2 = MagicMock()
        self.tablaCarritos.guardar_carrito(carritoMock1)
        self.tablaCarritos.guardar_carrito(carritoMock2)
        self.assertEqual(self.tablaCarritos.obtener_ultimo_carrito(), carritoMock2)

    def test_obtener_ultimo_carrito_vacio(self):
        self.assertIsNone(self.tablaCarritos.obtener_ultimo_carrito())

    def test_eliminar_carrito(self):
        carritoMock1 = MagicMock()
        carritoMock2 = MagicMock()
        self.tablaCarritos.guardar_carrito(carritoMock1)
        self.tablaCarritos.guardar_carrito(carritoMock2)
        self.tablaCarritos.eliminar_carrito()
        self.assertNotIn(carritoMock2, self.tablaCarritos.carritos)









