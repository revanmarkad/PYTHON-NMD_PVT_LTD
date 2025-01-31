# Program to check if a number is within a given range

try:
    # Take input for the number and the range limits
    number = float(input("Enter the number: "))
    lower_limit = float(input("Enter the lower limit of the range: "))
    upper_limit = float(input("Enter the upper limit of the range: "))

    # Check if the number is within the given range
    if lower_limit <= number <= upper_limit:
        print(f"The number {number} is within the range ({lower_limit}, {upper_limit}).")
    else:
        print(f"The number {number} is outside the range ({lower_limit}, {upper_limit}).")

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
