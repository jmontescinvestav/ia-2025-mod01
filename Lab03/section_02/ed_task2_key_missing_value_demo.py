#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task 2 — Error de lógica y uso de diccionario: clave sin valor en la construcción del diccionario
Reproduce el fallo (uso de setdefault sin valor / get vacío) y muestra la forma 
en que se resolvió.

"""

def demo_error():
    print("== Demo error Task 2: clave insertada sin valor (None) ==")
    animals = ["bear", "polar bear", "bee"]
    d = {}
    for animal in animals:
        key = animal.lower().strip()
        # Uso inicial defectuoso:
        d.setdefault(key)
    print("Diccionario defectuoso sin value validos:", d)
    none_count = sum(1 for v in d.values() if v is None)
    print(f"Valores None detectados: {none_count}")

def build_dict_fixed(animals):
    d = {}
    for animal in animals:
        key = animal.lower().strip()
        d[key] = animal           # asignación del valor asociado
        # tambien se usó: d.setdefault(key, animal)
    # Control temprano
    if any(v is None for v in d.values()):
        raise AssertionError("Se detectaron claves sin valor asociado (None).")
    return d

def demo_fix():
    print("\n== Corrección Task 2: asignar el valor explícito y validar ==")
    animals = ["bear", "polar bear", "bee"]
    d = build_dict_fixed(animals)
    print("Diccionario corregido:", d)

if __name__ == "__main__":
    demo_error()
    demo_fix()
