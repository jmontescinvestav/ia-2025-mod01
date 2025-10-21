#!/usr/bin/env python3
"""
Task 1 — ValueError al convertir cadenas a float (matriz 4x4)
Ocurre el error típico (coma decimal o token no numérico) y muestra la corrección.
Cómo ejecutar: python3 ed_task1_valueerror_matrix.py
"""

def demo_error():
    print("== Demo error Task 1: ValueError por coma decimal ==")
    line = "1 2 3,5 4"   # la coma decimal provoca ValueError al convertir a float
    print("Entrada problemática:", repr(line))
    tokens = line.split()
    try:
        row = [float(t) for t in tokens]   # aquí saltará el ValueError en '3,5'
        print("Fila convertida:", row)
    except ValueError as e:
        print(">> Caught:", e)

def demo_fix():
    print("\n== Corrección Task 1: normalizar separador / validar ==")
    def parse_row_4floats(line: str):
        tokens = [t.replace(',', '.') for t in line.split()]  # permitir coma decimal
        if len(tokens) != 4:
            raise ValueError("Se requieren exactamente 4 números por renglón.")
        try:
            return [float(t) for t in tokens]
        except ValueError:
            raise ValueError("Cada token debe ser numérico (usa punto decimal).")

    good = "1 2 3,5 4"
    print("Entrada corregida:", repr(good))
    row = parse_row_4floats(good)
    print("Fila convertida:", row)

if __name__ == "__main__":
    demo_error()
    demo_fix()
