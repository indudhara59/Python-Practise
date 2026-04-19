import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. SETUP & DATA (From Module 1)
# ==========================================
try:
    df = pd.read_csv('software_repo_data.csv')
except FileNotFoundError:
    # Creating sample data if you haven't run previous modules
    data = {
        'commit_id': ['c001', 'c002', 'c003', 'c004', 'c005', 'c006', 'c007', 'c008', 'c009', 'c010'],
        'message': ['Fix login bug', 'Update readme', 'Major refactor of auth', 'Typo fix', 'Add minor style', 
                    'Heavy clustering logic', 'Fix link', 'Add pandas helper', 'Small fix', 'Initial DS pipeline'],
        'priority': ['Medium', 'Low', 'High', 'Low', 'Low', 'High', 'Low', 'Medium', 'Low', 'High']
    }
    df = pd.DataFrame(data)

# ==========================================
# 2. NLP PRE-PROCESSING (From Module 2)
# ==========================================
def clean_text(text):
    # Lowercase and remove non-letters
    return re.sub(r'[^a-z\s]', '', text.lower())

df['clean_message'] = df['message'].apply(clean_text)

# ==========================================
# 3. VECTORIZATION (From Module 4)
# ==========================================
# Turning text into numbers is required for Information Retrieval
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_message'])

# ==========================================
# 4. INFORMATION RETRIEVAL LOGIC (Module 5)
# ==========================================
def search_repository(query):
    """
    Finds the most similar commit message to a user's search query.
    """
    # Clean and transform the user query
    clean_query = clean_text(query)
    query_vec = vectorizer.transform([clean_query])
    
    # Calculate Cosine Similarity between query and all messages
    # This measures the 'distance' between the query and the repository data
    similarities = cosine_similarity(query_vec, X).flatten()
    
    # Get the index of the highest similarity score
    best_match_index = similarities.argmax()
    
    return df.iloc[best_match_index], similarities[best_match_index]

# ==========================================
# 5. EXECUTION & REPORTING
# ==========================================
user_query = "Fix bUg"
result, score = search_repository(user_query)

print(f"--- Information Retrieval Result ---")
print(f"Query: '{user_query}'")
print(f"Best Match: {result['message']}")
print(f"Priority: {result['priority']}")
print(f"Similarity Score: {score:.2f}")