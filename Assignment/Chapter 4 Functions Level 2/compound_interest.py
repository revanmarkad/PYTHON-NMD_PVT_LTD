# Function to calculate compound interest
def compound_interest(P, R, T):
    """
    compound_interest(P, R, T)
    
    This function calculates compound interest using the formula:
    A = P * (1 + R / 100) ^ T
    Where:
    P is the principal amount,
    R is the rate of interest per year,
    T is the time in years.
    
    It works by:
    1. Calculating the final amount (A).
    2. Subtracting the principal (P) to return only the interest earned.
    """
    A = P * (1 + R / 100) ** T
    return A - P  # Return the interest earned (A - principal)
