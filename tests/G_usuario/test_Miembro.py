import unittest
from Modelo.G_usuario.Miembro import Miembro

class TestMiembro(unittest.TestCase):
    def setUp(self):
        self.miembro = Miembro(
            nombre="Luis Martínez",
            correo="luis.martinez@example.com",
            contrasena="miembro123",
            id_usuario=1
        )

    def tearDown(self):
        self.miembro = None

    def test_get_nombre(self):
        self.assertEqual(self.miembro.get_nombre(), "Luis Martínez")

    def test_get_correo(self):
        self.assertEqual(self.miembro.get_correo(), "luis.martinez@example.com")

    def test_get_contrasena(self):
        self.assertEqual(self.miembro.get_contrasena(), "miembro123")

    def test_get_id(self):
        self.assertEqual(self.miembro.get_id(), 1)

    def test_get_fecha_nacimiento(self):
        self.assertEqual(self.miembro.get_fecha_nacimiento(), "Aun no se ha ingresado una fecha de nacimiento")

    def test_set_fecha_nacimiento(self):
        self.miembro.set_fecha_nacimiento("1990-01-01")
        self.assertEqual(self.miembro.get_fecha_nacimiento(), "1990-01-01")

    def test_get_genero(self):
        self.assertEqual(self.miembro.get_genero(), "Aun no se ha ingresado un genero")

    def test_set_genero(self):
        self.miembro.set_genero("Masculino")
        self.assertEqual(self.miembro.get_genero(), "Masculino")

    def test_get_pais(self):
        self.assertEqual(self.miembro.get_pais(), "Aun no se ha ingresado un pais")

    def test_set_pais(self):
        self.miembro.set_pais("México")
        self.assertEqual(self.miembro.get_pais(), "México")
