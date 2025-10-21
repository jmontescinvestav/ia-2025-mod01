#!/usr/bin/env python3
"""
Lab 3 - Task 4: Creadod de password con validacion
Autores: Carlos Alberto Vidrios Serrano
         Jorge Saúl Montes Cáceres
"""

FORBIDDEN = set("&#%@")

def validate_password(pw: str):
    reasons = []
    if len(pw) < 8:
        reasons.append("El Password debe tener al menos 8 caracteres.")
    if any(ch.isspace() for ch in pw):
        reasons.append("El Password no debe contener espacios.")
    bad = FORBIDDEN.intersection(pw)
    if bad:
        reasons.append("El Password no debe contener ninguno de estos caracteres: " + ", ".join(sorted(FORBIDDEN)))
    return reasons  # empty list means valid

def main():
    print("=== Crear un Nuevo Password ===")
    while True:
        pw = input("Introduce el nuevo password: ")
        reasons = validate_password(pw)
        if reasons:
            print("Password inválido:")
            for r in reasons:
                print("  -", r)
            continue
        confirm = input("Confirm password: ")
        if confirm != pw:
            print("La confirmación no coincide. Intentar de nuevo.")
            continue
        print("Password creado.")
        break

if __name__ == "__main__":
    main()
