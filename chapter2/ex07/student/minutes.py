# Write your program here
# This program calculates the number of minutes in the number of years

years = int(input("Enter number of years: "))
one_day = 24 * 60
one_year = int(one_day) * 365

minutes = int(one_year) * int(years)

print("The number of minutes in", years, "years is", minutes)