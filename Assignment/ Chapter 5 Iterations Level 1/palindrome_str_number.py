
# 6. Check if a string or number is a palindrome
def is_palindrome(value):
    value_str = str(value)
    return value_str == value_str[::-1]

value = input("Enter a string or number to check for palindrome: ")
if is_palindrome(value):
    print(f"{value} is a palindrome.")
else:
    print(f"{value} is not a palindrome.")
