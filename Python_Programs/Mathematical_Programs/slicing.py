def string_slicing():
    text = "Hello, Python!"
    print("Original String:", text)
    print("First 5 characters:", text[:5])
    print("Last 6 characters:", text[-6:])
    print("Every 2nd character:", text[::2])
    print("Reverse String:", text[::-1])
    print()

def list_slicing():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80]
    print("Original List:", numbers)
    print("First 4 elements:", numbers[:4])
    print("Last 3 elements:", numbers[-3:])
    print("Elements from index 2 to 5:", numbers[2:6])
    print("Every 2nd element:", numbers[::2])
    print("Reverse List:", numbers[::-1])
    print()

def tuple_slicing():
    fruits = ("apple", "banana", "cherry", "date", "fig", "grape")
    print("Original Tuple:", fruits)
    print("First 3 fruits:", fruits[:3])
    print("Last 2 fruits:", fruits[-2:])
    print("Fruits from index 1 to 4:", fruits[1:5])
    print("Every 2nd fruit:", fruits[::2])
    print("Reverse Tuple:", fruits[::-1])
    print()

# Main Function
if __name__ == "__main__":
    string_slicing()
    list_slicing()
    tuple_slicing()
