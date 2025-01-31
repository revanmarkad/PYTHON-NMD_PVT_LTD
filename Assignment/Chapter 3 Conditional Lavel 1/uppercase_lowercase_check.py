# Program to check if a character is uppercase or lowercase

try:
    
    char = input("Enter a single character: ")

    # Validate input length
    if len(char) != 1 or not char.isalpha():
        print("Invalid input. Please enter a single alphabetic character.")
    else:
        # Check if the character is uppercase or lowercase
        if char.isupper():
            print(f"The character '{char}' is uppercase.")
        else:
            print(f"The character '{char}' is lowercase.")

except ValueError:
    print("Invalid input. Please enter a valid character.")
