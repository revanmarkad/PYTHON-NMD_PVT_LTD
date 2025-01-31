# Write a function repeat_message(message, times) that takes a message string and a number of times to repeat it, and prints the message that many times.

 
def repeat_message(message, times):
    for _ in range(times):
        print(message)

# Example usage
msg = input("Enter the message: ")
num = int(input("Enter the number of times to repeat: "))

repeat_message(msg, num)
