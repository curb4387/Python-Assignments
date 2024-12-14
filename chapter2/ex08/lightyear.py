# Write your program here
# This program calculates the distance light travels in a given number of years

years = int(input("Enter number of years: "))

speed_per_second = 3 * (10**8)
seconds_per_year = 365 * 24 * 60 * 60
distance_traveled = speed_per_second * seconds_per_year * years

print("The distance light travels in", years, "years is", distance_traveled, "meters")