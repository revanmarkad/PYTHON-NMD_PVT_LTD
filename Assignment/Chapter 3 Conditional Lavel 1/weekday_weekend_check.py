# Program to determine if a day is a weekend or a weekday

try:
     
    day = int(input("Enter a day number (1 for Monday, 7 for Sunday): "))

    # Check if the input is within the valid range
    if 1 <= day <= 7:
        # Determine if the day is a weekday or weekend
        if day == 6 or day == 7:
            print("It's a weekend!")
        else:
            print("It's a weekday.")
    else:
        print("Invalid input. Please enter a number between 1 and 7.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
