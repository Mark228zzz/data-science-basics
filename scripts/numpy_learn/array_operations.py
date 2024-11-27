import numpy as np

# create arrays
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

# print all arrays
print(f'{array1 = }')
print(f'{array2 = }')
print(f'{array3 = }')
print(f'matrix1 = \n{matrix1}')
print(f'matrix2 = \n{matrix2}\n')

# adding arrays
print(f'Addition:\n{array1 + array2 = }\n')

# multiplicating arrays
print(f'Multiplication:\n{array1 * array2 = }\n')

# subtracting arrays
print(f'Subtraction:\n{array1 - array2 = }\n')

# matrix multiplicating arrays
print(f'matmul1: matrix1 @ matrix2 = \n{np.matmul(matrix1, matrix2)}\n') # or `matrix1 @ matrix2` or `matrix1.dot(matrix2)`
print(f'matmul2: matrix2 @ array3 = \n{np.matmul(matrix2, array3)}\n') # or `matrix2 @ array3` or `matrix2.dot(array3)`

# scalar multiplicating array
print(f'Scalar multiplication:\n{array2 * 3 = }\n')

# broadcasting addition array
print(f'Broadcasting addition:\n{array1 + 7 = }')
