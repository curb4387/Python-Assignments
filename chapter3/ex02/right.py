# Write your program here
# This program takes 3 sides of a triangle and determines if it is a right triangle

side_one = int(input("Enter the first side: "))
side_two = int(input("Enter the second side: "))
side_three = int(input("Enter the third side: "))

pythagorean = (side_one**2) + (side_two**2)
if pythagorean == side_three**2:
    print("The triangle is a right triangle!")
else:
    print("The triangle is not a right triangle.")