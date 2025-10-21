#!/usr/bin/env python3
"""
Task 3 — TypeError al comparar str con int en el juego 'Adivina el número'.
Cómo ejecutar: python3 ed_task3_typeerror_str_int.py
"""

def demo_error():
    print("== Demo error Task 3: TypeError por str vs int ==")
    secret = 57
    s = "42"  # simulamos entrada de usuario sin convertir
    print(f"Secreto: {secret} | Entrada (str): {s!r}")
    try:
        if s < secret:  # comparación inválida en Python 3
            print("Muy bajo")
    except TypeError as e:
        print(">> Caught:", e)

def demo_fix():
    print("\n== Corrección Task 3: convertir entrada a int y validar ==")
    secret = 57
    s = "42"  # simulamos entrada textual
    try:
        guess = int(s)
    except ValueError:
        print("Introduce un entero entre 1 y 100.")
        return
    if guess < secret:
        print("Demasiado bajo...")
    elif guess > secret:
        print("Demasiado alto...")
    else:
        print("¡Correcto!")

if __name__ == "__main__":
    demo_error()
    demo_fix()
