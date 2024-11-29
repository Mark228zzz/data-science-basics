import numpy as np

# ====== Scalar ======
scalar = np.array(5)
print(f"Scalar:\n{scalar}\n")

# ====== 1D Array/Vector ======
array1d = np.array([1, 2, 3, 4])
print(f"1D Array/Vector:\n{array1d}\n")

# ====== 2D Array/Matrix ======
array2d = np.array([
    [1, 2],
    [3, 4]
])
print(f"2D Array/Matrix:\n{array2d}\n")

# ====== Arrays with Predefined Values ======
zeros = np.zeros((2, 4))  # Array of zeros with shape (2, 4)
print(f"Zeros Array:\n{zeros}\n")

ones = np.ones((3, 3))  # Array of ones with shape (3, 3)
print(f"Ones Array:\n{ones}\n")

identity = np.eye(3)  # Identity matrix of size 3x3
print(f"Identity Array:\n{identity}\n")

# ====== Arrays with Ranges ======
arange_array1 = np.arange(5, 9)  # Array from 5 to 8
print(f"Arange Array1 (5 to 9):\n{arange_array1}")

arange_array2 = np.arange(10, 20, 2)  # Array from 10 to 18 with step 2
print(f"Arange Array2 (10 to 20, step 2):\n{arange_array2}\n")

# ====== Randomized Arrays ======
randn_array = np.random.randn(2, 2)  # Random array with normal distribution
print(f"Random Normal Array (randn):\n{randn_array}\n")

randint_array = np.random.randint(0, 2, size=10)  # Random integers (0 or 1), size 10
print(f"Random Integer Array (randint):\n{randint_array}\n")

choice_array = np.random.choice(['Apple', 'Banana', 'Egg'], size=6)  # Random choices
print(f"Random Choice Array:\n{choice_array}\n")
