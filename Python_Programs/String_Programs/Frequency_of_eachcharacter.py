from collections import Counter

def character_frequency(s):
    return dict(Counter(s))

# User input
s = input("Enter a string to find the frequency of each character: ")
print(f"Character frequencies: {character_frequency(s)}")
