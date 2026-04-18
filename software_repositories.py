import pandas as pd

data = {
    'commit_id': ['c001', 'c002', 'c003', 'c004', 'c005', 'c006', 'c007', 'c008', 'c009', 'c010'],
    'developer_name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'Dave'],
    'lines_added': [120, 45, 600, 10, 30, 750, 15, 200, 50, 1000],
    'priority': ['Medium', 'Low', 'High', 'Low', 'Low', 'High', 'Low', 'Medium', 'Low', 'High'],
    'message': ['Fix bug', 'Update readme', 'Auth refactor', 'Typo', 'Style', 'Clustering', 'Link', 'Helper', 'Fix', 'Pipeline']
}

df = pd.DataFrame(data)
df.to_csv('software_repo_data.csv', index=False)
print("File 'software_repo_data.csv' created successfully!")