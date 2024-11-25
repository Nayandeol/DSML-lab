import numpy as np
def read_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    print(f"Enter the elements row by row (total {n * n} values):")
    elements = list(map(float, input().split()))
    if len(elements) != n * n:
        print("Error: Number of elements does not match matrix size!")
        return None
    return np.array(elements).reshape(n, n)
def compute_determinant(matrix):
    return np.linalg.det(matrix)
print("Matrix 1:")
matrix1 = read_matrix()
print("\nMatrix 2:")
matrix2 = read_matrix()
if matrix1 is not None:
    print("\nMatrix 1:")
    print(matrix1)
    det1 = compute_determinant(matrix1)
    print(f"Determinant of Matrix 1: {det1:.2f}")
if matrix2 is not None:
    print("\nMatrix 2:")
    print(matrix2)
    det2 = compute_determinant(matrix2)
    print(f"Determinant of Matrix 2: {det2:.2f}")
