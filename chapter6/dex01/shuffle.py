import random
def shuffleString(theString):
    stringList = list(theString)
    random.shuffle(stringList)
    newString = "".join(stringList)
    print(newString)
shuffleString("Apples are red")