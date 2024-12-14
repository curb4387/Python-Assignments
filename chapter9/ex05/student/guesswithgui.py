from breezypythongui import EasyFrame
import random

class guess(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Guessing Game", width = 310, height = 200)
        # Declare variables used in calculations
        self.smaller = 1
        self.larger = 100
        self.guessCount = 1
        self.guess = random.randint(self.smaller, self.larger)
        # Introduction to the game
        self.greeting = f"Welcome to the Guessing Game!\nChoose a number from {self.smaller} to {self.larger}.\nClick 'Ready' to start the game."
        self.rules = "Give me a hint by clicking a button below."
        self.gameText = self.addLabel(text = self.greeting, row = 1, column = 0, columnspan = 3, sticky = "NSEW")
        self.computerGuess = self.addLabel(text = "", row = 2, column = 0, columnspan = 3, sticky = "NSEW")
        # Hint buttons are disabled before the game starts
        self.leftButton = self.addButton(text = "Too large", row = 3, column = 0, command = self.tooLarge, state = "disabled")
        self.midButton = self.addButton(text = "Too small", row = 3, column = 1, command = self.tooSmall, state = "disabled")
        self.rightButton = self.addButton(text = " Correct ", row = 3, column = 2, command = self.correctGuess, state = "disabled")
        self.newGameButton = self.addButton(text = "New Game", row = 4, column = 1, command = self.playGame)

    def playGame(self):
        self.gameText["text"] = self.rules
        self.computerGuess["text"] = f"Is your number {self.guess}?"
        # Hint buttons are enabled once the game starts
        self.leftButton["state"] = "normal"
        self.midButton["state"] = "normal"
        self.rightButton["state"] = "normal"
        self.newGameButton["state"] = "disabled"

    def newGame(self):
        self.smaller = 1
        self.larger = 100
        self.guessCount = 1
        self.guess = random.randint(self.smaller, self.larger)
        self.gameText["text"] = self.greeting
        self.computerGuess["text"] = ""
        self.leftButton["state"] = "disabled"
        self.midButton["state"] = "disabled"
        self.rightButton["state"] = "disabled"
        self.newGameButton["command"] = self.playGame

    def tooLarge(self):
        if self.guess == 1:
            self.computerGuess["text"] = f"I'm out of guesses and you cheated!\nClick New Game to try again."
        if self.larger - 1 == self.smaller:
            self.computerGuess["text"] = f"I'm out of guesses and you cheated!\nClick New Game to try again."
        self.guessCount += 1
        self.larger = self.guess - 1
        self.guess = random.randint(self.smaller, self.larger)
        self.computerGuess["text"] = f"Is your number {self.guess}?"

    def tooSmall(self):
        if self.guess == 100:
            self.computerGuess["text"] = f"I'm out of guesses and you cheated!\nClick New Game to try again."
        if self.smaller + 1 == self.larger:
            self.computerGuess["text"] = f"I'm out of guesses and you cheated!\nClick New Game to try again."
        self.guessCount += 1
        self.smaller = self.guess + 1
        self.guess = random.randint(self.smaller, self.larger)
        self.computerGuess["text"] = f"Is your number {self.guess}?"

    def correctGuess(self):
        self.computerGuess["text"] = ""
        self.computerGuess["text"] = f"Hooray! I got it in {self.guessCount} tries!\nClick New Game to play again."
        self.leftButton["state"] = "disabled"
        self.midButton["state"] = "disabled"
        self.rightButton["state"] = "disabled"
        self.newGameButton["state"] = "normal"
        self.newGameButton["command"] = self.newGame

def main():
    guess()

if __name__ == "__main__":
    main()

input("pythong")