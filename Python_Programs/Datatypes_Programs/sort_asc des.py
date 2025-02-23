def sort_list(lst, reverse=False):
    return sorted(lst, reverse=reverse)

# User input
lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(f"Sorted list (ascending): {sort_list(lst)}")
print(f"Sorted list (descending): {sort_list(lst, True)}")
