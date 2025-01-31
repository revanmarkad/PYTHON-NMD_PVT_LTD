# Program to determine if a triangle is equilateral, isosceles, or scalene based on its angles

try:
    # Take input for the three angles of the triangle
    angle1 = float(input("Enter the first angle: "))
    angle2 = float(input("Enter the second angle: "))
    angle3 = float(input("Enter the third angle: "))

    # Check if the angles form a valid triangle (sum of angles must be 180)
    if angle1 + angle2 + angle3 == 180:
        # Determine the type of triangle based on the angles
        if angle1 == angle2 == angle3:
            print("The triangle is equilateral.")
        elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")
    else:
        print("The angles do not form a valid triangle. The sum of the angles must be 180 degrees.")

except ValueError:
    print("Invalid input. Please enter valid numeric values for the angles.")
