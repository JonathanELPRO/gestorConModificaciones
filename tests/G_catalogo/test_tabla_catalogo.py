import unittest
from unittest.mock import patch, MagicMock

from Modelo.G_catalogo.TablaCatalogo import TablaCatalogo
from Modelo.G_inventario.Inventario import Inventario
from Modelo.G_inventario.Producto import *

class TestTablaCatalogo(unittest.TestCase):
    def setUp(self):
        with patch.object(TablaCatalogo, 'obtener_productos_inventario', lambda x: None):
            self.tablaCatalogo = TablaCatalogo()

        self.tablaCatalogo.productos_inventario=[]

    def tearDown(self):
        self.tablaCatalogo.productos_inventario= None
        self.tablaCatalogo = None

    def test_obtener_productos_inventario(self):
            producto1 = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)
            producto2 = Collares("Collar de oro", "456DEF", "MarcaY", 5, "Oro", "Dorado", "Diamante", 100)
            producto3 = Anillos("Anillo de plata", "789GHI", "MarcaZ", 15, "Plata", "Plateado", "Zirconia", 30)
            producto4 = Piercings("Piercing de oro", "321JKL", "MarcaW", 3, "Oro", "Dorado", "Diamante", 50)
            producto5 = Pulseras("Pulsera de plata", "654MNO", "MarcaV", 7, "Plata", "Plateado", "Zirconia", 40)
            producto6 = Dijes("Dije de oro", "987PQR", "MarcaU", 2, "Oro", "Dorado", "Diamante", 60)
            producto7 = Aretes("Aretes de oro", "123STU", "MarcaT", 8, "Oro", "Dorado", "Diamante", 80)
            producto8 = Collares("Collar de plata", "456VWX", "MarcaS", 4, "Plata", "Plateado", "Zirconia", 25)
            producto9 = Anillos("Anillo de oro", "789YZA", "MarcaR", 12, "Oro", "Dorado", "Diamante", 70)
            producto10 = Piercings("Piercing de plata", "321BCD", "MarcaQ", 1, "Plata", "Plateado", "Zirconia", 35)
            inventario = [producto1,producto2,producto3,producto4,producto5,producto6,producto7,producto8,producto9,producto10]

            with patch.object(Inventario, 'obtener_lista_productos', return_value=inventario):
                self.tablaCatalogo.obtener_productos_inventario()
                self.assertEqual(len(self.tablaCatalogo.productos_inventario), 10)

    def test_obtener_catalogo_dije_correcto(self):
        self.tablaCatalogo.productos_inventario = [
            Dijes("Dije Y", "112AAB", "MarcaD", 1, "Plata", "Plateado", "Zafiro", 77)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Dijes")
        self.assertEqual(len(resultado), 1)



    def test_obtener_catalogo_producto_otro_tipo(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Reloj", "999XYZ", "MarcaO", 2, "Acero", "Negro", "Cristal", 120)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Dijes")
        self.assertEqual(len(resultado), 0)


    def test_obtener_catalogo_dije_pero_tipo_manilla(self):
        self.tablaCatalogo.productos_inventario = [
            Dijes("Dije X", "111AAA", "MarcaD", 1, "Oro", "Dorado", "Rubí", 99)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Manilla")
        self.assertEqual(len(resultado), 0)


    def test_obtener_catalogo_pulseras_correcto(self):
        self.tablaCatalogo.productos_inventario = [
            Pulseras("Pulsera Y", "112AABC", "MarcaDD", 1, "Plata", "Plateado", "Zafiro", 77)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Pulseras")
        self.assertEqual(len(resultado), 1)



    def test_obtener_catalogo_producto_otro_tipo2(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Reloj", "999XYZ", "MarcaO", 2, "Acero", "Negro", "Cristal", 120)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Pulseras")
        self.assertEqual(len(resultado), 0)


    def test_obtener_catalogo_piercings_correcto(self):
        self.tablaCatalogo.productos_inventario = [
            Piercings("Piercing Z", "113BBC", "MarcaEE", 2, "Oro", "Dorado", "Rubí", 88)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Piercings")
        self.assertEqual(len(resultado), 1)

    def test_obtener_catalogo_producto_otro_tipo3(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Cadena", "998WXY", "MarcaP", 3, "Cuero", "Marrón", "Cristal", 55)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Piercings")
        self.assertEqual(len(resultado), 0)

    def test_obtener_catalogo_anillos_correcto(self):
        self.tablaCatalogo.productos_inventario = [
            Anillos("Anillo X", "114CCC", "MarcaFF", 5, "Plata", "Plateado", "Topacio", 99)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Anillos")
        self.assertEqual(len(resultado), 1)

    def test_obtener_catalogo_producto_otro_tipo4(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Broche", "997VWX", "MarcaQ", 2, "Plástico", "Rosa", "Cristal", 25)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Anillos")
        self.assertEqual(len(resultado), 0)

    def test_obtener_catalogo_collares_correcto(self):
        self.tablaCatalogo.productos_inventario = [
            Collares("Collar A", "115DDD", "MarcaGG", 4, "Oro", "Dorado", "Perla", 110)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Collares")
        self.assertEqual(len(resultado), 1)

    def test_obtener_catalogo_producto_otro_tipo5(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Cintillo", "996UVW", "MarcaR", 1, "Tela", "Rojo", "Cristal", 15)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Collares")
        self.assertEqual(len(resultado), 0)

    def test_obtener_catalogo_aretes_correcto(self):
        self.tablaCatalogo.productos_inventario = [
            Aretes("Aretes B", "116EEE", "MarcaHH", 6, "Plata", "Plateado", "Esmeralda", 105)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Aretes")
        self.assertEqual(len(resultado), 1)

    def test_obtener_catalogo_producto_otro_tipo6(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.obtener_catalogo("Aretes")
        self.assertEqual(len(resultado), 0)

    def test_obtener_catalogo_inventario_vacio(self):
        resultado = self.tablaCatalogo.obtener_catalogo("Aretes")
        self.assertEqual(len(resultado), 0)

    def test_buscar_producto_con_dato_piedra(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.buscar_producto("Cristal")
        self.assertEqual(len(resultado), 1)

    def test_buscar_producto_con_dato_incoherente(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.buscar_producto("Largo")
        self.assertEqual(len(resultado), 0)

    def test_buscar_producto_con_dato_color(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.buscar_producto("Azul")
        self.assertEqual(len(resultado), 1)

    def test_buscar_producto_con_dato_material(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.buscar_producto("Metal")
        self.assertEqual(len(resultado), 1)

    def test_buscar_producto_con_dato_marca(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.buscar_producto("MarcaS")
        self.assertEqual(len(resultado), 1)

    def test_buscar_producto_con_dato_nombre(self):
        self.tablaCatalogo.productos_inventario = [
            Producto("Diadema", "995TUV", "MarcaS", 2, "Metal", "Azul", "Cristal", 35)
        ]
        resultado = self.tablaCatalogo.buscar_producto("Diadema")
        self.assertEqual(len(resultado), 1)

    def test_buscar_producto_con_inventario_vacio(self):
        resultado = self.tablaCatalogo.buscar_producto("Diadema")
        self.assertEqual(len(resultado), 0)

















