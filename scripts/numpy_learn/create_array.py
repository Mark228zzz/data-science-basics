import numpy as np

# create a scalar
scalar = np.array(5)
print(f'Scalar: {scalar}\n')

# create a 1D array/vector
array1d = np.array([1, 2, 3, 4])
print(f'1D array/vector:\n{array1d}\n')

# create an 2d array/matrix
array2d = np.array([
    [1, 2],
    [3, 4]
])
print(f'2D array/matrix:\n{array2d}\n')

# create an array with all zeros
zeros = np.zeros((2, 4)) # we have to type a shape of array
print(f'Zeros array:\n{zeros}\n')

# create an array with all ones
ones = np.ones((3, 3))
print(f'Ones array:\n{ones}\n')

# create an identity array
identity = np.eye(3)
print(f'Identity array:\n{identity}\n')

# create an array with arange
arange_array1 = np.arange(5, 9)
print(f'Arange array1: {arange_array1}')

arange_array2 = np.arange(10, 20, 2)
print(f'Arange array2: {arange_array2}\n')

# create a random array
randn_array = np.random.randn(2, 2)
print(f'Randn array:\n{randn_array}')

randint_array = np.random.randint(0, 2, size=10)
print(f'Randint array: {randint_array}')

choice_array = np.random.choice(['Apple', 'Banana', 'Egg'], size=6)
print(f'Choice array: {choice_array}')
