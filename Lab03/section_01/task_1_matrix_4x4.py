"""
Lab 3 - Task 1: 4x4 Multiplicación de matrices sin usar librerias externas
Autores: Carlos Alberto Vidrios Serrano
         Jorge Saúl Montes Cáceres
"""

def read_matrix_4x4(name: str):
    print(f"Introduce los 16 numeros para la matriz {name}, renglon por renglon (4 numeros por renglon).")
    M = []
    for r in range(4):
        while True:
            line = input(f"Renglon {r+1} (4 numeros separados por espacios): ").strip()
            parts = line.split()
            if len(parts) != 4:
                print("  -> Introduce exactamente 4 numeros.")
                continue
            try:
                row = [float(x) for x in parts]
                M.append(row)
                break
            except ValueError:
                print("  -> Numero invalido. Intenta de nuevo.")
    return M

def multiply_4x4(A, B):
    # Validate shapes
    if len(A) != 4 or any(len(row) != 4 for row in A):
        raise ValueError("Matriz A debe ser de 4x4")
    if len(B) != 4 or any(len(row) != 4 for row in B):
        raise ValueError("Matriz B debe ser de 4x4")
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
    print("=== 4x4 Multiplicacion de matrices ===")
    A = read_matrix_4x4("A")
    B = read_matrix_4x4("B")
    C = multiply_4x4(A, B)
    print_matrix(A, title="Matriz A:")
    print_matrix(B, title="Matriz B:")
    print_matrix(C, title="A x B = C:")

if __name__ == "__main__":
    main()
