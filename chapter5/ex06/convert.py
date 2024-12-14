hexTable = {
    "0": 0, "1": 1, "2": 2, "3": 3,
    "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "A": 10, "B": 11,
    "C": 12, "D": 13, "E": 14, "F": 15,
}

def decimalToRep(numString, base):
    newNum = ""
    if base > 10:
        for digit in numString:
            digit = hexTable[digit]
    numString = int(numString)
    while numString > 0:
        remainder = numString % base
        numString = numString // base
        newNum = str(remainder) + newNum
    return newNum

def main():
    numString = "15"
    base = 11
    print(decimalToRep(numString, base))
    numString = "110"
    base = 5
    print(decimalToRep(numString, base))
    numString = "13848"
    base = 7
    print(decimalToRep(numString, base))
    numString = "21"
    base = 2
    print(decimalToRep(numString, base))
    numString = "43127240"
    base = 8
    print(decimalToRep(numString, base))

if __name__ == "__main__":
    main()