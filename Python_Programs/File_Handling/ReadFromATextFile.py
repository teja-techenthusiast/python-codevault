def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

# User input
filename = input("Enter the file name to read: ")
try:
    print(read_file(filename))
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
