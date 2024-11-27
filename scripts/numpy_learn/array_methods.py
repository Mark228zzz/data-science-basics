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

matrix3 = np.array([
    [3, 2, 6],
    [7, 4, 9]
])

vector1 = np.array([3.0, 7.0, 5.2, 2.1, 3.5, 2.6, 1.4, 0.2])
numbers1 = np.array([1, 2, 3])
numbers2 = np.array([4, 5, 6])
expenses = np.array([np.nan, np.nan, 200.0, 650.0, 1525.0, np.nan])

# print arrays
print(f'matrix1 =\n{matrix1}\n')
print(f'matrix2 =\n{matrix2}\n')
print(f'matrix3 =\n{matrix3}\n')
print(f'{vector1 = }\n')
print(f'{numbers1 = }\n')
print(f'{numbers2 = }\n')
print(f'{expenses = }\n')

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
print(f'Argmin of matrix1: {matrix1.argmin()}\n')

# concatenating arrays
combined_numbers = np.concatenate((numbers1, numbers2))
print(f'Combined numbers: {combined_numbers}')

combined_matrix = np.concatenate((matrix2, matrix2))
print(f'Combined matrix:\n{combined_matrix}\n')

# spliting arrays
print(f'Splited combined_numbers by 2 batches: {np.split(combined_numbers, 2)}')
print(f'Splited combined_numbers by 3 batches: {np.split(combined_numbers, 3)}')
print(f'Splited matrix2: {np.split(matrix2, 2)}')

# sorting arrays
print(f'Sorted vector1: {np.sort(vector1)}')
print(f'Sorted matrix3:\n{np.sort(matrix3, axis=1)}\n')

# handling missing data
cleaned_expenses = np.nan_to_num(expenses, nan=0.0)
print(f'Cleaned expenses: {cleaned_expenses}')
