import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Alex'],
    'age': [25, 30, 21],
    'city': ['New York', 'Montreal', 'Chicago']
}

df = pd.DataFrame(data=data, index=['a', 'b', 'c'])

# accessing a single colomn
print(f'Accessing single colomn "name":\n{df['name']}\n')

# accessing multiple colomns
print(f'Accessing multiple colomns "name" and "city":\n{df[['name', 'city']]}\n')

# accessing rows by index position using iloc
print(f'Accessing first row using iloc:\n{df.iloc[0]}\n')
print(f'Accessing first and third row:\n{df.iloc[0:3:2]}\n')

# accessing to values in data
print(f'Accessing second row third value:\n{df.iloc[1, 2]}\n')

# accessing the row with label "b" using loc
print(f'Accessing row with label "b" using iloc:\n{df.loc['b']}\n')

# accessing rows with a condition
print(f'Rows where "age" > 23:\n{df[df['age'] > 23]}\n')

# accessing specific element
print(f'Accessing specific element (row a (0), column "name")\n{df.at['a', 'name']}\n')
