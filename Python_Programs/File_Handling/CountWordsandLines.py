def count_words_lines(filename):
    with open(filename, "r") as file:
        content = file.read()
        words = len(content.split())
        lines = len(content.splitlines())
    return words, lines

# User input
filename = input("Enter the file name to count words and lines: ")
try:
    words, lines = count_words_lines(filename)
    print(f"Words: {words}, Lines: {lines}")
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
