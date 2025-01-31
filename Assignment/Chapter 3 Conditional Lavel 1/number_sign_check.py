    # Program to determine if a number is positive, negative, or zero

try:
        
    number = float(input("Enter a number: "))

    # Check if the number is zero or negative
    if number == 0:
        print(f"The given number is zero: {number}")
    elif number < 0:
        print(f"The given number is negative: {number}")
    # Check if the number is positive
    elif number > 0:
        print(f"The given number is positive: {number}")
            
except:
    print("Invalid input. Please enter a valid number.")
