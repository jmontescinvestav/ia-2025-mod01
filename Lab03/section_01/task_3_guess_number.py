#!/usr/bin/env python3
"""
Lab 3 - Task 3: Adivinar numero con pistas
Autores: Carlos Alberto Vidrios Serrano
         Jorge Saúl Montes Cáceres
"""

import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("=== Adivina el número (1..100) ===")
    while True:
        s = input("Tu suposición (o 'q' para salir): ").strip().lower()
        if s == 'q':
            print(f"Quit. El numero secreto era: {secret}.")
            break
        try:
            guess = int(s)
        except ValueError:
            print("  -> Introduce un número entero entre 1 y 100.")
            continue
        if not (1 <= guess <= 100):
            print("  -> Fuera de rango. Introduce un número entre 1 y 100.")
            continue
        attempts += 1
        if guess == secret:
            print(f"¡Correcto! Necesitaste {attempts} intento(s).")
            break
        elif guess < secret:
            print("Demasiado bajo. Intenta un número más alto.")
        else:
            print("Demasiado alto. Intenta un número más bajo.")

if __name__ == "__main__":
    main()
