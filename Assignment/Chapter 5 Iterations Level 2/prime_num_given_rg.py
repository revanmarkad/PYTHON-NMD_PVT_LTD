
# 5. Print prime numbers in a given range
def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print()

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print_primes_in_range(start, end)
