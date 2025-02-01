# 5. Count the number of digits in an integer
def count_digits(n):
    digit_count = len(str(abs(n)))
    print(f"The number {n} has {digit_count} digits.")

n = int(input("Enter an integer to count its digits: "))
count_digits(n)