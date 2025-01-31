# Function to check if a number is even or odd
def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

# Example usage
num = int(input("Enter an integer: "))
result = is_even(num)
print(f"The number {num} is {result}.")

