

# Function to find the Least Common Multiple (LCM) of two numbers
import math

def find_lcm(a, b):
    """
    find_lcm(a, b)
    
    This function calculates the Least Common Multiple (LCM) of two numbers.
    It works by:
    1. Using the formula: LCM(a, b) = |a * b| / GCD(a, b), where GCD is the Greatest Common Divisor.
    2. Using the `math.gcd` function to find the GCD.
    """
    return abs(a * b) // math.gcd(a, b)


