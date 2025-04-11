import unittest
from Modelo.G_usuario.Session import Session
from Modelo.G_usuario.Administrador import Administrador
from Modelo.G_usuario.Miembro import Miembro


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        self.administrador = Administrador(
            nombre="Ana Gómez",
            correo="ana.gomez@example.com",
            contrasena="admin123",
            id_usuario=1
        )
        self.miembro = Miembro(
            nombre="Luis Martínez",
            correo="luis.martinez@example.com",
            contrasena="miembro123",
            id_usuario=2
        )

    def tearDown(self):
        self.session.cerrar_sesion()  # Asegúrate de cerrar la sesión después de cada prueba

    def test_iniciar_sesion(self):
        self.session.iniciar_sesion(self.administrador)
        self.assertEqual(self.session.obtener_usuario_autenticado(), self.administrador)

    def test_cerrar_sesion(self):
        self.session.iniciar_sesion(self.administrador)
        self.session.cerrar_sesion()
        self.assertIsNone(self.session.obtener_usuario_autenticado())

    def test_esta_autenticado(self):
        self.assertFalse(self.session.esta_autenticado())
        self.session.iniciar_sesion(self.administrador)
        self.assertTrue(self.session.esta_autenticado())

    def test_obtener_id_usuario(self):
        self.session.iniciar_sesion(self.administrador)
        self.assertEqual(self.session.obtener_id_usuario(), 1)

    def test_es_administrador(self):
        self.session.iniciar_sesion(self.administrador)
        self.assertTrue(self.session.es_administrador())

        self.session.cerrar_sesion()
        self.session.iniciar_sesion(self.miembro)
        self.assertFalse(self.session.es_administrador())

    def test_singleton(self):
        session1 = Session()
        session2 = Session()
        self.assertIs(session1, session2)  # Ambas instancias deben ser la misma
