"""
# Originally coded:
# Input bit string and split each string into a list
bit_string = input("Enter the bit string to decrpyt: ")
bit_strings = bit_string.split()

# Shift each string to the right
shifted_strings = []
for string in bit_strings:
    for bit in range(0, len(string)):
        shift_right = ""
        shift_right = string[-1]
        shift_right = shift_right + string[:-1]
    shifted_strings.append(shift_right)

# Convert the shifted string values in the list into integers
# Then convert each binary number into decimal numbers
sub = 0
shifted_string = shifted_strings[sub]
exponent = len(str(shifted_string)) - 1
for bit in range(0, len(shifted_strings)):
    shifted_strings[bit] = int(shifted_strings[bit])

sub = 0
decimal_strings = []
while sub < len(shifted_strings):
    decimal_string = shifted_strings[sub]
    decimal = 0
    exponent = len(str(shifted_string)) - 1
    for digit in str(decimal_string):
        decimal += int(digit) * 2 ** exponent
        exponent = exponent - 1
    decimal_strings.append(decimal)
    sub += 1

# Convert the decimal/ASCII value into its equivalent character
decrypted_text = ""
distance = 1
for decimal in decimal_strings:
    decimal = decimal - 1
    text = chr(decimal)
    decrypted_text = decrypted_text + text
print(decrypted_text)
"""
# Coded in class:
"""
# code from exercise 4-6
text = input("Enter a message: ")
code = ""
for letter in text:
    ordValue = ord(letter) + 1
    # converts each letter into binary
    bstring = ""
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        bstring = str(remainder) + bstring
    # shift to left when there's more than 1 character
    if len(bstring) > 1:
        bstring = bstring[1:] + bstring[0]
    # add encrypted character to code string
    code = code + bstring + " "
print("The encrypted binary string is: ", code)
"""
# using the output from the above code that encrypts a string
# hi there you weirdo = 1010011 1010101 000011 1101011 1010011 1001101 1100111 1001101 000011 1110101 1100001 1101101 000011 1110001 1001101 1010101 1100111 1001011 1100001
# what is going on = 1110001 1010011 1000101 1101011 000011 1010101 1101001 000011 1010001 1100001 1010101 1011111 1010001 000011 1100001 1011111
code = input("Enter the coded text: ")
wordList = code.split()
plainText = ""
for word in wordList:
    word = word[-1] + word[:-1]
    num = 0
    exponent = len(word) - 1
    for digit in word:
        print(digit, num)
        num = num + int(digit) * 2 ** exponent
        exponent = exponent - 1
    num = num - 1
    plainText = plainText + chr(num)
print(plainText)