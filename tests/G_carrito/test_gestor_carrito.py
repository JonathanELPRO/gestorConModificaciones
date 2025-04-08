import unittest
from unittest.mock import MagicMock, patch

from Modelo.G_carrito import TablaCarritos
from Modelo.G_carrito.GestorCarrito import GestorCarrito
from Modelo.G_carrito.Carrito import Carrito
from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import Piercings


class TestGestorCarrito(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorCarrito()
        self.mockTabla = MagicMock(spec=TablaCarritos)
        self.mockCarrito = MagicMock(spec=Carrito)
        self.gestor.tabla_carritos = self.mockTabla
        self.gestor.carrito = self.mockCarrito

    def tearDown(self):
        self.mockTabla=None
        self.mockCarrito=None
        self.gestor=None

    def test_guardar_carrito(self):
        self.gestor.guardar_carrito()
        self.mockTabla.guardar_carrito.assert_called_with(self.mockCarrito)

    def test_obtener_carrito(self):
        carritoEsperado = MagicMock()
        self.mockTabla.obtener_ultimo_carrito.return_value = carritoEsperado
        resultado = self.gestor.obtener_carrito()
        self.assertEqual(resultado, carritoEsperado)

    def test_obtener_total(self):
        self.mockCarrito.obtener_total.return_value = 999.99
        total = self.gestor.obtener_total()
        self.assertEqual(total, 999.99)

    def test_agregar_producto_producto_no_encontrado(self):
        with patch("Modelo.G_carrito.GestorCarrito.Inventario") as mockInventarioClase:
            mockInventario = MagicMock(spec=Inventario)
            mockInventarioClase.return_value = mockInventario
            mockInventario.obtener_producto.return_value = None

            resultado = self.gestor.agregar_producto("modelo123", 1)

            self.assertFalse(resultado)


    def test_agregar_producto_producto_encontrado(self):
        with patch("Modelo.G_carrito.GestorCarrito.Inventario") as mockInventarioClase:
            producto = Piercings("Piercing de plata", "321BCD", "MarcaQ", 1, "Plata", "Plateado", "Zirconia", 35)

            mockInventario = MagicMock(spec=Inventario)

            mockInventario.obtener_producto.return_value = producto

            mockInventarioClase.return_value = mockInventario

            resultado = self.gestor.agregar_producto("Piercing de plata", 1)

            self.assertTrue(resultado)

    # def test_eliminar_producto_con_carrito(self):
    #     self.mockCarrito.eliminar_producto.return_value = None
    #     resultado = self.gestor.eliminar_producto("modeloABC")
    #     self.assertTrue(resultado)

    def test_eliminar_producto_con_carrito(self):
        # Simula que el carrito tiene productos
        producto = Piercings("Piercing de plata", "321BCD", "MarcaQ", 1, "Plata", "Plateado", "Zirconia", 35)
        self.mockCarrito.productos = [producto]
        self.mockCarrito.eliminar_producto.return_value = None

        resultado = self.gestor.eliminar_producto("modeloABC")

        self.assertTrue(resultado)
        self.mockCarrito.eliminar_producto.assert_called_with("modeloABC")

    def test_eliminar_producto_sin_carrito(self):
        self.gestor.carrito = None
        resultado = self.gestor.eliminar_producto("modeloABC")
        self.assertFalse(resultado)

    def test_limpiar_carrito(self):
        self.gestor.limpiar_carrito()
        self.mockCarrito.limpiar_carrito.assert_called()
        self.mockTabla.guardar_carrito.assert_called()
