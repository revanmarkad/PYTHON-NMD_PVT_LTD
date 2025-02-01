
# 4. Print multiplication table of a number
def multiplication_table(x):
    print(f"Multiplication table of {x}:")
    for i in range(1, 11):
        print(f"{x} × {i} = {x * i}")

x = int(input("Enter a number to print its multiplication table: "))
multiplication_table(x)