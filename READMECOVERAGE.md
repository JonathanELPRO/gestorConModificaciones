
# 🧪 Guía para Medir Cobertura de Código con `coverage`

## ✅ Pasos para utilizar `coverage` en el proyecto

### 1. Instalar Coverage

```bash
pip install coverage
```

---

### 2. Ejecutar Tests con PyUnit (`unittest`) y Coverage

```bash
python -m coverage run --rcfile=.coveragerc -m unittest discover -s tests
```

📌 Esto ejecutará todos los tests en la carpeta `tests` y empezará a medir cobertura según las reglas definidas en `.coveragerc`.

---

### 3. Generar Reporte en Consola

```bash
python -m coverage report --rcfile=.coveragerc -m
```

---

### 4. Generar Reporte HTML Detallado

```bash
python -m coverage html --rcfile=.coveragerc
```

---

### 5. Visualizar el Reporte HTML

```bash
start htmlcov/index.html
```

> 🔍 Esto abrirá una vista detallada y navegable en tu navegador, resaltando líneas cubiertas y no cubiertas.

---

## 🎯 Apuntando a Carpetas Específicas

Estamos testeando solo la carpeta `Modelo`.

### 🎯 Ejemplo: Solo testear `G_pago`

#### `.coveragerc` ANTES

```ini
[run]
source = Modelo
omit =
```

🔍 Esto incluye toda la carpeta `Modelo`.

---

#### `.coveragerc` DESPUÉS

```ini
[run]
source = Modelo\G_pago
omit =
```

🔎 Ahora solo se medirá la cobertura de los archivos dentro de `Modelo/G_pago`.

---

## 🚫 Omitiendo Archivos Específicos

### Ejemplo: Omitir todos los `__init__.py`

#### `.coveragerc` ANTES

```ini
[run]
source = Modelo
omit =
```

---

#### `.coveragerc` DESPUÉS

```ini
[run]
source = Modelo
omit =
    __init__.py
```

📛 Esto omitirá todos los archivos `__init__.py` del análisis.

---

### 🧰 También puedes omitir rutas específicas:

```ini
omit =
    __init__.py
    Modelo\G_pago\archivo_que_quieres_omitir.py
```

---

## 📌 Notas Finales

- Puedes modificar `.coveragerc` libremente para adaptar el análisis a tus necesidades.
- Asegúrate de mantener una buena cobertura en las funciones críticas del sistema.
- Usa los reportes HTML para identificar qué líneas no están siendo testeadas.

---

💡 ¡Usa esta guía como plantilla para trabajar con coverage en otros módulos del proyecto también!
