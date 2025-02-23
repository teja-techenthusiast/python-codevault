def append_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")

# User input
filename = input("Enter the file name to append text to: ")
text = input("Enter the text to append: ")
append_to_file(filename, text)
print(f"Text appended to '{filename}'.")
