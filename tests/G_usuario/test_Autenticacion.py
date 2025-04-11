import unittest
from unittest.mock import MagicMock
from Modelo.G_usuario.Autenticacion import Autenticacion
from Modelo.G_usuario.Administrador import Administrador

class TestAutenticacion(unittest.TestCase):
    def setUp(self):
        # Crear un mock para la tabla de usuarios
        self.tabla_usuarios_mock = MagicMock()
        self.autenticacion = Autenticacion(self.tabla_usuarios_mock)

        # Crear un usuario administrador para las pruebas
        self.administrador = Administrador(
            nombre="Ana Gómez",
            correo="ana.gomez@example.com",
            contrasena="admin123",
            id_usuario=1
        )

    def test_validacion_credenciales_exitosas(self):
        # Configurar el mock para que devuelva el usuario cuando las credenciales son correctas
        self.tabla_usuarios_mock.validar_credenciales.return_value = self.administrador

        resultado = self.autenticacion.validacion_credenciales("ana.gomez@example.com", "admin123")
        self.assertTrue(resultado)
        self.assertEqual(self.autenticacion.session.obtener_usuario_autenticado(), self.administrador)

    def test_validacion_credenciales_fallidas(self):
        # Configurar el mock para que devuelva None cuando las credenciales son incorrectas
        self.tabla_usuarios_mock.validar_credenciales.return_value = None

        resultado = self.autenticacion.validacion_credenciales("incorrecto@example.com", "wrongpassword")
        self.assertFalse(resultado)
        self.assertIsNone(self.autenticacion.session.obtener_usuario_autenticado())
