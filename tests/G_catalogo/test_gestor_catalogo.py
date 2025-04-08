import unittest
from unittest.mock import MagicMock, patch
from Modelo.G_catalogo.GestorCatalogo import GestorCatalogo
from Modelo.G_catalogo.Catalogo import Catalogo
from Modelo.G_inventario.Producto import Producto, Aretes


class TestGestorCatalogo(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorCatalogo()

        self.mockTablaCatalogo = MagicMock()

        self.gestor.tabla_catalogo = self.mockTablaCatalogo

        productoFalso = Aretes("NombreX", "COD123", "MarcaZ", 10, "Plata", "Plateado", "Zirconia", 50)
        productoFalso2 = Aretes("NombreXy", "COD1234", "MarcaZY", 10, "Plata", "Plateado", "Zirconia", 50)

        self.mockTablaCatalogo.obtener_catalogo.return_value = [productoFalso,productoFalso2]
        self.mockTablaCatalogo.buscar_producto.return_value = [productoFalso]

    def tearDown(self):
        self.mockTablaCatalogo = None
        self.gestor = None

    def test_recibir_dato_catalogo_devuelve_catalogo_con_productos(self):
        catalogo = self.gestor.recibir_dato_catalogo("Aretes")
        self.assertEqual(len(catalogo.productos), 2)

    def test_recibir_dato_busqueda_devuelve_catalogo_con_productos(self):
        catalogo = self.gestor.recibir_dato_busqueda("MarcaZ")
        self.assertEqual(len(catalogo.productos), 1)
