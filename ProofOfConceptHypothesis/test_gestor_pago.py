from hypothesis import given
import hypothesis.strategies as st
from Modelo.G_pago.GestorPago import GestorPago  # Asegúrate de importar correctamente tu clase

# Crea una estrategia para generar un número de tarjeta válido (16 dígitos)
@st.composite
def tarjeta_valida(draw):
    numero = draw(st.just("1234567812345678"))
    fecha_vencimiento = draw(st.just("12/25"))
    cvv = draw(st.just("123"))
    return numero, fecha_vencimiento, cvv

# Crea una estrategia para generar un número de tarjeta inválido (menos de 16 dígitos)
@st.composite
def tarjeta_invalida(draw):
    numero = draw(st.just("123456781234567"))
    fecha_vencimiento = draw(st.just("12/25"))
    cvv = draw(st.just("123"))
    return numero, fecha_vencimiento, cvv

# Crea la estrategia para fechas de vencimiento inválidas
@st.composite
def fecha_invalida(draw):
    numero = draw(st.just("1234567812345678"))
    fecha_vencimiento = draw(st.just("1225"))
    cvv = draw(st.just("123"))
    return numero, fecha_vencimiento, cvv

# Crea la estrategia para cvv inválido
@st.composite
def cvv_invalido(draw):
    numero = draw(st.just("1234567812345678"))
    fecha_vencimiento = draw(st.just("12/25"))
    cvv = draw(st.just("12"))
    return numero, fecha_vencimiento, cvv

# Creamos un test que debe ejecutar la función de prueba con
# given provee diferentes combinaciones de datos generados por la estrategia tarjeta_valida()
@given(tarjeta_valida())
def test_validar_datos_correctos(datos):
    gestor_pago = GestorPago()
    numero, fecha_vencimiento, cvv = datos
    assert gestor_pago.validar_datos(numero, fecha_vencimiento, cvv) is True

@given(tarjeta_invalida())
def test_validar_datos_incorrectos_numero(datos):
    gestor_pago = GestorPago()
    numero, fecha_vencimiento, cvv = datos
    assert gestor_pago.validar_datos(numero, fecha_vencimiento, cvv) is False

@given(fecha_invalida())
def test_validar_datos_incorrectos_fecha(datos):
    gestor_pago = GestorPago()
    numero, fecha_vencimiento, cvv = datos
    assert gestor_pago.validar_datos(numero, fecha_vencimiento, cvv) is False

@given(cvv_invalido())
def test_validar_datos_incorrectos_cvv(datos):
    gestor_pago = GestorPago()
    numero, fecha_vencimiento, cvv = datos
    assert gestor_pago.validar_datos(numero, fecha_vencimiento, cvv) is False
