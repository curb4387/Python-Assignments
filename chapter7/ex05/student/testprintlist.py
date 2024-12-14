def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])

def main():
    seq = "Hello there world!"
    printAll(seq)

if __name__ == "__main__":
    main()