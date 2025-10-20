# Section 2 – Error Detection (Tasks 5–8)

Below are four different errors (raised intentionally or commonly encountered),
each with a short code snippet to reproduce, the actual Python exception message,
an explanation of **why** it happens, and a corrected version.

> **Tip:** In `errors_task_5_to_8.py` these are demonstrated with `try/except`
> so you can see each error and its fix in a single run.

---

## Task 5 — `SyntaxError` (missing colon after `if`)

**Bad code:**
```python
if True
    print("Hello")
```

**What happens & why:**  
`SyntaxError: expected ':'` — In Python, `if`, `for`, `while`, `def`, `class`, etc.
require a colon (`:`) to start the indented block.

**Fix:**
```python
if True:
    print("Hello")
```

---

## Task 6 — `TypeError` (adding `int` and `str`)

**Bad code:**
```python
3 + "3"
```

**What happens & why:**  
`TypeError: unsupported operand type(s) for +: 'int' and 'str'` — You cannot add
numbers and strings directly.

**Fix:**
```python
3 + int("3")     # => 6
# or
str(3) + "3"     # => "33"
```

---

## Task 7 — `IndexError` (list index out of range)

**Bad code:**
```python
nums = [10, 20, 30]
nums[3]  # valid indices are 0,1,2
```

**What happens & why:**  
`IndexError: list index out of range` — Index 3 does not exist in a 3‑element list.

**Fix:**
```python
nums[2]  # last valid index
# or check length before indexing
if len(nums) > 3:
    print(nums[3])
```

---

## Task 8 — `ValueError` (invalid literal for `int()`)

**Bad code:**
```python
int("abc")
```

**What happens & why:**  
`ValueError: invalid literal for int() with base 10: 'abc'` — The string does not
represent a valid base‑10 integer.

**Fix:**
```python
s = "123"
n = int(s)  # OK
# or validate before converting
s = "abc"
if s.isdigit():
    n = int(s)
else:
    print("Not a number")
```
