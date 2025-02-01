# Create a function is_palindrome(text) that checks if a given 
#  string is a palindrome (reads the same forward and backward).



def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniform comparison
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]



print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
