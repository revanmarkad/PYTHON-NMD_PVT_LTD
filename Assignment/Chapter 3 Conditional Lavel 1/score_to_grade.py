# Program to determine the grade based on score

try:
    
    score = float(input("Enter a score between 0.0 and 1.0: "))

    # Check for valid score range
    if 0.0 <= score <= 1.0:
        # Determine the grade based on the score
        if score >= 0.9:
            print("Grade: A")
        elif score >= 0.8:
            print("Grade: B")
        elif score >= 0.7:
            print("Grade: C")
        elif score >= 0.6:
            print("Grade: D")
        else:
            print("Grade: F")
    else:
        print("Invalid score. Please enter a score between 0.0 and 1.0.")
    
except ValueError:
    print("Invalid input. Please enter a numeric value.")
