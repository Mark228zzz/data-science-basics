import pandas as pd

# example sales data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Sales': [100, 200, 150, 300, 250],
    'Units Sold': [10, 20, 15, 30, 25]
}

# create DataFrame
df = pd.DataFrame(data)

# print DataFrame
print(f'DataFrame:\n{df}\n')

# 1. pivoting the data to get total sales by category
pivot_df = df.pivot(index='Date', columns='Category', values='Sales')
print(f"Pivot table:\n{pivot_df}\n")

# 2. rolling window to calculate the rolling sum of 'Sales'
df['Rolling_Sales'] = df['Sales'].rolling(window=2).sum()
print(f"Rolling sum of sales:\n{df[['Date', 'Sales', 'Rolling_Sales']]}\n")

# 3. shifting the 'Units Sold' column by 1 to get previous day's units sold
df['Units_Sold_Shifted'] = df['Units Sold'].shift(1)
print(f"Shifted units sold:\n{df[['Date', 'Units Sold', 'Units_Sold_Shifted']]}\n")

# 4. ranking the 'Sales' column in descending order
df['Sales_Rank'] = df['Sales'].rank(ascending=False)
print(f"Sales rank:\n{df[['Date', 'Sales', 'Sales_Rank']]}\n")

# 5. cumulative sum of the 'Sales'
df['Cumulative_Sales'] = df['Sales'].cumsum()
print(f"Cumulative Sales:\n{df[['Date', 'Sales', 'Cumulative_Sales']]}\n")
