# Write your program here

initial_organisms = float(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the rate of growth [a real number > 1]: "))
hours_to_growth = float(input("Enter the number of hours to achieve the rate of growth: "))
total_hours = float(input("Enter the total hours of growth: "))

growth_time = int(total_hours / hours_to_growth)
total_population = 0
time = 0

for time in range(growth_time):
    total_population = initial_organisms * growth_rate
    initial_organisms = total_population
    time += 1

print("The total population is", int(total_population))