# 7. Convert a number to binary
def number_to_binary(n):
    return bin(n)[2:]

n = int(input("Enter a number to convert to binary: "))
print(f"The binary representation of {n} is {number_to_binary(n)}")