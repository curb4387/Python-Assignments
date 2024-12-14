"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""
import random

def getWords(fileName):
    file = open(fileName, 'r')
    contents = file.read()
    wordList = contents.split()
    wordTuple = tuple(wordList)
    file.close()
    return wordTuple

articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")
conjunctions = getWords("conjunctions.txt")
adjectives = getWords("adjectives.txt")

def sentence():
    """Builds and returns a sentence."""
    phrase = nounPhrase() + " " + verbPhrase()
    prob = random.randint(1, 4)
    if prob == 1:
        return phrase + " " + random.choice(conjunctions) + " " + phrase
    else:
        return phrase

def nounPhrase():
    """Builds and returns a noun phrase."""
    nounPhrase = random.choice(articles) + " " + random.choice(nouns)
    prob = random.randint(1, 4)
    if prob == 1:
        return random.choice(articles) + " " + random.choice(adjectives) + \
               " " + random.choice(nouns)
    else:
        return nounPhrase

def verbPhrase():
    """Builds and returns a verb phrase."""
    verbPhrase = random.choice(verbs) + " " + nounPhrase()
    prob = random.randint(1, 4)
    if prob == 1:
        return verbPhrase + " " + prepositionalPhrase()
    else:
        return verbPhrase

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()
