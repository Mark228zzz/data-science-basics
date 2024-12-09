import pandas as pd

# example data
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'B', 'D', 'C', 'B', 'A', 'D', 'D', 'A', 'B', 'C', 'D', 'D'],
    'Values': [10, 20, 10, 30, 20, 10, 40, 30, 20, 10, 10, 10, 20, 20, 30, 20, 30]
}

# create a DataFrame
df = pd.DataFrame(data=data)
print(f'Data:\n{df}\n')

# value counts for 'Category'
value_counts = df['Category'].value_counts()
print(f'Value counts "Category":\n{value_counts}\n')

# group by 'Category' and count occurrences
grouped_counts = df.groupby('Category').size()
print(f'Grouped counts "Category":\n{grouped_counts}\n')

# group by 'Category' and compute aggregate metrics
grouped_agg = df.groupby('Category')['Values'].agg(['count', 'mean', 'sum', 'max', 'min'])
grouped_reset = grouped_agg.reset_index()
print(f'Grouped metrics by "Category":\n{grouped_reset}\n')
