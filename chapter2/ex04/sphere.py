# Write your program here
# This program calculates the diameter, circumference, surface area, and volume of a sphere
from math import pi
radius = float(input("Enter the radius: "))

diameter = radius * 2
circumference = 2 * (pi * radius)
surface_area = 4 * (pi * (radius ** 2))
volume = (4 / 3) * (pi * (radius ** 3))

print("The diameter is", diameter)
print("The circumference is", circumference)
print("The surface area is", surface_area)
print("The volume is", volume)