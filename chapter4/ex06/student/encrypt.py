text = input("Enter a message: ")

code = ""
for letter in text:
    ordValue = ord(letter) + 1
    bstring = "" # converts each letter into binary
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        bstring = str(remainder) + bstring
    if len(bstring) > 1: # shift to left when there's more than 1 character
        bstring = bstring[1:] + bstring[0]
    code = code + bstring + " "

print("The encrypted binary string is: ", code)