import unittest
from unittest.mock import patch
from Modelo.G_datos_envio.TablaDatosEnvio import TablaDatosEnvio

# Creamos una clase auxiliar para simular DatoEnvio
class FakeDatoEnvio:
    def __init__(self, nombre='', direccion='', ciudad='', codigo_postal='', pais=''):
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.pais = pais

    def set_nombre(self, value): self.nombre = value
    def set_direccion(self, value): self.direccion = value
    def set_ciudad(self, value): self.ciudad = value
    def set_codigo_postal(self, value): self.codigo_postal = value
    def set_pais(self, value): self.pais = value


class TestTablaDatosEnvio(unittest.TestCase):

    @patch('Modelo.G_datos_envio.TablaDatosEnvio.Session')
    def setUp(self, mock_session):
        self.mock_session = mock_session.return_value
        self.mock_session.obtener_id_usuario.return_value = 1

        self.tabla = TablaDatosEnvio()

    def test_agregar_dato_envio(self):
        dato = FakeDatoEnvio(nombre="Juan")
        resultado = self.tabla.agregar_dato_envio(dato)

        self.assertTrue(resultado)
        self.assertIn(1, self.tabla.tabla_datos_envio)
        self.assertEqual(len(self.tabla.tabla_datos_envio[1]), 1)
        self.assertEqual(self.tabla.tabla_datos_envio[1][0].nombre, "Juan")

    def test_obtener_datos_envio_existente(self):
        dato = FakeDatoEnvio(nombre="Maria")
        self.tabla.agregar_dato_envio(dato)

        datos = self.tabla.obtener_datos_envio()
        self.assertEqual(len(datos), 1)
        self.assertEqual(datos[0].nombre, "Maria")

    def test_obtener_datos_envio_inexistente(self):
        self.mock_session.obtener_id_usuario.return_value = 999
        datos = self.tabla.obtener_datos_envio()
        self.assertEqual(datos, [])

    def test_modificar_dato_nombre(self):
        dato = FakeDatoEnvio(nombre="Pedro")
        self.tabla.agregar_dato_envio(dato)

        self.tabla.modificar_dato("nombre", "Carlos", 0)
        self.assertEqual(self.tabla.tabla_datos_envio[1][0].nombre, "Carlos")

    def test_eliminar_dato_valido(self):
        dato = FakeDatoEnvio(nombre="Eliminarme")
        self.tabla.agregar_dato_envio(dato)

        resultado = self.tabla.eliminar_dato(0)
        self.assertTrue(resultado)
        self.assertEqual(len(self.tabla.tabla_datos_envio[1]), 0)

    def test_eliminar_dato_fuera_de_rango(self):
        resultado = self.tabla.eliminar_dato(5)
        self.assertFalse(resultado)

    def test_tiene_datos_envio_true(self):
        dato = FakeDatoEnvio()
        self.tabla.agregar_dato_envio(dato)
        self.assertTrue(self.tabla.tiene_datos_envio())

    def test_tiene_datos_envio_false(self):
        self.assertFalse(self.tabla.tiene_datos_envio())

    def test_modificar_dato_direccion(self):
        dato = FakeDatoEnvio(direccion="Av. Siempre Viva")
        self.tabla.agregar_dato_envio(dato)

        self.tabla.modificar_dato("direccion", "Av. Nueva", 0)
        self.assertEqual(self.tabla.tabla_datos_envio[1][0].direccion, "Av. Nueva")

    def test_modificar_dato_ciudad(self):
        dato = FakeDatoEnvio(ciudad="La Paz")
        self.tabla.agregar_dato_envio(dato)

        self.tabla.modificar_dato("ciudad", "Cochabamba", 0)
        self.assertEqual(self.tabla.tabla_datos_envio[1][0].ciudad, "Cochabamba")

    def test_modificar_dato_codigo_postal(self):
        dato = FakeDatoEnvio(codigo_postal="1234")
        self.tabla.agregar_dato_envio(dato)

        self.tabla.modificar_dato("cp", "5678", 0)
        self.assertEqual(self.tabla.tabla_datos_envio[1][0].codigo_postal, "5678")

    def test_modificar_dato_pais(self):
        dato = FakeDatoEnvio(pais="Bolivia")
        self.tabla.agregar_dato_envio(dato)

        self.tabla.modificar_dato("pais", "Argentina", 0)
        self.assertEqual(self.tabla.tabla_datos_envio[1][0].pais, "Argentina")


if __name__ == '__main__':
    unittest.main()
