import pytest
from Modelo.G_pago.GestorPago import GestorPago

@pytest.fixture
def gestor_pago():
    gestor = GestorPago()

    yield gestor

    print("Limpiando después de la prueba...")
    del gestor

def test_validar_datos_correctos(gestor_pago):
    assert gestor_pago.validar_datos('1234567812345678', '12/25', '123') == True

def test_validar_datos_numero_incorrecto(gestor_pago):
    assert gestor_pago.validar_datos('123456781234567', '12/25', '123') == False

def test_validar_datos_fecha_incorrecta(gestor_pago):
    assert gestor_pago.validar_datos('1234567812345678', '1225', '123') == False

def test_validar_datos_cvv_incorrecto(gestor_pago):
    assert gestor_pago.validar_datos('1234567812345678', '12/25', '12') == False
