#!/usr/bin/env python3
"""
Task 4 — SyntaxError por usar asignación ('=') dentro de una condición ('if').
Mostramos el error vía compile() (para que el script corra) y después la corrección.
Cómo ejecutar: python3 ed_task4_syntaxerror_assignment.py
"""

def demo_error():
    print("== Demo error Task 4: SyntaxError por '=' en condición ==")
    bad = "pw = 'seguro123'\nconfirm = 'seguro123'\nif confirm = pw:\n    print('Coincide')"
    try:
        compile(bad, "<string>", "exec")  # aquí se detecta el SyntaxError
    except SyntaxError as e:
        print(">> Caught:", e)

def demo_fix():
    print("\n== Corrección Task 4: usar '==' para comparar ==")
    good = "pw = 'seguro123'\nconfirm = 'seguro123'\nif confirm == pw:\n    print('Password creado.')\nelse:\n    print('La confirmación no coincide.')"
    print("Ejecutando versión corregida:")
    exec(good, {})

if __name__ == "__main__":
    demo_error()
    demo_fix()
