# Lab 3 — Control Structures

**Curso:** Talento Altamente Especializado – Inteligencia Artificial 2025  
**Módulo:** Introduction to Python II  
**Instructor:** Cristian Torres González
**Equipo 7:** Carlos Alberto Vidrios Serrano - Jorge Saúl Montes Cáceres


This lab practices *loops* and *control structures* with four programming tasks, plus
a section on identifying and explaining typical Python errors.

## Estructura de carpetas

```
Lab3_Control_Structures/
├─ Section_1/
│  ├─ task_1_matrix_4x4.py
│  ├─ task_2_dict_filters.py
│  ├─ task_3_guess_number.py
│  └─ task_4_password_validator.py
└─ Section_2/
   ├─ ERRORS.md
   └─ errors_task_5_to_8.py
```

## Ejecucion vía consola en Linux

```bash
cd Lab3_Control_Structures/Section_1
python3 task_1_matrix_4x4.py
python3 task_2_dict_filters.py
python3 task_3_guess_number.py
python3 task_4_password_validator.py

cd ../Section_2
python3 errors_task_5_to_8.py
```

> Make the scripts executable (optional):
> ```bash
> chmod +x Section_1/*.py Section_2/*.py
> ```

---

## Task 1 — 4×4 Matrix Multiplication (NO libraries)

- Enter two 4×4 matrices **row by row**.  
- The result `C = A × B` is printed with 4 decimals.  
- Implementation uses nested loops only (no `numpy`).

**Run:**
```bash
python3 Section_1/task_1_matrix_4x4.py
```

---

## Task 2 — Dictionary and Filters

- Builds a dictionary from the given animal names (case-insensitive keys).  
- Creates three dictionaries with words containing **'a'**, **'b'**, and **'y'**.  
- Prints counts and the sorted lists of matched animals.

**Run:**
```bash
python3 Section_1/task_2_dict_filters.py
```

---

## Task 3 — Guess the Number

- Secret number in **[1, 100]**.  
- Get hints: *Too low / Too high*.  
- Shows number of attempts when you guess correctly.  
- Type **`q`** to quit.

**Run:**
```bash
python3 Section_1/task_3_guess_number.py
```

---

## Task 4 — Password Validator

Rules enforced:
- At least **8** characters
- **No spaces**
- Must **not** contain any of: `&`, `#`, `%`, `@`

Prompts until a valid password is entered and confirmed.

**Run:**
```bash
python3 Section_1/task_4_password_validator.py
```

---

## Section 2 — Error Detection (Tasks 5–8)

- `ERRORS.md`: explanations and corrected code for 4 different errors:
  - `SyntaxError`, `TypeError`, `IndexError`, `ValueError`  
- `errors_task_5_to_8.py`: runnable demo that shows each error via `try/except`
  and prints the fixed approach.

**Run:**
```bash
python3 Section_2/errors_task_5_to_8.py
```

---

## Notes
- Scripts are self-contained and rely only on the Python standard library.
- Tested with Python 3.10+.
