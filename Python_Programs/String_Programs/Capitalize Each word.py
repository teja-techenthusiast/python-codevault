def capitalize_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

# User input
s = input("Enter a string to capitalize each word: ")
print(f"Capitalized string: {capitalize_each_word(s)}")
