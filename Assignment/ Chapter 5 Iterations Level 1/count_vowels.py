
# 9. Count the number of vowels in a string
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in sentence if char in vowels)
    print(f"The number of vowels in the input text is {count}.")

sentence = input("Enter a string to count vowels: ")
count_vowels(sentence)
