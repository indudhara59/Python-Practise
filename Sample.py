# The original template
letter = '''
Dear <|Name|>,
You are selected!
Joining Date: <|Date-|>
'''

# Information to fill in
name = input("Enter you name: ")
date = input("Enter the date of joining: ")

# Replacing the placeholders
formatted_letter = letter.replace("<|Name|>", name)
formatted_letter = formatted_letter.replace("<|Date-|>", date)

# Printing the result
print(formatted_letter)