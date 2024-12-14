file = input("Enter file name: ")
file = open(file, 'r')
fileContents = file.read()
file.close()

fileList = fileContents.split(" ")
newWords = []
for word in fileList:
    if word not in newWords:
        newWords.append(word)
newWords.sort()
newString = " ".join(newWords)
print(newString)