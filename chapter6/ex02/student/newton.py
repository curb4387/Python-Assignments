import math
TOLERANCE = 0.000001

def improveEstimate(num, estimate):
    estimate = (estimate + num / estimate) / 2
    return estimate

def limitReached(num, estimate):
    difference = abs(num - estimate ** 2)
    if difference <= TOLERANCE:
        limit = True
    else:
        limit = False
    return limit

def newton(num):
    estimate = 1.0
    limit = False
    while True:
        estimate = improveEstimate(num, estimate)
        if True == limitReached(num, estimate):
            return estimate

def main():36
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