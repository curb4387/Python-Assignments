# Testing getWords()
fileName = 'nouns.txt'
file = open(fileName, 'r')
contents = file.read()
wordList = contents.split()
wordTuple = tuple(wordList)
print(wordTuple)