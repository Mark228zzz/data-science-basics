import numpy as np

# create a scalar
scalar = np.array(5)
print(f'Scalar: {scalar}\n')

# create a 1D array/vector
array1d = np.array([1, 2, 3, 4])
print(f'1D array/vector:\n{array1d}\n')

# create a 2d array/matrix
array2d = np.array([
    [1, 2],
    [3, 4]
])
print(f'2D array/matrix:\n{array2d}\n')

# create a array with all zeros
zeros = np.zeros((2, 4)) # we have to type a shape of array
print(f'Zeros array:\n{zeros}\n')

# create a array with all ones
ones = np.ones((3, 3))
print(f'Ones array:\n{ones}\n')

# create an identity array
identity = np.eye(3)
print(f'Identity array:\n{identity}')
