def write_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

# User input
filename = input("Enter the file name to write to: ")
text = input("Enter the text to write to the file: ")
write_to_file(filename, text)
print(f"Text written to '{filename}'.")
