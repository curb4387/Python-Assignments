inFile = input("Enter the input file: ")
outFile = input("Enter the output file: ")
distance = int(input("Enter the distance value: "))

inputFile = open(inFile, 'r')
contents = inputFile.read()

outputFile = open(outFile, 'w')
code = ""
for ch in contents:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue = 127 - (distance - (1 - ordValue))
    code = code + chr(cipherValue)

outputFile.write(code)
outputFile.close()
inputFile.close()