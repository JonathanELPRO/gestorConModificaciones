import unittest
from Modelo.G_usuario.GestorUsuario import GestorUsuario
from Modelo.G_usuario.Miembro import Miembro
from Modelo.G_usuario.Administrador import Administrador

class TestGestorUsuario(unittest.TestCase):
    def setUp(self):
        self.gestor_usuario = GestorUsuario()
        self.miembro = Miembro("Luis Martínez", "luis.martinez@example.com", "miembro123", 1)
        self.administrador = Administrador("Ana Gómez", "ana.gomez@example.com", "admin123", 2)

    def test_recibir_datos_inicio_sesion_exitosos(self):
        self.gestor_usuario.tabla_usuarios.registrar_usuario(self.miembro)
        resultado = self.gestor_usuario.recibir_datos_inicio_sesion("luis.martinez@example.com", "miembro123")
        self.assertTrue(resultado)

    def test_recibir_datos_inicio_sesion_fallidos(self):
        resultado = self.gestor_usuario.recibir_datos_inicio_sesion("incorrecto@example.com", "wrongpassword")
        self.assertFalse(resultado)

    def test_recibir_datos_registro_usuario(self):
        resultado = self.gestor_usuario.recibir_datos_registro_usuario("Carlos López", "carlos.lopez@example.com", "1234")
        self.assertTrue(resultado)
        usuario_registrado = self.gestor_usuario.tabla_usuarios.validar_credenciales("carlos.lopez@example.com", "1234")
        self.assertIsNotNone(usuario_registrado)

    def test_recibir_datos_modificacion_usuario(self):#no terminado
        self.gestor_usuario.tabla_usuarios.registrar_usuario(self.miembro)
        # Iniciar sesión con el miembro registrado
        self.gestor_usuario.recibir_datos_inicio_sesion("luis.martinez@example.com", "miembro123")
        self.gestor_usuario.recibir_datos_modificacion_usuario(1, "Carlos López")
        self.assertEqual(self.miembro.get_nombre(), "Carlos López")

    def test_solicitud_datos_usuario(self):
        self.gestor_usuario.tabla_usuarios.registrar_usuario(self.miembro)
        self.gestor_usuario.recibir_datos_inicio_sesion("luis.martinez@example.com", "miembro123")
        datos_usuario = self.gestor_usuario.solicitud_datos_usuario()
        self.assertEqual(datos_usuario["Nombre"], "Luis Martínez")

    def test_solicitud_eliminar_cuenta(self):
        self.gestor_usuario.tabla_usuarios.registrar_usuario(self.miembro)
        self.gestor_usuario.recibir_datos_inicio_sesion("luis.martinez@example.com", "miembro123")
        resultado = self.gestor_usuario.solicitud_eliminar_cuenta()
        self.assertTrue(resultado)
        self.assertIsNone(self.gestor_usuario.tabla_usuarios.validar_credenciales("luis.martinez@example.com", "miembro123"))

    def test_solicitud_eliminar_cuenta_miembro(self):#no terminado
        self.gestor_usuario.tabla_usuarios.registrar_usuario(self.miembro)
        self.gestor_usuario.tabla_usuarios.registrar_usuario(self.administrador)
        self.gestor_usuario.recibir_datos_inicio_sesion("ana.gomez@example.com", "admin123")
        resultado = self.gestor_usuario.solicitud_eliminar_cuenta_miembro()
        self.assertTrue(resultado)
        self.assertNotIn(self.miembro, self.gestor_usuario.tabla_usuarios.usuarios)
