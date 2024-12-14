# Originally coded:
salary = float(input("Enter the starting salary: $"))
percent_increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: " ))
percent_increase = percent_increase / 100

print("")
print("Year", "%8s" % "Salary")
print("-------------")
for one_year in range(1, years + 1):
    print("%2s" % one_year, "%12s" % f"${salary:.2f}")
    salary += salary * percent_increase

"""
# Coded in class:
salary = float(input("Enter the starting salary: $"))
percent_increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: " ))
multiplier = 1 + (percent_increase / 100)
nextSalary = salary # use nextSalary to mutate so we can go back and refer to the original salary

print("Year     Salary\n---------------")

for year in range(1, years + 1):
    
    year = year + 1
    salary = salary + multiplier
    print("%2s" % year, "%12s" % f"${nextSalary:.2f}")
    nextSalary = nextSalary * multiplier
"""