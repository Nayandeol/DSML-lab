import numpy as np
def read_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    print(f"Enter the elements row by row (total {n * n} values):")
    elements = list(map(float, input().split()))
    if len(elements) != n * n:
        print("Error: Number of elements does not match matrix size!")
        return None
    return np.array(elements).reshape(n, n)
def compute_inverse(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        print("Matrix is not invertible.")
        return None
print("Matrix 1:")
matrix1 = read_matrix()
print("\nMatrix 2:")
matrix2 = read_matrix()
if matrix1 is not None:
    print("\nMatrix 1:")
    print(matrix1)
    inv1 = compute_inverse(matrix1)
    if inv1 is not None:
        print("\nInverse of Matrix 1:")
        print(inv1)
if matrix2 is not None:
    print("\nMatrix 2:")
    print(matrix2)
    inv2 = compute_inverse(matrix2)
    if inv2 is not None:
        print("\nInverse of Matrix 2:")
        print(inv2)
