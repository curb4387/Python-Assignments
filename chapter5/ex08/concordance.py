filename = input("Enter filename name: ")

filename = open(filename, 'r')
# fileContents = filename.read()
# filename.close()
# fileList = fileContents.split(" ")
# fileList.sort()
uniqueWords = {}

# Start with the line, then with the words in the line
# Do this in case we have files with multiple lines
for line in filename:
    words = line.split()
    for word in words:
        freq = uniqueWords.get(word, None)
        if freq == None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = freq + 1

words = list(uniqueWords.keys())
words.sort()
for word in words:
    print(word, uniqueWords[word])

# count = 0
# for word in fileList:
#     if word not in newWords:
#         count = 1
#         newWords[word] = count
#     elif word in newWords:
#         count += 1
#         newWords[word] = count
# for word in newWords:
#     print(word, newWords[word])