import unittest
from Modelo.G_usuario.Administrador import Administrador

class TestAdministrador(unittest.TestCase):
    def setUp(self):
        self.administrador = Administrador(
            nombre="Ana Gómez",
            correo="ana.gomez@example.com",
            contrasena="admin123",
            id_usuario=1
        )

    def tearDown(self):
        self.administrador = None

    def test_get_nombre(self):
        self.assertEqual(self.administrador.get_nombre(), "Ana Gómez")

    def test_get_correo(self):
        self.assertEqual(self.administrador.get_correo(), "ana.gomez@example.com")

    def test_get_contrasena(self):
        self.assertEqual(self.administrador.get_contrasena(), "admin123")

    def test_get_id(self):
        self.assertEqual(self.administrador.get_id(), 1)

    def test_get_puesto(self):
        self.assertEqual(self.administrador.get_puesto(), "CEO")

    def test_set_puesto(self):
        self.administrador.set_puesto("CTO")
        self.assertEqual(self.administrador.get_puesto(), "CTO")
