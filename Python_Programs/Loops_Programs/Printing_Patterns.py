def print_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def print_square(n):
    for i in range(n):
        print("*" * n)

def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# User input
n = int(input("Enter the number of rows for the pattern: "))
print("Triangle:")
print_triangle(n)
print("Square:")
print_square(n)
print("Pyramid:")
print_pyramid(n)
