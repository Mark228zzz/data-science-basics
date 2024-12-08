import pandas as pd

# read from CSV files
coffee = pd.read_csv('./data/csvs/coffee.csv')

# print all data
print(f'Full DataFrame:\n{coffee}\n')

# print column "Coffee Type"
print(f'Coffee Type:\n{coffee["Coffee Type"]}\n')

# print general info
print(f'Info:\n{coffee.info()}\n')

# print first 3 rows, default 5
print(f'Head:\n{coffee.head(3)}\n')

# print last 2 rows, default 5
print(f'Tail:\n{coffee.tail(2)}\n')

# print summary statistics for numerical data
print(f'Describtion:\n{coffee.describe()}\n')

# print indexes and columns
print(f'Indexes: {coffee.index.to_list()}\n')
print(f'Columns: {coffee.columns.to_list()}\n')

# print data types of each column
print(f'DataFrame dtypes:\n{coffee.dtypes}\n')

# print nunique values count per column
print(f'Nunique:\n{coffee.nunique()}\n')

# print unique values in "Day"
print(f'Unique:\n{coffee['Day'].unique()}\n')

# drop a row
df_dropped_row = coffee.drop([0, 1, 2, 13])
print(f'After dropping the rows from 0 to 3 and 13:\n{df_dropped_row}\n')

# drop a column
df_dropped_column = coffee.drop('Units Sold', axis=1) # axis=0 is rows, axis=1 is columns OR just columns='Units Sold'
print(f'After dropping the column "Units Sold":\n{df_dropped_column}\n')

# conditional filtering
filtered_df = coffee.query('`Units Sold` > 30')
print(f'Filtered DataFrame by "Units Sold" > 30:\n{filtered_df}\n')

# replace values where condition is not met
df_replaced = coffee.where(coffee['Units Sold'] > 30, 'NONE')
print(f'Replace "Units Sold with NONE":\n{df_replaced}\n')

# add a new column
coffee['Price'] = [4.99, 3.99, 4.99, 3.99, 4.99, 3.99, 4.99, 3.99, 4.99, 3.99, 4.99, 3.99, 4.99, 3.99]
print(f'After adding "Price" in DataFrame:\n{coffee}\n')

# sorting data and reset indexes
df_sorted = coffee.sort_values(by='Units Sold', ascending=False)
df_reset = df_sorted.reset_index(drop=True)
print(f'Sorted DataFrame:\n{df_reset}\n')

# grouping and aggregation
df_grouped = coffee.groupby('Coffee Type')['Units Sold'].mean()
print(f'Average Units Sold by Coffee Type:\n{df_grouped}\n')

# calculate revenue
coffee['Revenue'] = coffee['Units Sold'] * coffee['Price']
print(f'New DataFrame after calculating "Revenue":\n{coffee}\n')

# rename "Coffee Type" with "Type of Coffee"
coffee.rename(columns={'Coffee Type': 'Type of Coffee'}, inplace=True)
print(f'Re')
