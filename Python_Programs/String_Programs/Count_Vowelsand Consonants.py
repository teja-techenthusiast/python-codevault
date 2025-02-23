def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    num_vowels = sum(ch in vowels for ch in s)
    num_consonants = sum(ch.isalpha() and ch not in vowels for ch in s)
    return num_vowels, num_consonants

s = input("Enter a string to count vowels and consonants: ")
v, c = count_vowels_consonants(s)
print(f"Vowels: {v}, Consonants: {c}")