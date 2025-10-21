# Sección 2 — Detección de Errores (Casos por tarea)

Este documento describe **cuatro errores enconrados/cometidos** en la resolución de las tareas de la Sección 1, así como **la forma en que se resolvieron**. 

---

## Task 1 — Multiplicación 4×4: `IndexError` por índice fuera de rango

**Escenario:** En una versión preliminar de la multiplicación 4×4 se configuraron incorrectamente los límites de los bucles o se omitió validar que **todas** las filas de `A` y `B` tuvieran exactamente 4 elementos. Ello provocó accesos fuera de rango a las listas internas durante el cómputo de `C = A × B`.

**Síntoma típico:**
```
IndexError: list index out of range
```

### Cómo se reproduce (dos variantes habituales)
1) **Límite de bucle erróneo (columna fuera de rango):**
```python
for i in range(4):
    for j in range(5):   # <-- ERROR: debería ser range(4)
        s = 0.0
        for k in range(4):
            s += A[i][k] * B[k][j]  # truena cuando j == 4
        C[i][j] = s                 # también fallaría aquí por índice inexistente
```

2) **Filas desalineadas (falta de validación de longitud):**
```python
A = [[1,2,3,4], [5,6,7,8], [9,10,11], [13,14,15,16]]  # fila 3 incompleta
# Sin validación previa, el triple bucle puede provocar IndexError.
```

### Causa raíz (análisis)
- **Límites de iteración inconsistentes** con la estructura 4×4 (p. ej., `range(5)`).
- **Confusión de índices** en el triple bucle (`i`, `j`, `k`) o intercambio accidental de posiciones.
- **Ausencia de validaciones** de forma (filas con menos/más de 4 elementos).

### Resolución
1) **Acotar correctamente los bucles** a 4 en cada dimensión y mantener la convención `i`=fila de `A`, `j`=columna de `B`, `k`=índice interno:
```python
for i in range(4):
    for j in range(4):
        s = 0.0
        for k in range(4):
            s += A[i][k] * B[k][j]
        C[i][j] = s
```

2) **Validar forma 4×4 antes del cómputo** (previene índices fuera de rango por filas incompletas):
```python
if len(A) != 4 or any(len(row) != 4 for row in A):
    raise ValueError("Matriz A debe ser de 4x4")
if len(B) != 4 or any(len(row) != 4 for row in B):
    raise ValueError("Matriz B debe ser de 4x4")
```

> *Nota:* En la versión final estas validaciones ya están presentes. Para efectos del informe, se documenta que el `IndexError` se presentó en una **iteración preliminar** y quedó **resuelto** al acotar rangos y validar la forma.


---

## Task 2 — Diccionario y filtros: **Error de lógica** al crear el diccionario (clave sin valor)

**Escenario:** En desarrollo preliminar, al construir el diccionario de animales se **insertaba la clave pero se omitía (por error) el valor asociado**. Se usó inicialmente  `setdefault(key)` **sin** especificar el valor, o asignar desde `get(key)` vacío, provocando que las entradas quedaran con **`None`** y se perdiera la información real del animal proveniente de la cadena inicial.

**Síntomas (no siempre hay excepción):**
- Valores **`None`** en el diccionario: `{'bear': None, 'polar bear': None, ...}`.
- Filtros que devuelven claves correctas pero **valores vacíos** o conteos inconsistentes.

### Versión defectuosa
```python
animals = ["bear", "polar bear", "bee"]
d = {}
for animal in animals:
    key = animal.lower().strip()
    d.setdefault(key)         # ❌ crea la clave con valor None (default por omisión)
    # o bien:
    # d[key] = d.get(key)     # ❌ asigna None si no existía previamente
```

### Causa raíz (análisis)
- **Uso incompleto de la API** (`setdefault`) o **asignación desde un get vacío**, lo que genera entradas sin el valor que se quería preservar.
- Como no hay `KeyError`, el bug **pasa desapercibido** hasta que se inspeccionan las salidas.

### Resolución (versión correcta)
- Asignar explícitamente el **valor deseado** (p. ej., conservar el nombre original):
```python
for animal in animals:
    key = animal.lower().strip()
    d[key] = animal           # ✅ el valor asociado es el nombre original
    # alternativamente, si se quisiera crear solo si no existe:
    # d.setdefault(key, animal)
```

### Detección temprana
- Verificar que **no existan valores None** después de construir el diccionario:
```python
if any(v is None for v in d.values()):
    raise AssertionError("Se detectaron claves sin valor asociado (None).")
```
- Comparar tamaños si se agregan condiciones adicionales:
```python
assert len(d) == len(animals), "El tamaño del diccionario no coincide con la lista base."
```

---

## Task 3 — Adivina el número: `TypeError` por comparar `str` con `int`

**Escenario**: La entrada de `input()` se compara directamente contra un entero sin conversión.  
**Síntoma**: `TypeError: '<' not supported between instances of 'str' and 'int'`

### Datos del error
```python
secret = 57
s = "42"           # viene de input()
if s < secret:     # comparación inválida (str vs int)
    ...
```

### Causa raíz
- `input()` devuelve **cadenas**; se requiere conversión a `int` (y validar rango).

### Resolución
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

**Escenario**: En la verificación de confirmación de contraseña se utilizó por error `if confirm = pw:`.  
**Síntoma**: `SyntaxError: invalid syntax`

### Causa raíz
- En una expresión booleana se requiere **comparación** (`==`), no **asignación** (`=`).

### Resolución
1. Detectar el error de forma controlada con `compile()` para no detener el script.  
2. Mostrar la versión **corregida** con `==` y su ejecución.

**Fragmento clave**:
```python
good = "pw = 'seguro'\nconfirm = 'seguro'\nif confirm == pw:\n    print('Password creado.')"
exec(good, {})
```

### Buenas prácticas
- Usar un linter/formatter que ayude a detectar este tipo de equivocaciones.
- Revisar con calma signos y paréntesis cuando se reciba un `SyntaxError`.

---
