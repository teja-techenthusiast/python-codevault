def count_even_odd(start, end):
    even_count = sum(1 for i in range(start, end + 1) if i % 2 == 0)
    odd_count = sum(1 for i in range(start, end + 1) if i % 2 != 0)
    return even_count, odd_count

# User input
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
even_count, odd_count = count_even_odd(start, end)
print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")
