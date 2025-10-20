#!/usr/bin/env python3
"""
Lab 3 - Task 3: Guess the number
- Program chooses a number in [1, 100].
- User guesses until correct.
- After each wrong guess, print whether the secret number is higher or lower.
- At the end, show the number of attempts.
How to run:
  python3 task_3_guess_number.py
Tip: Type 'q' to quit early.
"""

import random

def main():
    secret = random.randint(1, 100)
    attempts = 0
    print("=== Guess the Number (1..100) ===")
    while True:
        s = input("Your guess (or 'q' to quit): ").strip().lower()
        if s == 'q':
            print(f"Quit. The secret number was {secret}.")
            break
        try:
            guess = int(s)
        except ValueError:
            print("  -> Please enter an integer between 1 and 100.")
            continue
        if not (1 <= guess <= 100):
            print("  -> Out of range. Enter 1..100.")
            continue
        attempts += 1
        if guess == secret:
            print(f"Correct! You needed {attempts} attempt(s).")
            break
        elif guess < secret:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

if __name__ == "__main__":
    main()
