# Program to calculate the sum of even digits in a given number

try:
   
    number = input("Enter a number: ")

    # Initialize sum of even digits
    even_sum = 0

    # Loop through each digit in the number
    for digit in number:
        if digit.isdigit():  # Check if the character is a digit
            if int(digit) % 2 == 0:  # Check if the digit is even
                even_sum += int(digit)

    # Print the sum of even digits
    print(f"The sum of even digits is: {even_sum}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
