
# 2. Print the Fibonacci sequence up to N terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci(n)
