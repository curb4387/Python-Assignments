articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
adjectives = ("RED")
conjunctions = ("AND")

def sentence(words):
    if conjunctions in words:
        return nounPhrase(words) and verbPhrase(words) \
            and sentence(words)
    else:
        return nounPhrase(words) and verbPhrase(words)

def nounPhrase(words):
    if len(words) < 2:
        return False
    else:
        article = words.pop(0)
        if words[0] in adjectives:
            adjective = words.pop(0)
            noun = words.pop(0)
            if len(words) > 0:
                if words[0] in conjunctions:
                    conjunction = words.pop(0)
                    return article in articles and adjective in adjectives  \
                        and noun in nouns and conjunction in conjunctions
            return article in articles and adjective in adjectives  \
                and noun in nouns
        else:
            noun = words.pop(0)
            if len(words) > 0:
                if words[0] in conjunctions:
                    conjunction = words.pop(0)
                    return article in articles and noun in nouns  \
                        and conjunction in conjunctions
            return article in articles and noun in nouns
    
def verbPhrase(words):
    if len(words) == 0:
        return False
    else:
        verb = words.pop(0)
        if prepositions in words:
            return verb in verbs and nounPhrase(words) and \
                prepositionalPhrase(words)
        else:
            return verb in verbs and nounPhrase(words)

def prepositionalPhrase(words):
    if len(words) == 0:
        return False
    else:
        preposition = words.pop(0)
        return preposition in prepositions and nounPhrase(words)
    
def main():
    while True:
        userInput = input("Enter a sentence or press return to quit: ")
        if userInput == "":
            return
        else:
            words = userInput.upper().split()
            if sentence(words):
                print("Ok, grammatically correct")
            else:
                print("Not ok, grammatically incorrect")

if __name__ == "__main__":
    main()