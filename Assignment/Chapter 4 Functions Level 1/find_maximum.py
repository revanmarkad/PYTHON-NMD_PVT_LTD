# Create a function find_max(a, b) that takes two numbers 
# as input and returns the maximum of the two.
 
def find_max(a, b):
    return a if a > b else b
 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

maximum = find_max(num1, num2)
print(f"The maximum of {num1} and {num2} is {maximum}")
