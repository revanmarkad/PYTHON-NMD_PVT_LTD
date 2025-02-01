
# Create a function is_prime(n) that takes an integer and returns True if it is a prime number, otherwise False.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
