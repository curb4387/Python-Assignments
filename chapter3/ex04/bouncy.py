# Write your program here
# This program calculates bounciness

height_dropped = float(input("Enter height the ball is dropped at: "))
bounce_index = float(input("Enter the bounciness index of the ball: "))
bounce_number = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

total_distance = height_dropped
current_height = height_dropped

for bounce in range(bounce_number):
    bounce_height = current_height * bounce_index
    total_distance += 2 * bounce_height
    current_height = bounce_height
total_distance = total_distance - bounce_height
print("Total distance traveled is:", total_distance, "units.")