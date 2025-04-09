import unittest
from Modelo.G_pago.TarjetaCredito import TarjetaCredito

class TestTarjetaCredito(unittest.TestCase):
    def test_tipo_tarjeta_credito(self):
        tarjeta = TarjetaCredito("1111222233334444", "01/30", "456")
        self.assertEqual(tarjeta.get_tipo(), "Credito")
