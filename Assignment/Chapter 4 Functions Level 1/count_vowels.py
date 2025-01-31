# Write a function count_vowels(text) that takes a string as 
# input and returns the count of vowels (a, e, i, o, u) in it.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# Example usage
input_text = input("Enter a string: ")
vowel_count = count_vowels(input_text)
print(f"The number of vowels in the given string is {vowel_count}")

