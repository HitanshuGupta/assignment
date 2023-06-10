factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Test the lambda function
number = int(input("Enter the number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
