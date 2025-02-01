
# 9. Count the number of words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = input("Enter a sentence: ")
print(f"The number of words in the sentence is {count_words(sentence)}")
