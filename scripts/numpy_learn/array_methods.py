import numpy as np

# ====== Data Initialization ======
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[1, 2], [3, 4]])
matrix3 = np.array([[3, 2, 6], [7, 4, 9]])
vector1 = np.array([3.0, 7.0, 5.2, 2.1, 3.5, 2.6, 1.4, 0.2])
numbers1 = np.array([1, 2, 3])
numbers2 = np.array([4, 5, 6])
expenses = np.array([np.nan, np.nan, 200.0, 650.0, 1525.0, np.nan])

# ====== Utility Functions ======
def print_array(name: str, array: np.ndarray) -> None:
    """Utility to print arrays in a structured format."""
    print(f"{name} =\n{array}\n")

def handle_missing_data(array: np.ndarray) -> np.ndarray:
    """Replaces NaN values in the array with 0.0."""
    return np.nan_to_num(array, nan=0.0)

# ====== Printing Arrays ======
print_array("matrix1", matrix1)
print_array("matrix2", matrix2)
print_array("matrix3", matrix3)
print_array("vector1", vector1)
print_array("numbers1", numbers1)
print_array("numbers2", numbers2)
print_array("expenses", expenses)

# ====== Basic Array Operations ======
print(f"Transpose of matrix1:\n{matrix1.T}\n")
print(f"Transpose of matrix2:\n{matrix2.T}\n")

# Aggregation Operations
print(f"Sum of matrix1: {matrix1.sum()}")
print(f"Sum of matrix2: {matrix2.sum()}")
print(f"Sum of vector1: {vector1.sum()}\n")

print(f"Mean of matrix1: {matrix1.mean()}")
print(f"Mean of matrix2: {matrix2.mean()}")
print(f"Mean of vector1: {vector1.mean()}\n")

print(f"Max of matrix1: {matrix1.max()}")
print(f"Max of matrix2: {matrix2.max()}")
print(f"Max of vector1: {vector1.max()}\n")

print(f"Min of matrix1: {matrix1.min()}")
print(f"Min of matrix2: {matrix2.min()}")
print(f"Min of vector1: {vector1.min()}\n")

print(f"Standard Deviation of matrix1: {matrix1.std()}")
print(f"Standard Deviation of matrix2: {matrix2.std()}")
print(f"Standard Deviation of vector1: {vector1.std()}\n")

# Index Operations
print(f"Argmax of matrix1: {matrix1.argmax()}")
print(f"Argmin of matrix1: {matrix1.argmin()}\n")

# ====== Advanced Operations ======
# Concatenating Arrays
combined_numbers = np.concatenate((numbers1, numbers2))
print_array("Combined Numbers", combined_numbers)

combined_matrix = np.concatenate((matrix2, matrix2))
print_array("Combined Matrix", combined_matrix)

# Splitting Arrays
print(f"Split combined_numbers into 2 batches: {np.split(combined_numbers, 2)}")
print(f"Split combined_numbers into 3 batches: {np.split(combined_numbers, 3)}\n")

# Sorting Arrays
print(f"Sorted vector1: {np.sort(vector1)}")
print(f"Sorted matrix3 (row-wise):\n{np.sort(matrix3, axis=1)}\n")

# ====== Missing Data Handling ======
cleaned_expenses = handle_missing_data(expenses)
print_array("Cleaned Expenses", cleaned_expenses)
