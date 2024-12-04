import pandas as pd
import numpy as np

# series from a list
series1 = pd.Series(data=[1, 6, 3, 8, 3])
print(f'Series from a list:\n{series1}\n')

# series from a dictionary, keys are the index
series2 = pd.Series(data={'a': 1, 'b': 2, 'c': 3})
print(f'Series from a dict:\n{series2}\n')

# series with custom index
series3 = pd.Series(data=[10, 20, 30], index=['x', 'y', 'z'])
print(f'Series with custom index:\n{series3}\n')

# series with missing values
series4 = pd.Series(data=[5, 6, None, 8, None, None, 11, 12])
print(f'Series with missing values:\n{series4}\n')

# series with string values
series5 = pd.Series(data=['apple', 'banana', 'orange', 'limon'])
print(f'Series with str values:\n{series5}\n')

# series from NumPy array
series6 = pd.Series(data=np.array([1.5, 2.5, 3.5, 4.5, 5.5]))
print(f'Series from NumPy array:\n{series6}\n')

# series with different data types
series7 = pd.Series(data=[1, 4, True, 'hello', 7.1])
print(f'Series with different data types:\n{series7}\n')

# series with data/time type, using pandas Timestamp
dates = pd.date_range('2024-01-01', periods=3, freq='D') # freq='D' means frequency every day
series8 = pd.Series(data=dates)
print(f'Series with data/time values:\n{series8}\n')
