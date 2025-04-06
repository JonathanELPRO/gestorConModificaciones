import unittest
from unittest.mock import patch
from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import *

class TestInventario(unittest.TestCase):
    def setUp(self):
        with patch.object(Inventario, 'inicializar_inventario', lambda x: None):
            self.inventario = Inventario()
        self.inventario.productos={"Aretes de diamante":23}
        self.productoEnCatalogo = Aretes("Aretes de diamante", "123ABCD", "MarcaXY", 23, "Diamante", "Diamante", "Diamante",30)
        self.inventario.productos_catalogo = [self.productoEnCatalogo]

    def tearDown(self):
        self.inventario.productos = {}
        self.inventario.productos_catalogo = []

    def test_agregar_producto_nuevo(self):
        productoNuevo = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)
        self.inventario.agregar_producto(productoNuevo)
        self.assertEqual(self.inventario.productos[productoNuevo.get_nombre()], 10)

    def test_agregar_producto_duplicado(self):
        productoDuplicado = Aretes("Aretes de diamante", "123ABCD", "MarcaXY", 23, "Diamante", "Diamante", "Diamante",30)
        self.inventario.agregar_producto(productoDuplicado)
        self.assertEqual(self.inventario.productos[productoDuplicado.get_nombre()], 46)

    def test_productos_inicializados_correctamente(self):
        self.inventario.inicializar_inventario()
        self.assertEqual(len(self.inventario.productos), 11)

    def test_eliminar_producto_existente(self):
        self.inventario.eliminar_producto("Aretes de diamante")
        self.assertNotIn("Aretes de diamante", self.inventario.productos)

    def test_eliminar_producto_no_existente(self):
        self.inventario.eliminar_producto("Aretes de Zafiro")
        self.assertNotIn("Aretes de Zafiro", self.inventario.productos)

    def test_buscar_producto_existente(self):
        self.assertEqual(self.inventario.buscar_producto("Aretes de diamante"),
                         "Aretes de diamante: 23")

    def test_buscar_producto_no_existente(self):
        self.assertEqual(self.inventario.buscar_producto("Aretes de Zafiro"),
                         "\nProducto no encontrado.")

    def test_actualizar_stock_producto_existente(self):
        self.inventario.actualizar_stock("Aretes de diamante", 10)
        self.assertEqual(self.inventario.productos["Aretes de diamante"], 33)

    def test_actualizar_stock_producto_no_existente(self):
        with patch("builtins.print") as mocked_print:
            self.inventario.actualizar_stock("Aretes de Zafiro", 10)
            mocked_print.assert_called_with("\nEl producto no existe en el inventario.")

    def test_obtener_inventario(self):
        inventario = self.inventario.obtener_inventario()
        self.assertEqual(inventario, self.inventario.productos)

    def test_obtener_lista_productos(self):
        productos_catalogo = self.inventario.obtener_lista_productos()
        self.assertEqual(productos_catalogo, self.inventario.productos_catalogo)

    def test_obtener_producto_con_nombre_existente(self):
        producto_obtenido = self.inventario.obtener_producto("Aretes de diamante")
        self.assertEqual(producto_obtenido.get_nombre(), self.productoEnCatalogo.get_nombre())

    def test_obtener_producto_con_modelo_existente(self):
        producto_obtenido = self.inventario.obtener_producto("123ABCD")
        self.assertEqual(producto_obtenido.get_nombre(), self.productoEnCatalogo.get_nombre())

    def test_obtener_producto_con_catalogo_vacio(self):
        self.inventario.productos_catalogo = []
        producto_obtenido = self.inventario.obtener_producto("230912AD")
        self.assertEqual(producto_obtenido, None)

    def test_obtener_producto_pasando_un_identificador_no_registrado(self):
        producto_obtenido = self.inventario.obtener_producto("230912AD")
        self.assertEqual(producto_obtenido, None)
