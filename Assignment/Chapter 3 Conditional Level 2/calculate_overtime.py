# Simple Program to calculate overtime pay

# Input the hourly rate and hours worked
hourly_rate = float(input("Enter hourly rate: $"))
hours_worked = float(input("Enter hours worked: "))

# If hours worked are more than 40, calculate overtime
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    total_pay = regular_pay + overtime_pay
else:
    regular_pay = hours_worked * hourly_rate
    total_pay = regular_pay

# Print the total pay
print(f"Total pay: ${total_pay:.2f}")
