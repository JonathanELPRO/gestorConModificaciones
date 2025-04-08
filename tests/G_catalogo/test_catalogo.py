import unittest
from unittest.mock import patch

from Modelo.G_catalogo.Catalogo import Catalogo
from Modelo.G_inventario.Producto import *


class TestCatalogo(unittest.TestCase):
    def setUp(self):
        self.catalogo = Catalogo()

    def tearDown(self):
        self.catalogo = None


    def test_agregar_productos_con_elementos(self):
        productoParaAgregar = Aretes("Aretes de plata", "123ABC", "MarcaX", 10, "Plata", "Plateado", "Zirconia", 20)
        productosParaAgregar = [productoParaAgregar]
        self.catalogo.agregar_productos(productosParaAgregar)
        self.assertEqual(len(self.catalogo.productos), 1)

    def test_agregar_productos_lista_vacia(self):
        productos=[]
        self.catalogo.agregar_productos(productos)
        self.assertEqual(len(self.catalogo.productos), 0)

    def test_obtener_productos(self):
        productosEsperados = self.catalogo.productos
        productosObtenidos = self.catalogo.obtener_productos()
        self.assertEqual(productosObtenidos, productosEsperados)

    def test___str___con_producto_disponible(self):
        producto1 = Anillos("Anillo de plata", "789GHI", "MarcaZ", 15, "Plata", "Plateado", "Zirconia", 30)
        self.catalogo.productos = [producto1]
        self.assertEqual(self.catalogo.__str__(),"Nombre: Anillo de plata\nModelo: 789GHI\nPrecio: 30\nEstado: Disponible\n\n")

    def test___str___con_producto_no_disponible(self):
        producto1 = Anillos("Anillo de plata", "789GHI", "MarcaZ", 0, "Plata", "Plateado", "Zirconia", 30)
        self.catalogo.productos = [producto1]
        self.assertEqual(self.catalogo.__str__(),"Nombre: Anillo de plata\nModelo: 789GHI\nPrecio: 30\nEstado: Agotado\n\n")

    def test___str___con_lista_productos_vacia(self):
        self.assertEqual(self.catalogo.__str__(),"")








