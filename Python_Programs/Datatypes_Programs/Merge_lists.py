def merge_lists(lst1, lst2):
    return lst1 + lst2

# User input
lst1 = list(map(int, input("Enter the first list of numbers: ").split()))
lst2 = list(map(int, input("Enter the second list of numbers: ").split()))
print(f"Merged list: {merge_lists(lst1, lst2)}")
