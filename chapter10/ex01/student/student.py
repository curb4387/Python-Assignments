### Checkers! This Python file allows 2 users to play Checkers against one another.
"""This game of Checkers follows normal Checkers rules whch are as follows:
- Black moves first
- All pieces must move forward diagonally (away from their start) and cannot move
backwards unless they first reach the opposing back row and are "kinged"
- All jumps are enforced
- If 2 or more jumps exist, the user may choose any jump they like
- If 1 player cannot move, the other player wins the game"""
# To review the rules, please check the following link:
# https://en.wikipedia.org/wiki/Checkers#General_rules

### Items (dictionary + 3 lists) used to determine moves
"""These coordinates correspond to what a user types in to move a piece.
The coordinates displayed on the board are A-H (left to right) and 1-8 (top to bottom).
When converted with this dictionary, this allows us to get to the exact piece that
the user wishes to move."""

coords = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"1":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7}
coordsRow = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}
coordsCol = {0:"1",1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8"}
rowList = ['1','2','3','4','5','6','7','8']
columnList = ['A','B','C','D','E','F','G','H']
jumpList = []

### Validating functions used in Checkers ###

# This function determines if a move is valid or not
def checkMove(move): # match pattern "6 A"
    if len(move) == 3:
        # condition: 6 in rowList, " ", A in columnList
        if move[0] in rowList and move[1] == " " and move[2] in columnList:
            match = 1
        else:
            match = 0
    else:
        match = 0
    return match

# This function gets the piece at the location provided by the user
def getPiece(piece): # for "6 A"
    # separate and put row-column piece into a list to find its coordinates
    # list: ['6', 'A'], coords = 5, 0
    piece_list = piece.split()
    c0 = coords[piece_list[0]]
    c1 = coords[piece_list[1]]
    return board[c0][c1]

# This function allow sthe user to move the piece from 1 square to another.
# It sets the square the piece moves from to empty "-"
def movePiece(moveFrom, moveTo): # for "6 A"
    from_ = getPiece(moveFrom)
    # Set move from to blank
    piece_list = moveFrom.split()
    c0 = coords[piece_list[0]]
    c1 = coords[piece_list[1]]
    board[c0][c1] = '-'
    # Set move to as player
    piece_list = moveTo.split()
    c0 = coords[piece_list[0]]
    c1 = coords[piece_list[1]]
    board[c0][c1] = from_

# This function is the game board, not to be confused with being bored.
def startBoard():
    row8 = [' ','r',' ','r',' ','r',' ','r']
    row7 = ['r',' ','r',' ','r',' ','r',' ']
    row6 = [' ','r',' ','r',' ','r',' ','r']
    row5 = ['-',' ','-',' ','-',' ','-',' ']
    row4 = [' ','-',' ','-',' ','-',' ','-']
    row3 = ['b',' ','b',' ','b',' ','b',' ']
    row2 = [' ','b',' ','b',' ','b',' ','b']
    row1 = ['b',' ','b',' ','b',' ','b',' ']
    board = [row8,row7,row6,row5,row4,row3,row2,row1]
    return board

# This function displays the board (as shown above) to the users
# with column and row identifiers (coordinates) to help the user select a piecec and move
def printBoard(board):
    x = 1
    print("   A B C D E F G H (Column values)")
    print('  _________________')
    for item in board:
        print(str(x) + " |" + " ".join(map(str, item)) + "| " + str(x))
        x = x + 1
    print('  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    print("   A B C D E F G H")

# This function checks to see whether the move is valid by determining whether
# the piece is being moved in the correct direction or not
# (diagonally forward for non-king pieces)
def checkFromTo(moveFrom, moveTo, p):
    piece_from = moveFrom.split()
    piece_to = moveTo.split()
    c0f = coords[piece_from[0]] # row from
    c1f = coords[piece_from[1]] # column from
    c0t = coords[piece_to[0]] # row to
    c1t = coords[piece_to[1]] # column to
    if p == 1 and (c0f - c0t) == 1 and abs(c1f - c1t) == 1:
        return 1
    elif p == 2 and (c0t - c0f) == 1 and abs(c1f - c1t) == 1:
        return 1
    else:
        return 0

# tbd
def checkJump(p, jumpList):
    for x in range(8):
        for y in range(8):
            if p == 1 and board[x][y] == 'b': # example = 5, 0
                if x <= 1:
                    abc = 1

                elif y <= 1:
                    # TEST SINGLE DIRECTION DIAGONAL JUMP (LEFT TO RIGHT)
                    if board[x - 1][y + 1] == 'r' and board[x - 2][y + 2] == '-': # r at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x - 2] + ' ' + coordsRow[y + 2])
                        print("TEST SINGLE DIRECTION DIAGONAL JUMP (LEFT TO RIGHT)")

                elif y >= 6:
                    # TEST SINGLE DIRECTION DIAGONAL JUMP (RIGHT TO LEFT)
                    if board[x - 1][y - 1] == 'r' and board[x - 2][y - 2] == '-': # r at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x - 2] + ' ' + coordsRow[y - 2])
                        print("TEST SINGLE DIRECTION DIAGONAL JUMP (RIGHT TO LEFT)")

                else:
                    # TEST BOTH DIRECTIONS
                    if board[x - 1][y + 1] == 'r' and board[x - 2][y + 2] == '-': # r at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x - 2] + ' ' + coordsRow[y + 2])
                        print("BOTH DIAGONAL LEFT TO RIGHT")

                    if board[x - 1][y - 1] == 'r' and board[x - 2][y - 2] == '-': # r at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x - 2] + ' ' + coordsRow[y - 2])
                        print("BOTH DIAGONAL LEFT TO RIGHT")

            if p == 2 and board[x][y] == 'r':
                if x >= 6:
                    abc = 1

                elif y <= 1:
                    if board[x + 1][y + 1] == 'r' and board[x + 2][y + 2] == '-': # r is at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x + 2] + ' ' + coordsRow[y + 2])

                elif y >= 6:
                    if board[x + 1][y - 1] == 'r' and board[x + 2][y - 2] == '-': # r is at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x + 2] + ' ' + coordsRow[y - 2])

                else:
                    if board[x + 1][y + 1] == 'r' and board[x + 2][y + 2] == '-': # r is at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x + 2] + ' ' + coordsRow[y + 2])

                    if board[x + 1][y - 1] == 'r' and board[x + 2][y - 2] == '-': # r is at 4, 1
                        jumpList.append(coordsCol[x] + ' ' + coordsRow[y] + ' ---> ' + coordsCol[x + 2] + ' ' + coordsRow[y - 2])

# This function uses the logic from the other fucntions to enforce the game rules and
# determine overall whether the move is legal or not, and if not, displays a message
# to the user regarding what went wrong
def legalMove(moveFrom, moveTo, p):
    if checkMove(moveFrom) == 1 and checkMove(moveTo) == 1:
        if getPiece(moveFrom) == ' ' or getPiece(moveTo) == ' ':
            print("")
            print("You have selected an invalid square.")
            print("")
            match = 0
        elif getPiece(moveTo) != '-':
            print("")
            print("This square is occupied. Please select a valid square to move to.")
            print("")
            match = 0
        elif checkFromTo(moveFrom, moveTo, p) == 0:
            print("")
            print("Please select a valid move adjacent to your square.")
            print("")
            match = 0
        elif ((getPiece(moveFrom).lower() == 'b' and p == 1) or (getPiece(moveFrom).lower() == 'r' and p == 2)):
            match = 1 # valid move
        else:
            print("")
            print("Please select a piece that is yours.")
            print("")
            match = 0
    else:
        print("")
        print("This is not a legal move. Please enter a legal move (ex. 6 A).")
        print("")
        match = 0
    return match

### Game introduction ###

print("""Welcome to Checkers! 
Checkers pits the black pieces against the red pieces 
where the objective of the game is to capture all of 
your opponent's pieces. Black moves first!
""")
player1 = input("Who is playing as black?: ") + " (Black)"
player2 = input("Who is playing as red?: ") + " (Red)"
print('')
print(f"Welcome, {player1} and {player2}! Let's get started...")
print('')

board = startBoard()

### Main game loop ###

z = 1
p = 1
while z < 5:
    printBoard(board)
    lm = 0
    # Loop until a legal move is made
    while lm == 0:
        checkJump(p, jumpList)
        print(jumpList)
        if p == 1 and jumpList == []:
            moveFrom = input(f"{player1}, what piece would you like to move? ('row column', example: 6 A): ")
            moveTo = input(f"{player1}, where would you like to move this piece? ('row column', example: 5 B): ")
            lm = legalMove(moveFrom, moveTo, p)
        elif p == 1:
            jumpChoice = ''
            while jumpChoice == '':
                print('')
                print("Here are the available jumps:")
                for num in range(len(jumpList)):
                    print("Jump " + str(num + 1) + ": " + str(jumpList[num]))
                jumpSelected = input(f"{player1}, which jump would you like to take? (please select the jump number from above, example: 1): ")
                try:
                    jumpChoice = int(jumpSelected)
                    if jumpChoice > 0 and jumpChoice <= len(jumpList):
                        jumpChoice = jumpList[jumpChoice - 1]
                    else:
                        jumpChoice = ''
                except:
                    jumpChoice = ''
        elif p == 2 and jumpList == []:
            moveFrom = input(f"{player2}, what piece would you like to move? ('row column', example: 6 A): ")
            moveTo = input(f"{player2}, where would you like to move this piece? ('row column', example: 5 B): ")
            lm = legalMove(moveFrom, moveTo, p)
        elif p == 2:
            jumpChoice = ''
            while jumpChoice == '':
                print('')
                print("Here are the available jumps:")
                for num in range(len(jumpList)):
                    print("Jump " + str(num + 1) + ": " + str(jumpList[num]))
                jumpSelected = input(f"{player2}, which jump would you like to take? (please select the jump number from above, example: 1): ")
                try:
                    jumpChoice = int(jumpSelected)
                    if jumpChoice > 0 and jumpChoice <= len(jumpList):
                        jumpChoice = jumpList[jumpChoice - 1]
                    else:
                        jumpChoice == ''
                except:
                    jumpChoice == ''

    jumpList = []

    getPiece(moveFrom)
    getPiece(moveTo)
    movePiece(moveFrom, moveTo)

    if p == 1:
        p = 2
    else:
        p = 1
    # xx = checkMove(moveFrom)
    # yy = checkMove(moveTo)
    # print(xx, yy)

    # temp_list = moveFrom.split()
    # print(temp_list, coords[temp_list[0]], coords[temp_list[1]], board[coords[temp_list[0]]][coords[temp_list[1]]])

    # temp_list = moveTo.split()
    # print(temp_list, coords[temp_list[0]], coords[temp_list[1]], board[coords[temp_list[0]]][coords[temp_list[1]]])