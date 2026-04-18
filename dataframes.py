import pandas as pd

# Creating a simple DataFrame of "Bugs" in a software project
data = {
    'bug_id': [101, 102, 103, 104],
    'priority': ['High', 'Low', 'High', 'Medium'],
    'status': ['Open', 'Closed', 'Open', 'Open'],
    'lines_of_code': [150, 20, 300, 45]
}

df = pd.DataFrame(data)

print(df)

print(df.head())
print(df.describe())
print(df[(df['priority'] == 'High') & (df['lines_of_code'] > 160)])