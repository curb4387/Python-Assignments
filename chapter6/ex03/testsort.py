# define isSorted that returns a bool value
def isSorted(list):
    previousItem = list[0]
    sorted = True
    count = 0
    for item in list:
        print(list[count])
        if item >= previousItem:
            sorted = True
        else:
            sorted = False
            break
        previousItem = list[count]
        count += 1
    return sorted


def main():
    list = [1, 2]
    print(isSorted(list))

if __name__ == "__main__":
    main()