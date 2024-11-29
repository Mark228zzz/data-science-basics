import numpy as np

# ====== Creating Arrays ======
scalar = np.array(3)
array = np.array([1, 2, 3, 4, 5, 6])
ages = np.array([15, 18, 20, 66, 52, 10, 25])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# ====== Reshaping Arrays ======
reshaped_array1 = array.reshape(2, 3)  # Shape (2, 3)
reshaped_array2 = array.reshape(3, 2)  # Shape (3, 2)
reshaped_array3 = array.reshape(6, 1)  # Shape (6, 1)

# ====== Display Properties ======
def display_array_info(name, arr):
    print(f"{name}:\n{arr}")
    print(f"Shape: {arr.shape}")
    print(f"Size: {arr.size}")
    print(f"Dimensions: {arr.ndim}\n")

# Scalar Info
display_array_info("Scalar", scalar)

# Array Info
display_array_info("Array", array)

# Matrix Info
display_array_info("Matrix", matrix)

# Reshaped Arrays Info
display_array_info("Reshaped Array 1 (2x3)", reshaped_array1)
display_array_info("Reshaped Array 2 (3x2)", reshaped_array2)
display_array_info("Reshaped Array 3 (6x1)", reshaped_array3)

# ====== Flattening Arrays ======
print(f"Flattened Matrix:\n{matrix.flatten()}\n")

# ====== Indexing ======
print(f"Element at index [3] in Array: {array[3]}")
print(f"Element at index [1] in Matrix: {matrix[1]}")
print(f"Element at index [2, 2] in Matrix: {matrix[2, 2]}")
print(f"Slice [2:5] in Array: {array[2:6]}")
print(f"Slice [0:3, 1] in Matrix:\n{matrix[0:3, 1]}")
print(f"Slice [1:3, 0:2] in Matrix:\n{matrix[1:3, 0:2]}")
print(f"Slice [0:, 1:3] in Matrix:\n{matrix[0:, 1:3]}\n")

# ====== Boolean Masking ======
print(f"Elements in Matrix > 4:\n{matrix > 4}\n")

# ====== Fancy Indexing ======
print(f"Elements in Ages >= 18:\n{ages[ages >= 18]}")
