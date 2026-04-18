## 2.1 The "Cleaning" Steps

Before you can analyze a commit message like `"FIXED: the annoying bug in the login.js file!!!!"`, you must process it through a data pipeline to ensure consistency and accuracy.

### The Pipeline Process

1.  **Lowercasing** Convert all text to lowercase so that words like `"Bug"` and `"bug"` are treated as the same token.
    
2.  **Noise Removal** Strip out punctuation (e.g., `!!!`) and special characters that do not contribute to the core meaning of the message.
    
3.  **Tokenization** Split the full sentence into a list of individual words, known as **tokens**.
    
4.  **Stop-word Removal** Filter out common language fillers such as `"the"`, `"is"`, and `"in"`. These words are removed because they carry little to no specific technical meaning for analysis.