
# 8. Print a pyramid pattern of stars
def print_pyramid_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

n = int(input("Enter the number of rows for the pyramid pattern: "))
print_pyramid_pattern(n)
