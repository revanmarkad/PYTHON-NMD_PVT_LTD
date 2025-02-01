# Function to find the second largest number in a list
def second_largest(numbers):
    """
    second_largest(numbers)
    
    This function takes a list of numbers and returns the second largest number.
    It works by:
    1. Removing duplicates using `set()` to ensure we only have unique numbers.
    2. Sorting the list in ascending order.
    3. Returning the second to last element (second largest).
    """
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort()  # Sort the list
    return unique_numbers[-2]  # Return the second to last element (second largest)

