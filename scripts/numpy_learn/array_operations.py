import numpy as np

# ====== Data Initialization ======
array1 = np.array([1, 2, 7])
array2 = np.array([2, 6, 2])
array3 = np.array([4, 2])
ages = np.array([12, 19, 17, 66, 25, 16, 20])
matrix1 = np.array([
    [3, 1],
    [1, 2]
])
matrix2 = np.array([
    [6, -4],
    [1, 2]
])

# ====== Utility Function ======
def print_array(name: str, array: np.ndarray):
    """Utility function to print arrays with structure."""
    print(f"{name} =\n{array}\n")

# ====== Printing Arrays ======
print_array("array1", array1)
print_array("array2", array2)
print_array("array3", array3)
print_array("matrix1", matrix1)
print_array("matrix2", matrix2)

# ====== Element-wise Operations ======
print(f"Addition (array1 + array2): {array1 + array2}\n")
print(f"Multiplication (array1 * array2): {array1 * array2}\n")
print(f"Subtraction (array1 - array2): {array1 - array2}\n")

# ====== Matrix Multiplication ======
print(f"Matrix Multiplication (matrix1 @ matrix2):\n{np.matmul(matrix1, matrix2)}\n")  # Equivalent to `matrix1 @ matrix2` or `matrix1.dot(matrix2)`
print(f"Matrix Multiplication (matrix2 @ array3):\n{np.matmul(matrix2, array3)}\n")    # Equivalent to `matrix2 @ array3` or `matrix2.dot(array3)`

# ====== Scalar Operations ======
print(f"Scalar Multiplication (array2 * 3): {array2 * 3}\n")

# ====== Broadcasting ======
print(f"Broadcasting Addition (array1 + 7): {array1 + 7}\n")
