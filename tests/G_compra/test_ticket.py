import unittest
from Modelo.G_inventario.Producto import Producto  # Asegúrate de que esta importación sea correcta
from Modelo.G_compra import Ticket  # Cambia 'tu_modulo' por el nombre del módulo donde está la clase Ticket

class TestTicket(unittest.TestCase):

    def setUp(self):
        """Configura un ticket para las pruebas."""
        self.ticket = Ticket(id_ticket=1, fecha="2023-10-01")

    def test_agregar_producto(self):
        """Prueba que se pueda agregar un producto al ticket."""
        self.ticket.agregar_producto(modelo="Producto A", cantidad=2, precio=50)
        self.assertEqual(len(self.ticket.productos), 1)
        self.assertEqual(self.ticket.productos[0]["modelo"], "Producto A")
        self.assertEqual(self.ticket.productos[0]["cantidad"], 2)
        self.assertEqual(self.ticket.productos[0]["precio"], 50)

    def test_obtener_total(self):
        """Prueba que se calcule el total correctamente."""
        self.ticket.agregar_producto(modelo="Producto A", cantidad=2, precio=50)
        self.ticket.agregar_producto(modelo="Producto B", cantidad=1, precio=100)
        total = self.ticket.obtener_total()
        self.assertEqual(total, 200)  # (2 * 50) + (1 * 100)

    def test_obtener_productos(self):
        """Prueba que se obtengan los productos correctamente."""
        self.ticket.agregar_producto(modelo="Producto A", cantidad=2, precio=50)
        productos = self.ticket.obtener_productos()
        self.assertEqual(len(productos), 1)
        self.assertEqual(productos[0]["modelo"], "Producto A")

    def test_str(self):
        """Prueba la representación en cadena del ticket."""
        self.ticket.agregar_producto(modelo="Producto A", cantidad=2, precio=50)
        self.assertEqual(str(self.ticket), "Ticket: 1 - 2023-10-01 - 100")  # 2 * 50 = 100

if __name__ == '__main__':
    unittest.main()