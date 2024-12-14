# Write your program here
num_sum = 0.0
counter = 0
while True:
    user_number = input("Enter a number or press Enter to quit: ")
    if user_number == "":
        break
    number = float(user_number)
    num_sum += number
    counter += 1
average = num_sum / counter
print("The sum is", num_sum)
print("The average is", average)