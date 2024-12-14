import math

# def newton(num, estimate = 1.0):
#     tolerance = 0.000001
#     difference = abs(num - estimate ** 2)
#     if difference <= tolerance:
#         return estimate
#     estimate = (estimate + num / estimate) / 2
#     ourEstimate = newton(num, estimate)
#     return ourEstimate

def newton(num, estimate = 1.0):
    tolerance = 0.000001
    difference = limitReached(num, estimate)
    if difference <= tolerance:
        return estimate
    estimate = improveEstimate(num, estimate)
    ourEstimate = newton(num, estimate)
    return ourEstimate

def limitReached(num, estimate):
    return abs(num - estimate ** 2)

def improveEstimate(num, estimate):
    return (estimate + num / estimate) / 2

def main():
    while True:
        x = input("Enter a positive number or enter to exit: ")
        if not x:
            break
        else:
            x = float(x)
        print("The program's estimate: ", newton(x))
        print("Python's estimate: ", math.sqrt(x))
        
if __name__ == "__main__":
    main()