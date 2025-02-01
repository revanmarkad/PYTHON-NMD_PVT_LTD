# Remove All Vowels


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in s if char not in vowels)
    print(result)

remove_vowels("Hello World")
