import unittest
from Modelo.G_pago.TarjetaBancaria import TarjetaBancaria

class TestTarjetaBancaria(unittest.TestCase):
    def setUp(self):
        self.tarjeta = TarjetaBancaria("1234567812345678", "12/25", "123")

    def test_get_numero(self):
        self.assertEqual(self.tarjeta.get_numero(), "1234567812345678")

    def test_set_numero(self):
        self.tarjeta.set_numero("1111222233334444")
        self.assertEqual(self.tarjeta.get_numero(), "1111222233334444")

    def test_get_fecha_vencimiento(self):
        self.assertEqual(self.tarjeta.get_fecha_vencimiento(), "12/25")

    def test_set_fecha_vencimiento(self):
        self.tarjeta.set_fecha_vencimiento("01/30")
        self.assertEqual(self.tarjeta.get_fecha_vencimiento(), "01/30")

    def test_get_cvv(self):
        self.assertEqual(self.tarjeta.get_cvv(), "123")

    def test_set_cvv(self):
        self.tarjeta.set_cvv("999")
        self.assertEqual(self.tarjeta.get_cvv(), "999")
