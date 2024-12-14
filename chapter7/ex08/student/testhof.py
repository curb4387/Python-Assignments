from functools import reduce
from hof import myMap, myFilter, myReduce

def odd(x): return x % 2 == 1
def add(x, y): return x + y
def multiply(x, y): return x * y

lyst = [2, 3, 53, 10, 20, 78, 16]

# Test myMap function
mapList = myMap(int, lyst)
print("myMap's answer:", mapList)
print("Python's answer:", list(map(int, lyst)))

# Test myFilter function
filterList = myFilter(odd, lyst)
print("myFilter's answer:", filterList)
print("Python's answer:", list(filter(odd, lyst)))

# Test myReduce function
reduceList = myReduce(add, lyst)
print("myReduce's answer:", reduceList)
print("Python's answer:", reduce(add, lyst))