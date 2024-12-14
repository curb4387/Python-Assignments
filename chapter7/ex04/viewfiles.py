import os, os.path

def displayFiles(pathname):
    if os.path.isfile(pathname):
        file = open(pathname, 'r')
        contents = file.read()
        file.close()
        return print(pathname, "\n", contents)
    elif os.path.isdir(pathname):
        for item in os.listdir(pathname):
            itemPathname = os.path.join(pathname, item)
            displayFiles(itemPathname)

def main():
    displayFiles(input("Enter pathname: "))

if __name__ == "__main__":
    main()