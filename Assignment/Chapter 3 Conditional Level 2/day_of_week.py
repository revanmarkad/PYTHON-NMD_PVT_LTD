# Program to output the corresponding day of the week based on an integer

try:
    # Input the integer (1-7)
    day_number = int(input("Enter an integer between 1 and 7: "))

    # Mapping integers to days of the week
    if day_number == 1:
        print("Sunday")
    elif day_number == 2:
        print("Monday")
    elif day_number == 3:
        print("Tuesday")
    elif day_number == 4:
        print("Wednesday")
    elif day_number == 5:
        print("Thursday")
    elif day_number == 6:
        print("Friday")
    elif day_number == 7:
        print("Saturday")
    else:
        print("Invalid input! Please enter an integer between 1 and 7.")

except ValueError:
    print("Invalid input. Please enter a valid integer between 1 and 7.")
