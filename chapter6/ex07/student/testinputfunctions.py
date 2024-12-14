# pre-coded inputInt function
def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    while True:
        numString = input(prompt)
        hasPoint = False
        isFloat = True
        for ch in numString:
            if ch == '.' and hasPoint:
                print("Error: the input cannot have more than one '.'")
                isFloat = False
                break
            elif ch == '.' and not hasPoint:
                hasPoint = True
            elif not ch.isdigit():
                print("Error: the input must consist only of digits")
                isFloat = False
                break
        if isFloat:
            return float(numString)
        # decimalPoints = numString.count('.')
        # if decimalPoints > 1:
        #     print("Error: the input cannot have more than one '.'")
        # else:
        #     digitCheck = numString.replace('.', '', 1)
        #     if digitCheck.isdigit():
        #         return float(numString)
        #     else:
        #         print("Error: the input must consist only of digits")

def main():
    n = inputFloat("Please enter an integer or a float: ")
    print(n)

if __name__ == "__main__":
    main()