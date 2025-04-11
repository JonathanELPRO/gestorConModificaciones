import unittest
from Modelo.G_usuario.TablaUsuarios import TablaUsuarios
from Modelo.G_usuario.Miembro import Miembro
from Modelo.G_usuario.Administrador import Administrador

class TestTablaUsuarios(unittest.TestCase):
    def setUp(self):
        self.tabla_usuarios = TablaUsuarios()
        self.miembro = Miembro(
            nombre="Luis Martínez",
            correo="luis.martinez@example.com",
            contrasena="miembro123",
            id_usuario=1
        )
        self.administrador = Administrador(
            nombre="Ana Gómez",
            correo="ana.gomez@example.com",
            contrasena="admin123",
            id_usuario=2
        )

    def tearDown(self):
        self.miembro = None
        self.administrador = None

    def test_registrar_usuario(self):
        resultado = self.tabla_usuarios.registrar_usuario(self.miembro)
        self.assertTrue(resultado)
        #self.assertIn(self.miembro, self.tabla_usuarios.validar_credenciales(self.miembro.correo,self.miembro.contrasena))

    def test_validar_credenciales_exitosas(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        resultado = self.tabla_usuarios.validar_credenciales("luis.martinez@example.com", "miembro123")
        self.assertEqual(resultado, self.miembro)

    def test_validar_credenciales_fallidas(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        resultado = self.tabla_usuarios.validar_credenciales("incorrecto@example.com", "wrongpassword")
        self.assertIsNone(resultado)

    def test_obtener_usuario_por_id(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        usuario = self.tabla_usuarios.obtener_usuario_por_id(1)
        self.assertEqual(usuario, self.miembro)

    def test_modificar_dato_usuario_nombre(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        # Iniciar sesión con el miembro registrado
        self.tabla_usuarios.session.iniciar_sesion(self.miembro)
        self.tabla_usuarios.modificar_dato_usuario(1, "Carlos López")
        self.assertEqual(self.miembro.get_nombre(), "Carlos López")

    def test_modificar_dato_usuario_correo(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        # Iniciar sesión con el miembro registrado
        self.tabla_usuarios.session.iniciar_sesion(self.miembro)
        self.tabla_usuarios.modificar_dato_usuario(2, "carlos.lopez@example.com")
        self.assertEqual(self.miembro.get_correo(), "carlos.lopez@example.com")

    def test_eliminar_cuenta(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        # Iniciar sesión con el miembro registrado
        self.tabla_usuarios.session.iniciar_sesion(self.miembro)
        resultado = self.tabla_usuarios.eliminar_cuenta()
        self.assertTrue(resultado)  # Verifica que la eliminación fue exitosa
        self.assertNotIn(self.miembro, self.tabla_usuarios.usuarios)  # Verifica que el usuario ya no está en la lista

    def test_obtener_miembros(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        self.tabla_usuarios.registrar_usuario(self.administrador)
        miembros = self.tabla_usuarios.obtener_miembros()
        self.assertIn(self.miembro, miembros)
        self.assertNotIn(self.administrador, miembros)

    def test_eliminar_cuenta_miembro(self):
        self.tabla_usuarios.registrar_usuario(self.miembro)
        resultado = self.tabla_usuarios.eliminar_cuenta_miembro(self.miembro)
        self.assertTrue(resultado)
        self.assertNotIn(self.miembro, self.tabla_usuarios.usuarios)
