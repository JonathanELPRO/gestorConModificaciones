import unittest
from Modelo.G_pago.TarjetaDebito import TarjetaDebito

class TestTarjetaDebito(unittest.TestCase):
    def test_tipo_tarjeta_debito(self):
        tarjeta = TarjetaDebito("9999888877776666", "03/27", "789")
        self.assertEqual(tarjeta.get_tipo(), "Debito")
