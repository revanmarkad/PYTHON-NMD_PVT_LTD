# : Create a program to check if a person is eligible to vote. (Age >= 18)


try:
    age = int(input("Enter your age: "))
    
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

except ValueError:
    print("Please provide a valid number for age.")
