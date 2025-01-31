# Program to check if a number is a multiple of 10

try:
   
    number = int(input("Enter a number: "))

    # Check if the number is a multiple of 10
    if number % 10 == 0:
        print(f"{number} is a multiple of 10.")
    else:
        print(f"{number} is not a multiple of 10.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
