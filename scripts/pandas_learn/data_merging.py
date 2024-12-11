import pandas as pd

# example DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'age': [25, 30, 23]})
df3 = pd.DataFrame({'key': [1, 2, 3], 'value': ['196', '263', '512']})

# merge on "ID", how='outer'
merged_df = pd.merge(df1, df2, on='ID', how='outer')
print(f'Merge df1 and df2, on="ID", how="outer":\n{merged_df}\n')

# merge on "ID", how='inner'
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(f'Merge df1 and df2, on="ID", how="inner":\n{merged_df}\n')

# specity different column names
merged_custom_df = pd.merge(df1, df3, left_on='ID', right_on='key', how='inner')
print(f'Custom merge df1 and df3:\n{merged_custom_df}\n')

# concarenate df1 and df2
concat_df = pd.concat([df1, df2], ignore_index=True)
print(f'Concat df1 and df2:\n{concat_df}\n')

# horizontal concatenation
concat_horizontal = pd.concat([df1, df2], axis=1)
print(f'Horizontal concatenation\n{concat_horizontal}\n', )

# concatenation with keys
concat_with_keys = pd.concat([df1, df2], keys=['First', 'Second'])
print(f'Concatenation with keys \n{concat_with_keys}\n')
