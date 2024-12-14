import math

def newton(num):
    tolerance = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + num / estimate) / 2
        difference = abs(num - estimate ** 2)
        if difference <= tolerance:
            return estimate

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