# Concatenation
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2

# Slicing
def slice_tuple(tup, start, end):
    return tup[start:end]

# Repetition
def repeat_tuple(tup, n):
    return tup * n

# User input
tup1 = tuple(map(int, input("Enter the first tuple of numbers: ").split()))
tup2 = tuple(map(int, input("Enter the second tuple of numbers: ").split()))
print(f"Concatenated tuple: {concatenate_tuples(tup1, tup2)}")
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
print(f"Sliced tuple: {slice_tuple(tup1, start, end)}")
n = int(input("Enter a number for repetition: "))
print(f"Repeated tuple: {repeat_tuple(tup1, n)}")
