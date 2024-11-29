import numpy as np

# basic dtype usage
int_array = np.array([1, 2, 3, 4], dtype=np.int32)
float_array = np.array([1.1, 0.0, 3.8, 4.0], dtype=np.float64)
complex_array = np.array([1 + 2j, 2 + 3j], dtype=np.complex128)

print(f'Integer array: {int_array}')
print(f'Floating-point array: {float_array}')
print(f'Complex number array: {complex_array}\n')

# change dtype
converted_int_array = float_array.astype(np.int32)
bool_array = float_array.astype(np.bool_)

print(f'Converted to integer: {converted_int_array}')
print(f'Converted to boolean: {bool_array}\n')

# unsigned integer array
unsigned_int_array = np.array([1, 2, 3, 4], dtype=np.uint8)
print(f'Unsigned integer array: {unsigned_int_array}\n')

# structured array
structured_array = np.array([(1, 'John', 22), (2, 'Alice', 23)], dtype=[('ID', np.int32), ('Name', 'U10'), ('Age', np.int32)])
print(f'Structured array: \n{structured_array}\n')
print(f'Names: {structured_array["Name"]}\n')

# mixed dtype arithmetic
mixed_array = np.array([1, 2, 3], dtype=np.int32) + np.array([0.5, 1.5, 2.5], dtype=np.float64)
print(f'Mixed dtype array: {mixed_array}\n')

# optimizing memory for large arrays
large_array = np.arange(1000000, dtype=np.int16)
print(f'Large array (first and last 5 elements): {large_array[:5]}... {large_array[-5:]}\n')

# load data with specified dtype
data = np.genfromtxt('data/csvs/numbers.csv', dtype=np.int32)
print(f'Loaded data with dtype np.int32:\n{data}\n')

data = np.genfromtxt('data/csvs/numbers.csv', dtype=np.float32)
print(f'Loaded data with dtype np.float32:\n{data}\n')
