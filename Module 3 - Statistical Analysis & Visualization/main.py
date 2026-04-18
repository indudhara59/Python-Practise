import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

# --- PRE-REQUISITE: LOAD & CLEAN (Module 2) ---
df = pd.read_csv('software_repo_data.csv')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    return tokens

df['clean_tokens'] = df['message'].apply(clean_text)

# --- MODULE 3: STATISTICAL ANALYSIS ---

# 1. Flatten all tokens into one list to count frequencies
all_words = [word for tokens in df['clean_tokens'] for word in tokens]
word_counts = Counter(all_words)

# 2. Extract Top 5 for the report
top_5 = word_counts.most_common(10)
words = [item[0] for item in top_5]
counts = [item[1] for item in top_5]

# --- MODULE 3: VISUALIZATION ---

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Create the Bar Chart
plt.bar(words, counts, color='midnightblue') # Using your preferred "Midnight" aesthetic

# Add scientific labels as per course requirements
plt.xlabel('Extracted Keywords (Tokens)', fontsize=12)
plt.ylabel('Frequency of Occurrence', fontsize=12)
plt.title('Top 5 Keywords in Software Repository Analysis', fontsize=14)

# Save the result for your Git Repository
plt.savefig('repo_analysis_chart.png')
print("Analysis Complete. Chart saved as 'repo_analysis_chart.png'")

# Show the plot on screen
plt.show()