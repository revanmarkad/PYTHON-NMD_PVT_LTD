def count_vowels_consonants(s):
    vowels = "aeiou"
    s = s.lower()
    vowels_count = sum(1 for char in s if char in vowels)
    consonants_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")

count_vowels_consonants("Hello")
