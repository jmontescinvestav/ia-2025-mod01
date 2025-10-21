# Sección 2 — Detección de Errores (Casos por tarea)

Este documento describe **cuatro errores frecuentes** que suelen cometer las y los estudiantes al resolver las tareas de la Sección 1, así como **la forma en que se corrigen**. La intención pedagógica es fomentar un proceso disciplinado de *reproducir → diagnosticar → corregir → prevenir*.

---

## Task 1 — Multiplicación 4×4: `ValueError` al convertir a `float`

**Escenario**: Al capturar una fila de 4 números para una matriz, se ingresa una **coma decimal** (`3,5`) o un **token no numérico**.  
**Síntoma**: `ValueError: could not convert string to float: '3,5'`

### Cómo se reproduce
- Entrada: `"1 2 3,5 4"`  
- Conversión directa: `[float(t) for t in line.split()]` provoca `ValueError` en `3,5`.

### Causa raíz
- Python espera **punto** decimal (`3.5`) para `float()`. La coma no es válida por omisión.
- También ocurre si se cuelan letras o símbolos extraños.

### Resolución (en el script `ed_task1_valueerror_matrix.py`)
1. **Normalizar** separadores: `t.replace(',', '.')` para tolerar comas si se desea.  
2. **Validar longitud**: asegurar exactamente 4 tokens por renglón.  
3. **Manejar excepciones**: dar mensajes claros y orientados a la acción.

**Fragmento clave**:
```python
tokens = [t.replace(',', '.') for t in line.split()]
if len(tokens) != 4:
    raise ValueError("Se requieren exactamente 4 números por renglón.")
row = [float(t) for t in tokens]
```

### Buenas prácticas
- Especificar en el enunciado que se use **punto decimal**.
- Validar el número exacto de elementos por fila antes de convertir.
- Emitir mensajes precisos (qué se espera y cómo corregir).

---

## Task 2 — Diccionario y filtros: `AttributeError` al usar `.items()` en una **lista**

**Escenario**: Se construye una lista de animales y, por confusión, se intenta iterar con `.items()` como si fuera diccionario.  
**Síntoma**: `AttributeError: 'list' object has no attribute 'items'`

### Cómo se reproduce
```python
animals = ["cat", "dog", "bee"]
for k, v in animals.items():  # <-- .items() solo existe en dict
    ...
```

### Causa raíz
- `.items()` es exclusivo de **diccionarios**. Una lista no tiene ese método.

### Resolución (en el script `ed_task2_attributeerror_items.py`)
1. **Construir el diccionario** explícitamente (clave en minúsculas, valor original).  
2. **Aplicar filtros** siempre sobre el **diccionario** con `.items()`.

**Fragmento clave**:
```python
d = {name.lower(): name for name in animals}
filtered = {k: v for k, v in d.items() if 'b' in k}
```

### Buenas prácticas
- Nombrado claro: `animals` (lista) vs. `d` (diccionario).  
- En desarrollo, confirmar tipos con `type()` si hay dudas.

---

## Task 3 — Adivina el número: `TypeError` por comparar `str` con `int`

**Escenario**: La entrada de `input()` se compara directamente contra un entero sin conversión.  
**Síntoma**: `TypeError: '<' not supported between instances of 'str' and 'int'`

### Cómo se reproduce
```python
secret = 57
s = "42"           # viene de input()
if s < secret:     # comparación inválida (str vs int)
    ...
```

### Causa raíz
- `input()` devuelve **cadenas**; se requiere conversión a `int` (y validar rango).

### Resolución (en el script `ed_task3_typeerror_str_int.py`)
1. **Convertir** con `int()`, capturando `ValueError` si la entrada no es numérica.  
2. **Validar rango** si aplica (p. ej., 1 a 100).  
3. Comparar ya con tipos homogéneos (`int` vs `int`).

**Fragmento clave**:
```python
try:
    guess = int(s)
except ValueError:
    print("Introduce un entero entre 1 y 100.")
    continue
```

### Buenas prácticas
- Convertir lo antes posible y mantener consistencia de tipos.
- Mensajes de error breves y accionables.

---

## Task 4 — Validador de contraseña: `SyntaxError` por usar `=` en vez de `==`

**Escenario**: En la verificación de confirmación de contraseña se escribe `if confirm = pw:`.  
**Síntoma**: `SyntaxError: invalid syntax`

### Cómo se reproduce
- El intérprete marca error de sintaxis al **compilar** el bloque con `=` en una condición.

### Causa raíz
- En una expresión booleana se requiere **comparación** (`==`), no **asignación** (`=`).

### Resolución (en el script `ed_task4_syntaxerror_assignment.py`)
1. Detectamos el error de forma controlada con `compile()` para no detener el script.  
2. Mostramos la versión **corregida** con `==` y su ejecución.

**Fragmento clave**:
```python
good = "pw = 'seguro'\nconfirm = 'seguro'\nif confirm == pw:\n    print('Password creado.')"
exec(good, {})
```

### Buenas prácticas
- Usar un linter/formatter que ayude a detectar este tipo de equivocaciones.
- Revisar con calma signos y paréntesis cuando se reciba un `SyntaxError`.

---

