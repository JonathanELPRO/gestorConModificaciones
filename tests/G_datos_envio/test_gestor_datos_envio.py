import unittest
from unittest.mock import MagicMock
from Modelo.G_datos_envio.GestorDatosEnvio import GestorDatosEnvio
from Modelo.G_datos_envio.DatoEnvio import DatoEnvio
from Modelo.G_datos_envio.TablaDatosEnvio import TablaDatosEnvio


class TestGestorDatosEnvio(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorDatosEnvio()
        self.gestor.tabla_datos_envio = MagicMock(spec=TablaDatosEnvio)

    def test_verificar_datos_envio_validos(self):
        self.assertTrue(self.gestor.verificar_datos_envio("Juan", "Calle Falsa 123", "La Paz", "12345", "Bolivia"))

    def test_verificar_datos_envio_invalidos(self):
        self.assertFalse(self.gestor.verificar_datos_envio("", "Calle Falsa 123", "La Paz", "12345", "Bolivia"))
        self.assertFalse(self.gestor.verificar_datos_envio("Juan", "", "La Paz", "12345", "Bolivia"))
        self.assertFalse(self.gestor.verificar_datos_envio("Juan", "Calle Falsa 123", "", "12345", "Bolivia"))
        self.assertFalse(self.gestor.verificar_datos_envio("Juan", "Calle Falsa 123", "La Paz", "", "Bolivia"))
        self.assertFalse(self.gestor.verificar_datos_envio("Juan", "Calle Falsa 123", "La Paz", "12345", ""))

    def test_recibir_datos_agregar_datos_envio_exitoso(self):
        self.gestor.verificar_datos_envio = MagicMock(return_value=True)

        nombre = "Juan"
        direccion = "Calle Falsa 123"
        ciudad = "La Paz"
        cp = "12345"
        pais = "Bolivia"
        resultado = self.gestor.recibir_datos_agregar_datos_envio(nombre, direccion, ciudad, cp, pais)

        self.assertTrue(resultado)

        self.gestor.tabla_datos_envio.agregar_dato_envio.assert_called_once()
        dato_envio_llamado = self.gestor.tabla_datos_envio.agregar_dato_envio.call_args[0][0]
        self.assertIsInstance(dato_envio_llamado, DatoEnvio)
        self.assertEqual(dato_envio_llamado.get_nombre(), nombre)
        self.assertEqual(dato_envio_llamado.get_direccion(), direccion)
        self.assertEqual(dato_envio_llamado.get_ciudad(), ciudad)
        self.assertEqual(dato_envio_llamado.get_codigo_postal(), cp)
        self.assertEqual(dato_envio_llamado.get_pais(), pais)

    def test_recibir_datos_agregar_datos_envio_fallo(self):
        self.gestor.verificar_datos_envio = MagicMock(return_value=False)
        resultado = self.gestor.recibir_datos_agregar_datos_envio("Juan", "", "La Paz", "12345", "Bolivia")
        self.assertFalse(resultado)

    def test_obtener_datos_envio(self):
        self.gestor.tabla_datos_envio.obtener_datos_envio.return_value = [DatoEnvio("Juan", "Calle Falsa 123", "La Paz", "12345", "Bolivia")]
        datos = self.gestor.obtener_datos_envio()
        self.assertEqual(len(datos), 1)
        self.assertEqual(datos[0].get_nombre(), "Juan")

    def test_recibir_modificacion(self):
        self.gestor.tabla_datos_envio.modificar_dato.return_value = True
        resultado = self.gestor.recibir_modificacion("nombre", "Carlos", 0)
        self.assertTrue(resultado)
        self.gestor.tabla_datos_envio.modificar_dato.assert_called_once_with("nombre", "Carlos", 0)

    def test_recibir_eliminar_dato(self):
        self.gestor.tabla_datos_envio.eliminar_dato.return_value = True
        resultado = self.gestor.recibir_eliminar_dato(0)
        self.assertTrue(resultado)
        self.gestor.tabla_datos_envio.eliminar_dato.assert_called_once_with(0)

    def tearDown(self):
        self.gestor = None  # Liberar la referencia al objeto GestorDatosEnvio



if __name__ == '__main__':
    unittest.main()
