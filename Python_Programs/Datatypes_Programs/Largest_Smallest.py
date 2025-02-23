def largest_smallest(lst):
    largest = lst[0]
    smallest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Largest and Smallest:", largest_smallest(lst))