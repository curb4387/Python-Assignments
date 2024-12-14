# Write your program here
# This program inputs 3 sides of a triangle and determines if it is an equilateral triangle

first_side = input("Enter the first side: ")
second_side = input("Enter the second side: ")
third_side = input("Enter the third side: ")

if first_side == second_side and first_side == third_side:
    print("The triangle is equilateral!")
else:
    print("The triangle is not equilateral.")