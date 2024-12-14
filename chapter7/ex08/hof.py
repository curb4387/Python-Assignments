def myMap(func, lyst):
    newList = []
    for item in lyst:
        newList.append(func(item))
    return newList

def myFilter(func, lyst):
    newList = []
    for item in lyst:
        if func(item) == True:
            newList.append(item)
    return newList

def myReduce(func, lyst):
    total = lyst[0]
    for i in lyst[1:]:
        total = func(total, i)
    return total