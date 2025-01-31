import math

# Program to determine the type of roots of a quadratic equation

try:
    # Accept coefficients of the quadratic equation
    a = float(input("Enter the coefficient a (for ax^2): "))
    b = float(input("Enter the coefficient b (for bx): "))
    c = float(input("Enter the coefficient c (for c): "))

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Determine the type of roots based on the discriminant
    if discriminant > 0:
        print("The roots are real and distinct.")
    elif discriminant == 0:
        print("The roots are real and equal.")
    else:
        print("The roots are complex.")

except ValueError:
    print("Invalid input. Please enter valid numeric values for the coefficients.")
