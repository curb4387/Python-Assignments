# Write your program here
def leibniz_pi(iterations):
    count = 0
    for number in range(iterations):
        leibniz = (-1) ** number / (2 * number + 1)
        count += leibniz
    return (count * 4)
iterations = int(input("Enter the number of iterations: "))
pi_approximation = leibniz_pi(iterations)
print("The approximation of pi is", pi_approximation)
