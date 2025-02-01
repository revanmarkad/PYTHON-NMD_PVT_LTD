
# 7. Find the largest number in a list
def find_largest_number(numbers):
    return max(numbers)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(f"The largest number in the list is {find_largest_number(numbers)}")
