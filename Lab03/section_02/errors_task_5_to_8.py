#!/usr/bin/env python3
"""
Section 2 – Tasks 5–8: Demonstrate four different errors and their fixes.
This script *shows* each error via try/except so that the file can run to completion.

To run:
  python3 errors_task_5_to_8.py
"""

def show(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title))

# Task 5: SyntaxError — demonstrate via compile() so we can catch it at runtime.
show("Task 5 — SyntaxError (missing colon)")
bad_code = "if True\n    print('Hello')"  # missing colon
try:
    compile(bad_code, "<string>", "exec")
    print("No error (unexpected)")
except SyntaxError as e:
    print("Caught:", e)
# Fixed version:
exec("if True:\n    print('Fixed: Hello')")

# Task 6: TypeError — int + str
show("Task 6 — TypeError (int + str)")
try:
    _ = 3 + "3"
except TypeError as e:
    print("Caught:", e)
print("Fixed (3 + int('3')):", 3 + int("3"))

# Task 7: IndexError — out of range
show("Task 7 — IndexError (out of range)")
nums = [10, 20, 30]
try:
    _ = nums[3]
except IndexError as e:
    print("Caught:", e)
print("Fixed (last element):", nums[-1])

# Task 8: ValueError — invalid literal for int()
show("Task 8 — ValueError (invalid literal for int())")
try:
    _ = int("abc")
except ValueError as e:
    print("Caught:", e)
print("Fixed (int('42')):", int("42"))
