#!/usr/bin/env python3
"""
Lab 3 - Task 1: 4x4 matrix multiplication (NO libraries)
Author: You
How to run:
  python3 task_1_matrix_4x4.py
Then follow the prompts to enter the matrices row by row.

Rules checked:
- Uses only pure Python lists and loops (no numpy, no external libs).
"""

def read_matrix_4x4(name: str):
    print(f"Enter the 16 numbers for matrix {name}, row by row (4 numbers per row).")
    M = []
    for r in range(4):
        while True:
            line = input(f"Row {r+1} (4 numbers separated by spaces): ").strip()
            parts = line.split()
            if len(parts) != 4:
                print("  -> Please enter exactly 4 numbers.")
                continue
            try:
                row = [float(x) for x in parts]
                M.append(row)
                break
            except ValueError:
                print("  -> Invalid number. Try again.")
    return M

def multiply_4x4(A, B):
    # Validate shapes
    if len(A) != 4 or any(len(row) != 4 for row in A):
        raise ValueError("Matrix A must be 4x4")
    if len(B) != 4 or any(len(row) != 4 for row in B):
        raise ValueError("Matrix B must be 4x4")
    # Initialize C with zeros
    C = [[0.0 for _ in range(4)] for _ in range(4)]
    # Triple loop
    for i in range(4):
        for j in range(4):
            s = 0.0
            for k in range(4):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

def print_matrix(M, title=None):
    if title:
        print(title)
    for row in M:
        print("  " + "  ".join(f"{val:10.4f}" for val in row))

def main():
    print("=== 4x4 Matrix Multiplication ===")
    A = read_matrix_4x4("A")
    B = read_matrix_4x4("B")
    C = multiply_4x4(A, B)
    print_matrix(A, title="Matrix A:")
    print_matrix(B, title="Matrix B:")
    print_matrix(C, title="A x B = C:")

if __name__ == "__main__":
    main()
