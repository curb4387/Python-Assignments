# Write your program here
# This program calculates an employee's weekly pay

hourly_wage = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter total regular hours: "))
overtime_hours = float(input("Enter total overtime hours: "))

regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * (hourly_wage * 1.5)
total_weekly_pay = regular_pay + overtime_pay

print(f"The total weekly pay is ${total_weekly_pay:.2f}")