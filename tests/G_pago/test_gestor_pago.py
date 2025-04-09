import unittest
from unittest.mock import patch, MagicMock
from Modelo.G_pago.GestorPago import GestorPago
from Modelo.G_pago.TarjetaCredito import TarjetaCredito
from Modelo.G_pago.TarjetaDebito import TarjetaDebito

class TestGestorPago(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorPago()

    # ---------- Pruebas de validar_datos ----------
    def test_validar_datos_correctos(self):
        self.assertTrue(self.gestor.validar_datos("1234567812345678", "12/25", "123"))

    def test_validar_datos_numero_invalido(self):
        self.assertFalse(self.gestor.validar_datos("123", "12/25", "123"))

    def test_validar_datos_fecha_invalida(self):
        self.assertFalse(self.gestor.validar_datos("1234567812345678", "1225", "123"))

    def test_validar_datos_cvv_invalido(self):
        self.assertFalse(self.gestor.validar_datos("1234567812345678", "12/25", "12"))

    # ---------- Pruebas de recibir_datos_bancarios_agregar ----------
    @patch("Modelo.G_pago.TablaPago.TablaPago.agregar_tarjeta")
    def test_agregar_tarjeta_credito_valida(self, mock_agregar):
        mock_agregar.return_value = True
        result = self.gestor.recibir_datos_bancarios_agregar("credito", "1234567812345678", "12/25", "123")
        self.assertTrue(result)
        mock_agregar.assert_called_once()
        tarjeta = mock_agregar.call_args[0][0]
        self.assertIsInstance(tarjeta, TarjetaCredito)

    @patch("Modelo.G_pago.TablaPago.TablaPago.agregar_tarjeta")
    def test_agregar_tarjeta_debito_valida(self, mock_agregar):
        mock_agregar.return_value = True
        result = self.gestor.recibir_datos_bancarios_agregar("debito", "1234567812345678", "12/25", "123")
        self.assertTrue(result)
        mock_agregar.assert_called_once()
        tarjeta = mock_agregar.call_args[0][0]
        self.assertIsInstance(tarjeta, TarjetaDebito)

    @patch("Modelo.G_pago.TablaPago.TablaPago.agregar_tarjeta")
    def test_agregar_tarjeta_datos_invalidos(self, mock_agregar):
        result = self.gestor.recibir_datos_bancarios_agregar("credito", "123", "1", "12")
        self.assertFalse(result)
        mock_agregar.assert_not_called()

    # ---------- Prueba de solicitud_obtener_tarjetas_bancarias ----------
    @patch("Modelo.G_pago.TablaPago.TablaPago.obtener_tarjetas")
    def test_obtener_tarjetas(self, mock_obtener):
        mock_obtener.return_value = ["tarjeta1", "tarjeta2"]
        result = self.gestor.solicitud_obtener_tarjetas_bancarias()
        self.assertEqual(result, ["tarjeta1", "tarjeta2"])
        mock_obtener.assert_called_once()

    # ---------- Prueba de recibir_datos_bancarios_modificar ----------
    @patch("Modelo.G_pago.TablaPago.TablaPago.modificar_tarjeta")
    def test_modificar_tarjeta(self, mock_modificar):
        mock_modificar.return_value = True
        result = self.gestor.recibir_datos_bancarios_modificar(0, "numero", "9876543210123456")
        self.assertTrue(result)
        mock_modificar.assert_called_once_with(0, "numero", "9876543210123456")

    # ---------- Prueba de recibir_datos_bancarios_eliminar ----------
    @patch("Modelo.G_pago.TablaPago.TablaPago.eliminar_tarjeta")
    def test_eliminar_tarjeta(self, mock_eliminar):
        mock_eliminar.return_value = True
        result = self.gestor.recibir_datos_bancarios_eliminar(0)
        self.assertTrue(result)
        mock_eliminar.assert_called_once_with(0)

if __name__ == "__main__":
    unittest.main()
