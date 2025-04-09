import unittest
from Modelo.G_usuario.Usuario import Usuario


class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario(
            nombre="Juan Pérez",
            correo="juan.perez@example.com",
            contrasena="contrasena123",
            id_usuario=1
        )





    def test_get_nombre(self):
        self.assertEqual(self.usuario.get_nombre(), "Juan Pérez")

    def test_set_nombre(self):
        self.usuario.set_nombre("Carlos López")
        self.assertEqual(self.usuario.get_nombre(), "Carlos López")

    def test_get_correo(self):
        self.assertEqual(self.usuario.get_correo(), "juan.perez@example.com")

    def test_set_correo(self):
        self.usuario.set_correo("carlos.lopez@example.com")
        self.assertEqual(self.usuario.get_correo(), "carlos.lopez@example.com")


    def test_get_contrasena(self):
        self.assertEqual(self.usuario.get_contrasena(), "contrasena123")

    def test_set_contrasena(self):
        self.usuario.set_contrasena("nueva_contrasena")
        self.assertEqual(self.usuario.get_contrasena(), "nueva_contrasena")

    def tearDown(self):
        self.usuario = None

    def test_get_id(self):
        self.assertEqual(self.usuario.get_id(), 1)




