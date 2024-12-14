# Write your program here
octal_num = input("Enter an octal integer: ")
decimal = 0
exponent = len(octal_num) - 1

for digit in octal_num:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1

print("The integer value is", decimal)