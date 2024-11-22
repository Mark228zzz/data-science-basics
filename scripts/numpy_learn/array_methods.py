import numpy as np

# create arrays
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
matrix2 = np.array([
    [1, 2],
    [3, 4]
])

vector1 = np.array([3.0, 7.0, 5.2, 2, 3.5, 2.6, 1.4, 0.3])

# print arrays
print(f'matrix1 =\n{matrix1}\n')
print(f'matrix2 =\n{matrix2}\n')
print(f'{vector1 = }\n')

# transpose arrays
print(f'Transpose of matrix1:\n{matrix1.T}\n')
print(f'Transpose of matrix2:\n{matrix2.T}\n')

# sum of arrays
print(f'Sum of matrix1: {matrix1.sum()}')
print(f'Sum of matrix2: {matrix2.sum()}')
print(f'Sum of vector1: {vector1.sum()}\n')

# mean of arrays
print(f'Mean of matrix1: {matrix1.mean()}')
print(f'Mean of matrix2: {matrix2.mean()}')
print(f'Mean of vector1: {vector1.mean()}\n')

# max of arrays
print(f'Max of matrix1: {matrix1.max()}')
print(f'Max of matrix2: {matrix2.max()}')
print(f'Max of vector1: {vector1.max()}\n')

# min of arrays
print(f'Min of matrix1: {matrix1.min()}')
print(f'Min of matrix2: {matrix2.min()}')
print(f'Min of vector1: {vector1.min()}\n')

# std of arrays
print(f'Std of matrix1: {matrix1.std()}')
print(f'Std of matrix2: {matrix2.std()}')
print(f'Std of vector1: {vector1.std()}\n')

# argmax and argmin. They will print element index
print(f'Argmax of matrix1: {matrix1.argmax()}')
print(f'Argmin of matrix1: {matrix1.argmin()}')
