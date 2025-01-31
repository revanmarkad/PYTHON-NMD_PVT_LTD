# Program to check if three sides form a valid triangle

try:
     
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))

    # Check if the sides satisfy the triangle inequality theorem
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print("The sides form a valid triangle.")
    else:
        print("The sides do not form a valid triangle.")

except ValueError:
    print("Invalid input. Please enter valid numeric values for the sides.")
