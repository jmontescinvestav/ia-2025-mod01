#!/usr/bin/env python3
"""
Task 2 — AttributeError: 'list' object has no attribute 'items'
Causa: intentar usar .items() sobre una lista en lugar de un diccionario.
Cómo ejecutar: python3 ed_task2_attributeerror_items.py
"""

def demo_error():
    print("== Demo error Task 2: AttributeError por .items() en lista ==")
    animals = ["cat", "dog", "bee"]
    print("Estructura actual:", type(animals).__name__, animals)
    try:
        for k, v in animals.items():   # <-- AttributeError
            pass
    except AttributeError as e:
        print(">> Caught:", e)

def demo_fix():
    print("\n== Corrección Task 2: construir dict y filtrar sobre dict ==")
    animals = ["cat", "dog", "bee"]
    d = {name.lower(): name for name in animals}
    letter = "b"
    filtered = {k: v for k, v in d.items() if letter in k}
    print("Diccionario base:", d)
    print(f"Filtrado por letra '{letter}':", filtered)

if __name__ == "__main__":
    demo_error()
    demo_fix()
