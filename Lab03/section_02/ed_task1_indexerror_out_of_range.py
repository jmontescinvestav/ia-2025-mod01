"""
Task 1 — IndexError por índice fuera de rango (multiplicación 4×4).
En un punto del dearrollo se comete un error de indice fuera de rango
El código demuestra dos variantes del fallo y luego la versión corregida.
"""

def demo_error_range_bounds():
    print("== Demo error Task 1 (Variante A): límite de columna fuera de rango ==")
    # Matrices 4x4 válidas
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10,11,12],
         [13,14,15,16]]
    B = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    C = [[0]*4 for _ in range(4)]

    try:
        # ERROR: j debería recorrer range(4); aquí se usa range(5)
        for i in range(4):
            for j in range(5):  # <-- fuera de rango (columna 4 no existe)
                s = 0.0
                for k in range(4):
                    s += A[i][k] * B[k][j]  # IndexError cuando j == 4
                C[i][j] = s                 
    except IndexError as e:
        print(">> Caught:", e)


def demo_error_misaligned_rows():
    print("\n== Demo error Task 1 (Variante B): filas desalineadas ==")
    # A tiene una fila de solo 3 elementos (fila 3)
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11],         # <-- fil incompleta
         [13, 14, 15, 16]]
    B = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    C = [[0]*4 for _ in range(4)]

    try:
        for i in range(4):
            for j in range(4):
                s = 0.0
                for k in range(4):
                    s += A[i][k] * B[k][j]  # IndexError cuando i==2, k==3
                C[i][j] = s
    except IndexError as e:
        print(">> Caught:", e)


def multiply_4x4_safe(A, B):
    """Multiplica A×B para matrices 4×4 con validación de forma."""
    if len(A) != 4 or any(len(row) != 4 for row in A):
        raise ValueError("Matriz A debe ser de 4x4")
    if len(B) != 4 or any(len(row) != 4 for row in B):
        raise ValueError("Matriz B debe ser de 4x4")

    C = [[0.0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):   # límites correctos
            s = 0.0
            for k in range(4):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def demo_fix():
    print("\n== Corrección Task 1: validacion de forma y límites correctos ==")
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10,11,12],
         [13,14,15,16]]
    B = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    C = multiply_4x4_safe(A, B)
    print("Producto A×B (4×4) calculado correctamente:")
    for fila in C:
        print("  ", "  ".join(f"{x:8.2f}" for x in fila))


if __name__ == "__main__":
    demo_error_range_bounds()
    demo_error_misaligned_rows()
    demo_fix()
