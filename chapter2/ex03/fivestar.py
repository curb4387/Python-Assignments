# Write your program here
# This program calculates the total cost of video rentals
new = int(input("Enter amount of new videos: "))
old = int(input("Enter amount of old videos: "))
newCost = float(3.00)
oldCost = float(2.00)

new = new * newCost
old = old * oldCost
totalCost = new + old

print(f"\nTotal rental cost: ${totalCost:.2f}")