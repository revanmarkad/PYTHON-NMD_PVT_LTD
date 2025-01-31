# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1  # The factorial of 0 and 1 is 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
