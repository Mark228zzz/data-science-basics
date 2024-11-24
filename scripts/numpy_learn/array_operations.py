import numpy as np

# create arrays
a = np.array([1, 2, 7])
b = np.array([2, 6, 2])
c = np.array([4, 2])
matrix1 = np.array([
    [3, 1],
    [1, 2]
])
matrix2 = np.array([
    [6, -4],
    [1, 2]
])

# print all arrays
print(f'{a = }')
print(f'{b = }')
print(f'matrix1 = \n{matrix1}')
print(f'matrix2 = \n{matrix2}\n')

# adding arrays
print(f'Addition:\n{a + b = }\n')

# multiplicating arrays
print(f'Multiplication:\n{a * b = }\n')

# subtracting arrays
print(f'Subtraction:\n{a - b = }\n')

# matrix multiplicating arrays
print(f'matmul1:\nmatrix1 @ matrix2 = \n{np.matmul(matrix1, matrix2)}\n') # or `matrix1 @ matrix2` or `matrix1.dot(matrix2)`
print(f'matmul2:\nmatrix2 @ c = \n{np.matmul(matrix2, c)}\n') # or `matrix2 @ c` or `matrix2.dot(c)`

# scalar multiplicating array
print(f'Scalar multiplication:\n{b * 3 = }\n')

# Broadcasting addition array
print(f'Broadcasting Addition:\n{a + 7 = }')
