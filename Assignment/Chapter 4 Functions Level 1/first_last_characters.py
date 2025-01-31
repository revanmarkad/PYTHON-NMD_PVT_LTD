# Function to return the first and last character of a string
def first_last(text):
    if len(text) == 0:
        return ("", "")  # Return empty tuple if the string is empty
    return (text[0], text[-1])

# Example usage
input_text = input("Enter a string: ")
result = first_last(input_text)
print(f"The first and last characters are: {result}")
