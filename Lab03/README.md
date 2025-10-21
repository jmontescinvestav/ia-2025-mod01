# Laboratorio 3 — Estructuras de Control

**Curso:** Talento Altamente Especializado – Inteligencia Artificial 2025  
**Módulo:** Introducción a Python  
**Docente:** Cristian Torres González  
**Equipo 7:** Carlos Alberto Vidrios Serrano — Jorge Saúl Montes Cáceres

Este laboratorio fortalece el dominio de los *bucles* y las *estructuras de control* mediante cuatro tareas de programación, además de una sección orientada a identificar y explicar errores frecuentes en Python, con enfoque formativo.

## Estructura de carpetas

```
Lab3/
├─ Section_1/
│  ├─ task_1_matrix_4x4.py
│  ├─ task_2_dict_filters.py
│  ├─ task_3_guess_number.py
│  └─ task_4_password_validator.py
└─ Section_2/
   ├─ ERRORS.md
   └─ errors_task_5_to_8.py
```

## Tarea 1 — Multiplicación de matrices 4×4 (sin librerías externas)

- Captura de dos matrices **4×4** fila por fila.  
- Cálculo del producto `C = A × B` y presentación del resultado con cuatro decimales.  
- Implementación con bucles anidados (sin uso de bibliotecas de terceros).

## Tarea 2 — Diccionario y filtros

- Construcción de un diccionario a partir de la lista de animales (claves insensibles a mayúsculas).  
- Generación de tres diccionarios con términos que contengan **‘a’**, **‘b’** y **‘y’**.  
- Presentación de conteos y listados ordenados de coincidencias.

## Tarea 3 — Adivina el número

- Selección de un número secreto dentro del intervalo **[1, 100]**.  
- Retroalimentación progresiva: *Muy bajo / Muy alto*.  
- Reporte del número de intentos al acertar; opción de salida anticipada con **`q`**.

## Tarea 4 — Validador de contraseña

Criterios de validación:
- Longitud mínima de **8** caracteres.  
- **Sin espacios**.  
- Exclusión de los caracteres: `&`, `#`, `%`, `@`.  

Se solicita confirmación y se repite hasta cumplir los criterios establecidos.

## Sección 2 — Detección de errores (Tasks 5–8)

- `ERRORS.md`: explicación y corrección de cuatro errores representativos  
  (`SyntaxError`, `TypeError`, `IndexError`, `ValueError`), con énfasis en la causa raíz y la prevención.  
- `errors_task_5_to_8.py`: demostración controlada con manejo de excepciones para ilustrar los fallos y su resolución.

## Notas

- Los scripts son autocontenidos y emplean únicamente la biblioteca estándar de Python.  
- Probado con Python **3.10** o superior.  
