from Modelo.G_pago.GestorPago import GestorPago
import unittest

class TestGestorPago(unittest.TestCase):
    
    def setUp(self):
        self.gestor_pago = GestorPago()

    def test_validar_datos(self):
        self.assertTrue(self.gestor_pago.validar_datos("1234567812345678", "12/23", "123"))
        self.assertFalse(self.gestor_pago.validar_datos("12345678", "12/23", "123"))
        self.assertFalse(self.gestor_pago.validar_datos("1234567812345678", "12/2023", "123"))
        self.assertFalse(self.gestor_pago.validar_datos("1234567812345678", "12/23", "12"))
    
    def tearDown(self):
        del self.gestor_pago

