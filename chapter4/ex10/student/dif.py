file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

inputFile1 = open(file1, 'r')
inputFile2 = open(file2, 'r')

while True:
    line1 = inputFile1.readline()
    line2 = inputFile2.readline()
    if line1 == "" and line2 == "":
        print("Yes")
        break
    elif line1 != line2:
        print("No")
        print(line1)
        print(line2)
        break

inputFile1.close()
inputFile2.close()