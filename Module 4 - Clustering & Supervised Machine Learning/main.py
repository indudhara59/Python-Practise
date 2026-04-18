import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# ==========================================
# MODULE 1: DATA LOADING & PREPARATION
# ==========================================
# In your course, you analyze "software repositories".
# This mimics a repository export you might get on Monday.
try:
    df = pd.read_csv('software_repo_data.csv')
except FileNotFoundError:
    # Creating sample data if the file doesn't exist
    data = {
        'commit_id': ['c001', 'c002', 'c003', 'c004', 'c005', 'c006', 'c007', 'c008', 'c009', 'c010'],
        'developer_name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'Dave'],
        'lines_added': [120, 45, 600, 10, 30, 750, 15, 200, 50, 1000],
        'priority': ['Medium', 'Low', 'High', 'Low', 'Low', 'High', 'Low', 'Medium', 'Low', 'High'],
        'message': ['Fix login bug', 'Update readme', 'Major refactor of auth', 'Typo fix', 'Add minor style', 
                    'Heavy clustering logic', 'Fix link', 'Add pandas helper', 'Small fix', 'Initial DS pipeline']
    }
    df = pd.DataFrame(data)
    df.to_csv('software_repo_data.csv', index=False)

# ==========================================
# MODULE 2: NLP PIPELINE (TEXT CLEANING)
# ==========================================
# This addresses the "Natural language processing pipeline".
def clean_text(text):
    text = text.lower() # Case Normalization
    text = re.sub(r'[^a-z\s]', '', text) # Noise Removal
    tokens = text.split() # Tokenization
    return tokens

df['clean_tokens'] = df['message'].apply(clean_text)

# ==========================================
# MODULE 3: STATISTICAL ANALYSIS & VISUALIZATION
# ==========================================
# Used to "derive useful implications" and "present research results".

# Flattening the list of lists for word frequency analysis
all_words = [word for tokens in df['clean_tokens'] for word in tokens]
word_counts = Counter(all_words)
top_5 = word_counts.most_common(5)

# Visualizing the Keyword Trends
words, counts = zip(*top_5)
plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='midnightblue')
plt.title('Top 5 Keywords in Software Repository')
plt.xlabel('Tokens')
plt.ylabel('Frequency')
plt.savefig('keyword_analysis.png') # Saving for your scientific report 
print("Statistical chart saved as 'keyword_analysis.png'.")

# ==========================================
# MODULE 4: CLUSTERING (MACHINE LEARNING)
# ==========================================
# This covers "Clustering of source code" and "Topic modeling".

# 1. Convert text to numbers (Vectorization)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['message'])

# 2. Apply K-Means Clustering
# Grouping the "complex and heterogeneous" repo data into 3 topics.
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster_id'] = kmeans.fit_predict(X)

# ==========================================
# FINAL OUTPUT: THE SCIENTIFIC SUMMARY
# ==========================================
print("\n--- Final Analysis Result ---")
print(df[['message', 'priority', 'cluster_id']])

# Summary statistics for the "scientific format" report 
print("\n--- Repository Summary Statistics ---")
print(df.describe())