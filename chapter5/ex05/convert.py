hexTable = {
    "0": 0, "1": 1, "2": 2, "3": 3,
    "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "A": 10, "B": 11,
    "C": 12, "D": 13, "E": 14, "F": 15,
}

def repToDecimal(numString, base):
    decimal = 0
    exponent = len(numString) - 1
    numString = numString.upper()
    for digit in numString:        
        decimal += hexTable[digit] * base ** exponent
        exponent -= 1
    return decimal

def main():
    numString = "35A"
    base = 5
    print(repToDecimal(numString, base))
    numString = "55239"
    base = 7
    print(repToDecimal(numString, base))
    numString = "00010101"
    base = 2
    print(repToDecimal(numString, base))
    numString = "243B87E90"
    base = 8
    print(repToDecimal(numString, base))

if __name__ == "__main__":
    main()