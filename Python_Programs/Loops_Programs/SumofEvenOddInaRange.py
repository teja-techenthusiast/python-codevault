def sum_even_odd(start, end):
    even_sum = sum(i for i in range(start, end + 1) if i % 2 == 0)
    odd_sum = sum(i for i in range(start, end + 1) if i % 2 != 0)
    return even_sum, odd_sum

# User input
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
even_sum, odd_sum = sum_even_odd(start, end)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
