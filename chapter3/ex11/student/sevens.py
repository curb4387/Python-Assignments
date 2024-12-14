# Write your program here
import random

money_bet = int(input("How many dollars do you have?: "))
initial_bet = money_bet
max_money = initial_bet
count = 0
current_count = 0
while money_bet > 0:
    dice_1 = random.randint(1, 7)
    dice_2 = random.randint(1, 7)
    dice_sum = dice_1 + dice_2
    count += 1
    if dice_sum != 7:
        money_bet -= 1
    else:
        money_bet += 4
    if money_bet > initial_bet:
        max_money = money_bet
        current_count = count

print("You are broke after", count, "rolls.")
print("You should have quit after", current_count, "rolls when you had", "$%-2d" % max_money)