
# Write a function find_gcd(a, b) that takes two numbers and returns their Greatest Common Divisor (GCD).


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
