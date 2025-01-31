# Program to calculate BMI and determine the health category

try:
 
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine health category based on BMI
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

     
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Health Category: {category}")

except ValueError:
    print("Invalid input. Please enter valid numeric values for height and weight.")
