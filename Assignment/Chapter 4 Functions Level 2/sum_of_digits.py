def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total


print(sum_of_digits(123))  # Output: 6
print(sum_of_digits(-456)) # Output: 15
