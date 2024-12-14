# Write your program here
decimal = int(input("Enter a decimal integer: "))

if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Octal")
    octal_num = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octal_num = str(remainder) + octal_num
        print("%5d%8d%12s" % (decimal, remainder, octal_num))

print("The binary representation is", octal_num)