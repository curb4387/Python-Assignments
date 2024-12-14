# Write your program here
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

while smaller > 0:
    remainder = larger % smaller
    larger = smaller
    smaller = remainder
greatest_common_divisor = larger

print("The greatest common divisor is", greatest_common_divisor)