# Program to check if a student passes based on their score

try:
    
    score = float(input("Enter the student's score (0 to 100): "))

    # Check if the score is within the valid range
    if 0 <= score <= 100:
        # Determine if the student passes or fails
        if score >= 40:
            print(f"The student passes with a score of {score}.")
        else:
            print(f"The student fails with a score of {score}.")
    else:
        print("Invalid score. Please enter a value between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter a valid numeric score.")
