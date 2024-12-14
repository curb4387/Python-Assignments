# range = highestnum - lowestnum
def myRange(start, stop = None, step = None):
    if stop == None and step == None:
        stop = start
        start = 0
        step = 1
    elif step == None:
        step = 1
    valueList = []
    if step == 0:
        return print(valueList = [])
    if step > 0:
        if start >= stop:
            return print(valueList = [])
        num = start
        while num < stop:
            valueList.append(num)
            num += step
    else:
        if start <= stop:
            return print(valueList = []) 
        num = start
        while num > stop:
            valueList.append(num)
            num += step
    return valueList

def main():
    print(myRange(10))
    print(myRange(1, 10))
    print(myRange(1, 10, 2))
    print(myRange(10, 1, -1))

if __name__ == "__main__":
    main()