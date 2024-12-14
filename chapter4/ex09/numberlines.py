# Originally coded:
"""
inputFile = input("Enter the name of the input file: ")
outputFile = input("Enter the name of the output file: ")

initialFile = open(inputFile, 'r')
newFile = open(outputFile, 'w')

count = 1
for line in initialFile:
    formatted_line = "%4s" % str(count) + ">" + " " + line
    newFile.write(formatted_line)
    count += 1

initialFile.close()
newFile.close()
"""
# Coded in class:
file1 = input("Enter the name of file 1: ")
file2 = input("Enter the name of file 2: ")

openfile1 = open(file1, "r")
openfile2 = open(file2, "w")

linenum = 0
for line in openfile1:
    linenum = linenum + 1
    openfile2.write("%4d> %s" % (linenum, line))

openfile1.close()
openfile2.close()