fileName = input("Enter filename: ")
file = open(fileName, 'r')
contents = file.read()
fileLines = contents.split('\n')
lineNum = len(fileLines)
print("There are", lineNum, "lines in the file.")

userNum = input(f"Enter a line number from 1 to {lineNum}, or 0 to quit: ")
while True:
    if int(userNum) > int(lineNum):
        print("Error: enter a line number in range, or 0 to quit.")
    elif userNum == '0':
        break
    else:
        userNum = int(userNum) - 1
        print(fileLines[userNum])
    userNum = input(f"Enter a line number from 1 to {lineNum}, or 0 to quit: ")

file.close()