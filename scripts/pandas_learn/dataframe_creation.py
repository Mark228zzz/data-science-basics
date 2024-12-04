import pandas as pd
import numpy as np

# DataFrame from a dictionary of lists
data1 = {
    'name': ['Alice', 'Bob', 'Alex'],
    'age': [25, 30, 41],
    'city': ['New York', 'Montreal', 'Vancouver']
}

df1 = pd.DataFrame(data=data1)
print(f'DataFrame from dict:\n{df1}\n')

# DataFrame from a list of lists
data2 = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Montreal'],
    ['Alex', 41, 'Vancouver']
]

df2 = pd.DataFrame(data=data2)
print(f'DataFrame from list of lists:\n{df2}\n')

# DataFrame with a custom index
df3 = pd.DataFrame(data=data1, index=['a', 'b', 'c'])
print(f'DataFrame with custom index:\n{df3}\n')

# DataFrame from a NumPy array
arr = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
])

df4 = pd.DataFrame(data=arr, columns=['name', 'age', 'city'])
print(f"DataFrame from NumPy array:\n{df4}\n")
