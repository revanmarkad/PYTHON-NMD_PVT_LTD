#  Write a program that takes an integer input and prints "Odd" if the number is odd and "Even" if it's even.

try:
    inp = int(input("Enter a number: "))

    if inp % 2 == 0:
        print(f"The given number {inp} is even.")
    else:
        print(f"The given number {inp} is odd.")
        
except ValueError:
    print("Invalid input! Please enter a valid integer.")
