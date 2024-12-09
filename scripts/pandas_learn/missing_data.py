import pandas as pd

# creating DataFrame with missing values
data = {
    'name': ['Alice', 'Bob', None],
    'age': [30, 22, None],
    'city': [None, 'Los Angeles', 'New York']
}

df = pd.DataFrame(data=data)

# print info about DataFrame to see the missing values
print(f'DataFrame info:\n{df.info()}\n')

# check for missing values
print(f'Check for missing values:\n{df.isnull()}\n')

# drop rows with missing values
df_dropped = df.dropna()
print(f'DataFrame after dropping missing values:\n{df_dropped}\n')

# fill missing values with a constant
df_filled = df.fillna({'name': 'NONAME', 'age': -1, 'city': 'UNKNOWN'})
print(f'DataFrame after filling missing values:\n{df_filled}\n')

# interpolate missing values (for numerical columns)
df_interpolated = df['age'].interpolate()
print(f'DataFrame after interpolating missing values in "age":\n{df_interpolated}\n')

# check for NaN and non-NaN values
print(f'Check if values is NaN:\n{df['name'].isna()}\n')
print(f'Check if values is NOT NaN:\n{df['name'].notna()}\n')

# count missing values per column
print(f'Counting NaN values per column:\n{df.isna().sum()}\n')
