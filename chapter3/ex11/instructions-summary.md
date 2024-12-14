## Your Tasks

In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7, the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so on. A little mathematical analysis reveals that there are not enough ways to win to make the game worthwhile; however, because many people’s eyes glaze over at the first mention of mathematics, your challenge is to write a program in the file **sevens.py** that demonstrates the futility of playing the game.

Your program should take as input the amount of money that the player wants to put into the pot, and play the game until the pot is empty. At that point, the program should print the number of rolls it took to break the player, as well as maximum amount of money in the pot. (LO: 3.3, 3.4)

## Instructions

**Task 1**: Write the **sevens.py** program that plays the game of sevens until the pot is empty and prints the number of rolls it took to break the player.

An example of the program is shown below:

```txt
How many dollars do you have? 50

You are broke after 220 rolls.
You should have quit after 6 rolls when you had $59.
```