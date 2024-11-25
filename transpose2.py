import numpy as np
def read_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print(f"Enter the elements row by row (total {rows * cols} values):")
    elements = list(map(float, input().split()))
    if len(elements) != rows * cols:
        print("Error: Number of elements does not match matrix size!")
        return None
    return np.array(elements).reshape(rows, cols)
print("Matrix 1:")
matrix1 = read_matrix()
if matrix1 is not None:
    print("\nMatrix 2:")
    matrix2 = read_matrix()
    if matrix2 is not None:
        transpose1 = np.transpose(matrix1)
        transpose2 = np.transpose(matrix2)
        print("\nMatrix 1:")
        print(matrix1)
        print("\nTranspose of Matrix 1:")
        print(transpose1)
        print("\nMatrix 2:")
        print(matrix2)
        print("\nTranspose of Matrix 2:")
        print(transpose2)
    else:
        print("Matrix 2 input is invalid!")
else:
    print("Matrix 1 input is invalid!")
