
# Function to convert a sentence to title case (first letter of each word capitalized)
def title_case(sentence):
    """
    title_case(sentence)
    
    This function takes a sentence and returns it in title case (capitalizes the first letter of each word).
    It works by:
    1. Splitting the sentence into individual words.
    2. Capitalizing each word.
    3. Joining the words back into a sentence.
    """
    return ' '.join([word.capitalize() for word in sentence.split()])
