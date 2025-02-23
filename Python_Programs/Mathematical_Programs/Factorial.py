#with recurssion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

#without recurssion
''' def factorial(n):
    result = 1
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return result
    else:
        for i in range(2, n + 1):
            result *= i
        return result

# Example:  
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
'''