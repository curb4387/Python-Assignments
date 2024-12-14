QUIT = '5'
COMMANDS = '1', '2', '3', '4', '5'
MENU = """1   Open
2   Save
3   Compile
4   Run
5   Quit"""

# Displays menu of commands
def printMenu(MENU):
    return print(MENU)

# Accepts an input command from user
def acceptCommand(menuLen):
    command = int(input("Enter a number: "))
    while command > menuLen:
        command = input("Enter a number: ")
    return str(command)

# Calls a function to perform the command
def performCommand(command):
    if command == '1':
        return print("Command = Open")
    elif command == '2':
        return print("Command = Save")
    elif command == '3':
        return print("Command = Compile")
    elif command == '4':
        return print("Command = Run")
    elif command == QUIT:
        return print("Have a nice day!")

def main():
    while True:
        printMenu(MENU)
        command = acceptCommand(len(COMMANDS))
        performCommand(command)
        if command == QUIT:
            break

if __name__ == "__main__":
    main()