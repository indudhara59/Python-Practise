import pandas as pd

df = pd.read_csv('software_repo_data.csv')

print(df)

# Group by developer and count their commits
commit_counts = df.groupby('developer_name')['commit_id'].count()

print(commit_counts)