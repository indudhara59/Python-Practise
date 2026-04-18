import pandas as pd
import re
from collections import Counter

# Load the data we made in Module 1
df = pd.read_csv('software_repo_data.csv')

def clean_text(text):
    # 1. Lowercase
    text = text.lower()
    # 2. Remove non-alphabet characters (punctuation/numbers)
    text = re.sub(r'[^a-z\s]', '', text)
    # 3. Simple Tokenization (split by space)
    tokens = text.split()
    return tokens

# Apply the cleaning to our 'message' column
df['clean_tokens'] = df['message'].apply(clean_text)

# print(df[['message', 'clean_tokens']].head())
print(df[['message', 'clean_tokens']])

# print(df)

# 1. Load the data (assuming you ran the previous cleaning code)
# df['clean_tokens'] currently looks like: [['fix', 'login', 'bug'], ['update', 'readme'], ...]

# --- TASK A: IDENTIFYING TRENDS (Word Frequency) ---
# We flatten the list of lists into one single list of all words used in the repo
all_words = [word for tokens in df['clean_tokens'] for word in tokens]

# Count how many times each word appears
word_counts = Counter(all_words)

print("--- Top 5 Most Common Words in Repository ---")
print(word_counts.most_common(5))


# --- TASK B: INFORMATION RETRIEVAL (Filtering by Keyword) ---
# Find all rows where the developer mentioned 'bug'
# This helps with 'software maintenance tasks' mentioned in your course doc
bug_related_commits = df[df['clean_tokens'].apply(lambda x: 'bug' in x)]

print("\n--- Commits Related to 'Bug' ---")
print(bug_related_commits[['message', 'priority']])


# --- TASK C: STATISTICAL ANALYSIS ---
# Calculate the average number of words per commit message
df['word_count'] = df['clean_tokens'].apply(len)
avg_length = df['word_count'].mean()

print(f"\nAverage words per commit: {avg_length}")

df.to_csv("new_dataframe.csv", index=False)