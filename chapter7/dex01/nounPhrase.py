import random
articles = ["the", "a", "one", "some", "any"]
adjectives = ["big", "small", "blue", "green", "yellow", "red", "purple", "orange", "brown", "black", "white"]
nouns = ["apple", "peach", "banana", "pear", "orange", "grape", "strawberry", "blueberry", "raspberry", "cherry", "watermelon", "cantaloupe", "honeydew"]
#nounphrase = article [adjectivephrase] noun
def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + \
        adjectivePhrase() + " " + random.choice(nouns)

#adjectivephrase = adjective [adjectivephrase]
def adjectivePhrase():
    """Builds and returns an adjective phrase."""
    choice = random.randint(1, 2)
    if choice == 1:
        adj = random.choice(adjectives) + " " + adjectivePhrase()
    else:
        adj = random.choice(adjectives)
    return adj

print(nounPhrase())