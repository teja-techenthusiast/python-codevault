def copy_file(source, destination):
    with open(source, "r") as src_file:
        content = src_file.read()
    with open(destination, "w") as dest_file:
        dest_file.write(content)

# User input
source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")
try:
    copy_file(source, destination)
    print(f"Contents copied from '{source}' to '{destination}'.")
except FileNotFoundError:
    print(f"The file '{source}' was not found.")
