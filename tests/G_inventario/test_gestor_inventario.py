import unittest
from unittest.mock import patch, MagicMock
from Modelo.G_inventario.GestorInventario import GestorInventario
from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import *

class TestGestorInventario(unittest.TestCase):
    def setUp(self):
        with patch.object(Inventario, 'inicializar_inventario', lambda x: None):
            self.mockInventario = MagicMock(spec=Inventario)
        self.gestor = GestorInventario()
        self.gestor.Inventario = self.mockInventario
        self.productoPrueba = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)

    def tearDown(self):
        self.mockInventario = None
        self.gestor = None
        self.productoPrueba = None

    def test_agregar_producto(self):
        self.mockInventario.agregar_producto.return_value = None
        self.gestor.Inventario.obtener_inventario.return_value = {"Aretes de plata": 10}
        self.gestor.agregar_producto(self.productoPrueba)
        self.assertIn(self.productoPrueba.nombre, self.gestor.Inventario.obtener_inventario())

    def test_eliminar_producto(self):
        self.mockInventario.obtener_inventario.return_value = {self.productoPrueba.nombre: self.productoPrueba.stock}
        self.gestor.eliminar_producto(self.productoPrueba.nombre)
        self.mockInventario.obtener_inventario.return_value = {}
        self.assertNotIn(self.productoPrueba.nombre, self.gestor.Inventario.obtener_inventario())

    def test_buscar_producto(self):
        self.mockInventario.buscar_producto.return_value = "Aretes de plata: 10"
        self.assertEqual("Aretes de plata: 10", self.gestor.buscar_producto(self.productoPrueba.nombre))

    def test_obtener_inventario(self):
        self.mockInventario.obtener_inventario.return_value = {self.productoPrueba.nombre: self.productoPrueba.stock}
        self.assertEqual(self.gestor.obtener_inventario(), {self.productoPrueba.nombre: self.productoPrueba.stock})

    def test_actualizar_stock_nombre_presente_en_catalogo(self):
        self.gestor.Inventario.productos_catalogo = [self.productoPrueba]
        self.gestor.actualizar_stock(self.productoPrueba.nombre, self.productoPrueba.stock)
        self.mockInventario.actualizar_stock.assert_called_once_with(self.productoPrueba.nombre,
                                                                     self.productoPrueba.stock)

    def test_actualizar_stock_nombre_no_presente_en_catalogo(self):
        self.gestor.Inventario.productos_catalogo = [self.productoPrueba]
        self.gestor.actualizar_stock("Aretes de oro", 21)
        self.mockInventario.actualizar_stock.assert_called_once_with("Aretes de oro", 21)

    def test_actualizar_stock_catalogo_vacio(self):
        self.gestor.Inventario.productos_catalogo = []
        self.gestor.actualizar_stock(self.productoPrueba.nombre, self.productoPrueba.stock)
        self.mockInventario.actualizar_stock.assert_called_once_with(self.productoPrueba.nombre,
                                                                     self.productoPrueba.stock)

