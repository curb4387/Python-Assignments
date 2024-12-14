# Compute mean, mode, and median of any given set of numbers.

def mean(numberSet):
    total = 0
    for num in numberSet:
        total += num
    mean = total / (len(numberSet))
    if numberSet == "":
        mean = 0
    return mean

def mode(numberSet):
    numDictionary = {}
    for num in numberSet:
        number = numDictionary.get(num, None)
        if number == None:
            numDictionary[num] = 1
        else:
            numDictionary[num] = number + 1
    theMax = max(numDictionary.values())
    for num in numDictionary:
        if numDictionary[num] == theMax:
            mode = num
    if numberSet == "":
        mode = 0
    return mode

def median(numberSet):
    numberSet.sort()
    median = len(numberSet) // 2
    if len(numberSet) % 2 == 1:
        median = numberSet[median]
    else:
        median = (numberSet[median] + numberSet[median - 1]) / 2
    if numberSet == "":
        median = 0
    return median

def main():
    numberSet = [44,23,77,23]
    print("The mean is", mean(numberSet))
    print("The mode is", mode(numberSet))
    print("The median is", median(numberSet))

if __name__ == "__main__":
    main()
