import numpy as np

# create arrays and reshaped version of them
array = np.array([1, 2, 3, 4, 5, 6])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
reshaped_array1 = array.reshape(2, 3)
reshaped_array2 = array.reshape(3, 2)
reshaped_array3 = array.reshape(6, 1)

# print origin arrays
print(f'{array = }')
print(f'Array shape: {array.shape}') # The form of the array
print(f'Array size: {array.size}\n') # The number of all elements in the array

print(f'Matrix:\n{matrix}')
print(f'Matrix shape: {matrix.shape}')
print(f'Matrix size: {matrix.size}\n')

# reshaping arrays
print(f'Reshaped array1 to (2, 3):\n{reshaped_array1}')
print(f'Reshaped array1 shape: {reshaped_array1.shape}\n')

print(f'Reshaped array2 to (3, 2):\n{reshaped_array2}')
print(f'Reshaped array1 shape: {reshaped_array2.shape}\n')

print(f'Reshaped array2 to (6, 1):\n{reshaped_array3}')
print(f'Reshaped array1 shape: {reshaped_array3.shape}\n')

# flattening arrays
print(f'Flatten matrix: {matrix.flatten()}')

# indexing arrays
print(f'Element at index [3] in array: {array[3]}')
print(f'Element at index [1] in matrix: {matrix[1]}')
print(f'Element at index [2, 2] in matrix: {matrix[2, 2]}')
print(f'Element at index [2:5] in array: {array[2:6]}')
print(f'Element at index [0:3, 1] in matrix: {matrix[0:3, 1]}')
print(f'Element at index [1:3, 0:2] in matrix:\n{matrix[1:3, 0:2]}')
print(f'Element at index [0:, 1:3] in matrix:\n{matrix[0:, 1:3]}')

# boolean masking arrays
print(f'Elements greater that 4:\n{matrix > 4}') # True if element greater than 4 else False
