import unittest
from Modelo.G_datos_envio.DatoEnvio import DatoEnvio

class TestDatoEnvio(unittest.TestCase):

    def setUp(self):
        """Método para inicializar los objetos antes de cada test."""
        self.dato_envio = DatoEnvio(
            nombre="Juan Pérez",
            direccion="Calle Falsa 123",
            ciudad="La Paz",
            codigo_postal="12345",
            pais="Bolivia"
        )

    def test_get_nombre(self):
        """Prueba que el método get_nombre retorna el valor correcto."""
        self.assertEqual(self.dato_envio.get_nombre(), "Juan Pérez")

    def test_get_direccion(self):
        """Prueba que el método get_direccion retorna el valor correcto."""
        self.assertEqual(self.dato_envio.get_direccion(), "Calle Falsa 123")

    def test_get_ciudad(self):
        """Prueba que el método get_ciudad retorna el valor correcto."""
        self.assertEqual(self.dato_envio.get_ciudad(), "La Paz")

    def test_get_codigo_postal(self):
        """Prueba que el método get_codigo_postal retorna el valor correcto."""
        self.assertEqual(self.dato_envio.get_codigo_postal(), "12345")

    def test_get_pais(self):
        """Prueba que el método get_pais retorna el valor correcto."""
        self.assertEqual(self.dato_envio.get_pais(), "Bolivia")

    def test_set_nombre_valido(self):
        """Prueba que el set_nombre cambia el valor correctamente."""
        self.dato_envio.set_nombre("Carlos Gómez")
        self.assertEqual(self.dato_envio.get_nombre(), "Carlos Gómez")

    def test_set_nombre_vacio(self):
        """Prueba que el set_nombre lanza una excepción si el nombre está vacío."""
        with self.assertRaises(ValueError):
            self.dato_envio.set_nombre("")

    def test_set_direccion_valida(self):
        """Prueba que el set_direccion cambia el valor correctamente."""
        self.dato_envio.set_direccion("Avenida Siempre Viva 742")
        self.assertEqual(self.dato_envio.get_direccion(), "Avenida Siempre Viva 742")

    def test_set_direccion_vacia(self):
        """Prueba que el set_direccion lanza una excepción si la dirección está vacía."""
        with self.assertRaises(ValueError):
            self.dato_envio.set_direccion("")

    def test_set_ciudad_valida(self):
        """Prueba que el set_ciudad cambia el valor correctamente."""
        self.dato_envio.set_ciudad("Cochabamba")
        self.assertEqual(self.dato_envio.get_ciudad(), "Cochabamba")

    def test_set_ciudad_vacia(self):
        """Prueba que el set_ciudad lanza una excepción si la ciudad está vacía."""
        with self.assertRaises(ValueError):
            self.dato_envio.set_ciudad("")

    def test_set_codigo_postal_valido(self):
        """Prueba que el set_codigo_postal cambia el valor correctamente."""
        self.dato_envio.set_codigo_postal("54321")
        self.assertEqual(self.dato_envio.get_codigo_postal(), "54321")

    def test_set_codigo_postal_vacio(self):
        """Prueba que el set_codigo_postal lanza una excepción si el código postal está vacío."""
        with self.assertRaises(ValueError):
            self.dato_envio.set_codigo_postal("")

    def test_set_pais_valido(self):
        """Prueba que el set_pais cambia el valor correctamente."""
        self.dato_envio.set_pais("Perú")
        self.assertEqual(self.dato_envio.get_pais(), "Perú")

    def test_set_pais_vacio(self):
        """Prueba que el set_pais lanza una excepción si el país está vacío."""
        with self.assertRaises(ValueError):
            self.dato_envio.set_pais("")

    def test_str(self):
        """Prueba que el método __str__ devuelve la representación correcta."""
        expected_str = (
            "Nombre: Juan Pérez\n Direccion:Calle Falsa 123\n Ciudad:La Paz\n "
            "Codigo Postal:12345\n Pais:Bolivia"
        )
        self.assertEqual(str(self.dato_envio), expected_str)

if __name__ == '__main__':
    unittest.main()
