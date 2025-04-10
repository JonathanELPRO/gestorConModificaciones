import unittest
from unittest.mock import MagicMock, patch
from Modelo.G_pago.TablaPago import TablaPago

class TestTablaPago(unittest.TestCase):

    @patch("Modelo.G_pago.TablaPago.Session")
    def setUp(self, mock_session_class):
        self.mock_session = MagicMock()
        self.mock_session.obtener_id_usuario.return_value = "usuario1"
        mock_session_class.return_value = self.mock_session
        self.tabla_pago = TablaPago()

    def test_agregar_tarjeta_nueva_sin_datos_envio(self):
        self.mock_session.obtener_id_usuario.return_value = "usuario1"
        tarjeta = MagicMock()
        result = self.tabla_pago.agregar_tarjeta(tarjeta)
        self.assertTrue(result)

    def test_agregar_tarjeta_con_datos_envio(self):
        self.mock_session.obtener_id_usuario.return_value = "usuario2"
        # Agrega datos de envío
        self.tabla_pago._TablaPago__pagos["usuario2"] = []
        tarjeta = MagicMock()
        result = self.tabla_pago.agregar_tarjeta(tarjeta)
        self.assertTrue(result)

    def test_obtener_tarjetas_existente(self):
        tarjeta = MagicMock()
        self.tabla_pago.agregar_tarjeta(tarjeta)
        tarjetas = self.tabla_pago.obtener_tarjetas()
        self.assertEqual(tarjetas, [tarjeta])

    def test_obtener_tarjetas_sin_datos(self):
        self.mock_session.obtener_id_usuario.return_value = "otro_usuario"
        tarjetas = self.tabla_pago.obtener_tarjetas()
        self.assertIsNone(tarjetas)

    def test_modificar_tarjeta_numero(self):
        tarjeta = MagicMock()
        self.tabla_pago.agregar_tarjeta(tarjeta)

        result = self.tabla_pago.modificar_tarjeta(0, "numero", "123")
        tarjeta.set_numero.assert_called_once_with("123")
        self.assertTrue(result)

    def test_modificar_tarjeta_fecha_vencimiento(self):
        tarjeta = MagicMock()
        self.tabla_pago.agregar_tarjeta(tarjeta)
        result = self.tabla_pago.modificar_tarjeta(0, "fecha_vencimiento", "12/24")
        tarjeta.set_fecha_vencimiento.assert_called_once_with("12/24")
        self.assertTrue(result)

    def test_modificar_tarjeta_cvv(self):
        tarjeta = MagicMock()
        self.tabla_pago.agregar_tarjeta(tarjeta)
        result = self.tabla_pago.modificar_tarjeta(0, "cvv", "456")
        tarjeta.set_cvv.assert_called_once_with("456")
        self.assertTrue(result)

    def test_modificar_tarjeta_sin_datos_pago(self):
        self.tabla_pago.__pagos = {}
        result = self.tabla_pago.modificar_tarjeta(0, "numero", "789")
        self.assertFalse(result)

    def test_eliminar_tarjeta(self):
        tarjeta = MagicMock()
        self.tabla_pago.agregar_tarjeta(tarjeta)
        result = self.tabla_pago.eliminar_tarjeta(0)
        self.assertTrue(result)
        self.assertEqual(self.tabla_pago._TablaPago__pagos["usuario1"], [])

    def test_eliminar_tarjeta_usuario_no_encontrado(self):
        tarjeta = MagicMock()
        self.tabla_pago.__pagos = {}
        result = self.tabla_pago.eliminar_tarjeta(0)
        self.assertFalse(result)
        self.assertEqual(self.tabla_pago._TablaPago__pagos, {})

    def test_tiene_datos_pago_true(self):
        tarjeta = MagicMock()
        self.tabla_pago.agregar_tarjeta(tarjeta)
        self.assertTrue(self.tabla_pago.tiene_datos_pago())

    def test_tiene_datos_pago_false(self):
        self.mock_session.obtener_id_usuario.return_value = "nuevo_usuario"
        self.assertFalse(self.tabla_pago.tiene_datos_pago())
