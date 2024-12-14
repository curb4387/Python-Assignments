from functools import reduce

def add(x, y): return x + y

filename = input("Enter the input file name: ")
file = open(filename, 'r')
nums = file.read()
file.close()
numList = nums.split()
print(numList)
numList = list(map(int, numList))

listSum = reduce(add, numList)
average = listSum / len(numList)
print("The average is", float(average))