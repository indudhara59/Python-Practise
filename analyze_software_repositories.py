import pandas as pd
from tabulate import tabulate

# 1. Load the data (Requirement from Course Content)
df = pd.read_csv('software_repo_data.csv')

# 2. Filtering: Find only 'High' priority tasks
# This relates to "software architecture and maintenance tasks" 
high_priority = df[df['priority'] == 'High']

# 3. Statistical Analysis: Group by developer to see workload
# This is a core "Data Science technique" for SE 
workload = df.groupby('developer_name')['lines_added'].sum()

print("--- High Priority Commits ---")
print(high_priority)
print("\n--- Total Lines Added per Developer ---")
print(workload)

print(df)


# print(df.to_markdown()) # Great for your Git README
# # OR
print(tabulate(df, headers='keys', tablefmt='psql'))