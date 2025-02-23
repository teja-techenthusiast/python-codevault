def count_words(s):
    return len(s.split())

# User input
s = input("Enter a string to count the words: ")
print(f"Number of words: {count_words(s)}")
