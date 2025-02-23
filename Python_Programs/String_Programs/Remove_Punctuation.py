import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# User input
s = input("Enter a string to remove punctuation: ")
print(f"String without punctuation: {remove_punctuation(s)}")
