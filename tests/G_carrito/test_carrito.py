import unittest
from unittest.mock import MagicMock, patch
from Modelo.G_carrito.Carrito import Carrito


class TestCarrito(unittest.TestCase):
    def setUp(self):
        self.carrito = Carrito()
        self.carrito.productos= [
            {
                "modelo": "J001",
                "nombre": "Anillo de plata",
                "precio": 150.0,
                "cantidad": 2
            },
            {
                "modelo": "J002",
                "nombre": "Collar de oro",
                "precio": 950.0,
                "cantidad": 1
            }
        ]

    def tearDown(self):
        self.carrito.productos = None
        self.carrito = None

    def test_agregar_producto(self):
        producto_mock = MagicMock()
        producto_mock.get_modelo.return_value = "J003"
        producto_mock.get_nombre.return_value = "Pulsera de perlas"
        producto_mock.get_precio.return_value = 300.0

        self.carrito.agregar_producto(producto_mock, "3")

        self.assertEqual(len(self.carrito.productos),3)

    def test_eliminar_producto_existente(self):
        self.carrito.eliminar_producto("Anillo de plata")
        self.assertEqual(len(self.carrito.productos),1)

    def test_eliminar_producto_no_existente(self):
        self.carrito.eliminar_producto("Pulsera de cuero")  # No existe
        self.assertEqual(len(self.carrito.productos), 2)


    def test_eliminar_producto_carrito_vacio(self):
        self.carrito.productos = []
        self.carrito.eliminar_producto("Anillo de plata")
        self.assertEqual(len(self.carrito.productos), 0)

    def test_obtener_carrito(self):
        self.assertEqual(self.carrito.obtener_carrito(),self.carrito.productos)

    def test_obtener_total_carrito_no_vacio(self):
        self.assertEqual(self.carrito.obtener_total(),1250.0)

    def test_obtener_total_carrito_vacio(self):
        self.carrito.productos=[]
        self.assertEqual(self.carrito.obtener_total(),0)

    def test_limpiar_carrito(self):
        self.carrito.limpiar_carrito()
        self.assertEqual(len(self.carrito.productos),0)

    def test_mostrar_carrito_con_dos_productos(self):
        with patch("builtins.print") as mocked_print:
            self.carrito.mostrar_carrito()
            output = "".join([call[0][0] for call in mocked_print.call_args_list])
            self.assertEqual(output,"\n=== Carrito ===\nProducto: Anillo de plata Precio: 150.0 Cantidad: 2Producto: Collar de oro Precio: 950.0 Cantidad: 1\nTotal: 1250.0")

    def test_mostrar_carrito_con_un_producto(self):
        self.carrito.productos = [
            {
                "modelo": "J001",
                "nombre": "Anillo de plata",
                "precio": 150.0,
                "cantidad": 2
            }
        ]
        with patch("builtins.print") as mocked_print:
            self.carrito.mostrar_carrito()
            output = "".join([call[0][0] for call in mocked_print.call_args_list])
            self.assertEqual(output,"\n=== Carrito ===\nProducto: Anillo de plata Precio: 150.0 Cantidad: 2\nTotal: 300.0")

    def test_mostrar_carrito_vacio(self):
        self.carrito.productos=[]
        with patch("builtins.print") as mocked_print:
            self.carrito.mostrar_carrito()
            mocked_print.assert_called_with("\nCarrito vacío")











