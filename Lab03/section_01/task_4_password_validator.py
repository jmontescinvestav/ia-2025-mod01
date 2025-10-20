#!/usr/bin/env python3
"""
Lab 3 - Task 4: Password creation validator
Rules:
- At least 8 characters
- No spaces
- Must NOT include any of these characters: &, #, %, @
Prompts the user until a valid password is entered and confirmed.
How to run:
  python3 task_4_password_validator.py
"""

FORBIDDEN = set("&#%@")

def validate_password(pw: str):
    reasons = []
    if len(pw) < 8:
        reasons.append("Password must be at least 8 characters long.")
    if any(ch.isspace() for ch in pw):
        reasons.append("Password must not contain spaces.")
    bad = FORBIDDEN.intersection(pw)
    if bad:
        reasons.append("Password must not contain any of these characters: " + ", ".join(sorted(FORBIDDEN)))
    return reasons  # empty list means valid

def main():
    print("=== Create a New Password ===")
    while True:
        pw = input("Enter new password: ")
        reasons = validate_password(pw)
        if reasons:
            print("Invalid password:")
            for r in reasons:
                print("  -", r)
            continue
        confirm = input("Confirm password: ")
        if confirm != pw:
            print("Confirmation does not match. Try again.")
            continue
        print("Password accepted.")
        break

if __name__ == "__main__":
    main()
