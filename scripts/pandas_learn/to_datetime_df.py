import pandas as pd

# example data
data = {
    'Event': ['Start', 'Middle', 'End'],
    'Date': ['2024-12-01', '12/05/2024', 'December 9, 2024'],
    'Time': ['14:00', '16:30', '18:45']
}

# create a DataFrame
df = pd.DataFrame(data=data)
print(f'DataFrame:\n{df}\n')

# convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')
print(f'After converting "Date" to datetime:\n{df}\n')

# combine 'Date' and 'Time' into a single datetime column
df['Datetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'], errors='coerce', format='mixed')
print(f'After creating "Datetime" column:\n{df}\n')

# extract year, month, and day from datetime
df['Year'] = df['Datetime'].dt.year
df['Month'] = df['Datetime'].dt.month
df['Day'] = df['Datetime'].dt.day
df['Weekday'] = df['Datetime'].dt.weekday
print(f'Adding "Year", "Month", "Day", "Weekday" in the DataFrame:\n{df}\n')

# filter events after a specific date
filtered_df = df[df['Datetime'] > pd.Timestamp('2024-12-03')]
print(f'Events After 2024-12-03:\n{filtered_df}\n')
