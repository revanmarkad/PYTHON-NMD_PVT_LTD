# Find First Repeated Character

def first_repeated_character(s):
    seen = set()
    for char in s:
        if char in seen:
            print(char)
            return
        seen.add(char)
    print("No repeated character found")

first_repeated_character("abca")
