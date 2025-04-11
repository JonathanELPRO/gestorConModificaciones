import unittest
from unittest.mock import MagicMock
from Modelo.G_compra import TablaCompra  # Cambia 'tu_modulo' por el nombre del módulo donde está la clase TablaCompra


class TestTablaCompra(unittest.TestCase):

    def setUp(self):
        """Configura una tabla de compra para las pruebas."""
        self.tabla_compra = TablaCompra()

    def test_agregar_ticket_nuevo_usuario(self):
        """Prueba que se pueda agregar un ticket para un nuevo usuario."""
        # Crear un mock de Ticket
        ticket_mock = MagicMock()
        ticket_mock.id_ticket = 1
        ticket_mock.fecha = "2023-10-01"
        ticket_mock.obtener_total.return_value = 100  # Simular el método obtener_total

        self.tabla_compra.agregar_ticket(ticket_mock, identificador=1)

        self.assertEqual(len(self.tabla_compra.tickets), 2)
        self.assertIn(1, self.tabla_compra.tickets[0])  # Verifica que el usuario 1 esté en la tabla


    def test_obtener_tickets(self):
        """Prueba que se obtengan todos los tickets correctamente."""
        # Crear mocks de Ticket
        ticket_mock1 = MagicMock()
        ticket_mock1.id_ticket = 1
        ticket_mock1.fecha = "2023-10-01"
        ticket_mock1.obtener_total.return_value = 100

        ticket_mock2 = MagicMock()
        ticket_mock2.id_ticket = 2
        ticket_mock2.fecha = "2023-10-02"
        ticket_mock2.obtener_total.return_value = 200

        self.tabla_compra.agregar_ticket(ticket_mock1, identificador=1)
        self.tabla_compra.agregar_ticket(ticket_mock2, identificador=2)

        tickets = self.tabla_compra.obtener_tickets()
        self.assertEqual(len(tickets), 4)  # Debe haber 2 tickets en total

    def test_init_test(self):
        """Prueba que la inicialización de prueba funcione correctamente."""
        self.assertEqual(len(self.tabla_compra.tickets), 2)  # Debe haber 2 tickets iniciales
        self.assertIn(1, self.tabla_compra.tickets[0])  # Usuario 1 debe tener tickets
        self.assertIn(2, self.tabla_compra.tickets[1])  # Usuario 2 debe tener tickets


if __name__ == '__main__':
    unittest.main()