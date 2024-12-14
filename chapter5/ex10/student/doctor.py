"""
Program: doctor.py
Author: Ken
Conducts an interactive session of nondirective psychotherapy.
"""

import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please coninue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ",
              "Earlier you said that ")

replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours",
                "you":"I"} 

inputList = []

def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    if len(inputList) > 4:
        qualifier = random.choice(qualifiers)
        if qualifier == qualifiers[3]:
            sentence = random.choice(inputList)
            return qualifier + changePerson(sentence)
    else:
        qualifier = random.choice(qualifiers[0:3])
    if probability == 1:
        return random.choice(hedges)
    else:
        return qualifier + changePerson(sentence)

def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        if word == "are":
            replyWords.append("am")
        elif word == "am":
            replyWords.append("are")
        else:
            replyWords.append(replacements.get(word, word))
    return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        inputList.append(sentence)
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()

