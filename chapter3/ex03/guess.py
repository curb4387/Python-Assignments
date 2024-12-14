# Write your program here
# TKTK: Add started code here.
import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

max_guess = int(math.log(larger - smaller + 1, 2))
print("The maximum number of guesses the computer can make is", max_guess)
count = 0

while count < max_guess:
    guess = random.randint(smaller, larger)
    print("Your number is", guess)
    user_hint = input("Enter =, <, or >: ")
    count += 1
    if user_hint == "<":
        larger = guess - 1
        print(smaller, larger)
    elif user_hint == ">":
        smaller = guess + 1
        print(smaller, larger)
    elif user_hint == "=":
        print("Hooray, I've got it in", count, "tries!")
        break
    else:
        print("Invalid. Please try again.")
        count -= 1
    if smaller > larger:
        print("I'm out of guesses, and you cheated!")