import random
import datetime

#SOURCES
#https://www.pythonprogramming.in/how-to-calculate-the-time-difference-between-two-datetime-objects.html
#https://stackoverflow.com/questions/43305577/python-calculate-the-difference-between-two-datetime-time-objects/43308104
#https://docs.python.org/3/library/datetime.html
#https://www.w3schools.com/python/python_ref_string.asp
#https://www.w3schools.com/python/python_classes.asp


'''
* This is a signgle position/tile on the board. 
* Value is what is displayed on a tile. The value is the number of bombs around the given tile.
* A tile is flagged when the user thinks that there is a bomb under that tile. This is done through user input.
* The board is a List of Lists where each Sublists is a row.
'''
class piece:
    def __init__(self, value):
        self.value = value
        self.display = False
        self.flag = False

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setDisplay(self, display):
        self.display = display

    def getDisplay(self):
        return self.display

    def setFlag(self, flag):
        self.flag = flag

    def getFlag(self):
        return self.flag
'''
* The board is a List of Lists where each Sublists is a row.
* The list of indices is used to display the row labels and column labels of the board
'''
board = []
indices = ['0', '1', '2', '3', '4', '5',
           '6', '7', '8', '9', 'A', 'B', 
           'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']



def main():
    print("###########################\n")
    print("# Welcome to Minesweeper! #\n")
    print("###########################\n")
       #Starting Clock

    width = getWidth()      #Getting width of board from user as input
    height = getHeight()    #Getting height of board from user as input
    bombs = getBombs(width,height)      #Function to randomly get number of bombs to put on board given the width and height.
    bombsonboard = 0        #Count of the bombs on board
    timer = clockTime()
    timeStart = 0     
    if timer == 1:
        timeStart = startClock() 
    '''
    * Loop to create the board
    * The board is a 2 dimensional list (list of lists)
    * Bombs are being added at random locations.
    * The Pieces on the board are shuffle. This is done so that the bombs are all at random positions.
    '''

    for h in range(height):
        row = []
        for w in range(width):
            if bombsonboard < bombs and random.choice([0,1]):
                p = piece('*')
                bombsonboard = bombsonboard + 1
                row.append(p)
            else:
                p = piece(0)
                row.append(p)
        board.append(row)
    random.shuffle(board)
    
    '''
    *This loop iterates over the entire board row by row.
    *It firsts checks whether a given position is a bomb or not. If not then : 
    *    If a position is not a bomb, it then calculates the number of neighbouring bombs that position has.
    *    For each non-bomb position on the board, it sets the value to the number of neighbours that have bombs.
    '''

    for h in range(height):
        for w in range(len(board[h])):
            bcount = 0
            if board[h][w].getValue() != '*':
                if h-1 in range(0, height) and w-1 in range(0, width):
                    if board[h-1][w-1].getValue() == '*':
                        bcount = bcount + 1
                if h-1 in range(0, height) and w in range(0, width):
                    if board[h-1][w].getValue() == '*':
                        bcount = bcount + 1
                if h-1 in range(0, height) and w+1 in range(0, width):
                    if board[h-1][w+1].getValue() == '*':
                        bcount = bcount + 1
                if h in range(0, height) and w-1 in range(0, width):
                    if board[h][w-1].getValue() == '*':
                        bcount = bcount + 1
                if h in range(0, height) and w+1 in range(0, width):
                    if board[h][w+1].getValue() == '*':
                        bcount = bcount + 1
                if h+1 in range(0, height) and w-1 in range(0, width):
                    if board[h+1][w-1].getValue() == '*':
                        bcount = bcount + 1
                if h+1 in range(0, height) and w in range(0, width):
                    if board[h+1][w].getValue() == '*':
                        bcount = bcount + 1
                if h+1 in range(0, height) and w+1 in range(0, width):
                    if board[h+1][w+1].getValue() == '*':
                        bcount = bcount + 1
                board[h][w].setValue(bcount)

    
    '''
    *This is the main game loop. The gameflag is used to decide whether the game is over or not. It takes user input for the move and plays the game.
    *It Iterates through the board. And gets the count of open-pieces (variable oc) and not-bomb-pieces count (variable nbc)
    * If the open-pieces are equal to number of not-bomb-pieces that means that the game is over and player has won.
    * After game over, it sets all the bombs to being visible ( Piece.setDisplay() is set to True ). 
    
    '''
    gameflag = True
    while gameflag:
        printBoard(width, height)
        coord = getInput(width, height)
        gameflag = doMove(coord, width, height)
        oc = 0
        nbc = 0
        for h in range(height):
            for w in board[h]:
                if w.getDisplay():
                    oc = oc + 1
                if w.getValue() != '*':
                    nbc = nbc + 1
        if oc == nbc:
            printBoard(width, height)
            print("You won!\n")
            if timer == 1:
                timeStop = endClock()
                datetimeFormat = '%H:%M:%S'
                overallTime = datetime.datetime.strptime(timeStop, datetimeFormat) - datetime.datetime.strptime(timeStart, datetimeFormat)
                print("Congratz, You time was in [Hr,Min,Sec]-->...", overallTime)
            gameflag = False
            return
    for h in range(height):
        for w in board[h]:
            if w.getValue() == '*':
                w.setDisplay(True)
    printBoard(width, height)
    print("Game Ended!")
    return


"""
* Asks user to enter a number for width of the board.
* Checks if it is inside the given range or not.
"""
def getWidth():
    width = input("Enter a number for width between 9 and 36: ")
    wf = True
    while wf:
        try:
            width = int(width)
            if width > 8 and width < 37:
                wf = False
            else:
                int(a)
        except:
            print("Invalid Input !")
            width = input("Enter a number for width between 9 and 36: ")
    return width


"""
* Asks user to enter a number for height of the board.
* Checks if it is inside the given range or not.
"""
def getHeight():
    height = input("Enter a number for height between 9 and 36: ")
    hf = True
    while hf:
        try:
            height = int(height)
            if height > 8 and height < 37:
                hf = False
            else:
                int(a)
        except:
            print("Invalid Input!")
            height = input("Enter a number for height between 9 and 36: ")
    return height


"""
* Asks user to enter number of bombs inside the board.
* Checks wheather the input is inside the range or not.
"""
def getBombs(width, height):
    bombs = input("Enter a number of bombs between "+str(width)+" and "+str(2*height+2*width)+": ")
    bf = True
    while bf:
        try:
            bombs = int(bombs)
            if bombs > width - 1 and bombs < 2*height+2*width + 1:
                bf = False
            else:
                int(a)
        except:
            print("Invalid Input!")
            bombs = input("Enter a number of bombs between "+str(width)+" and "+str(2*height+2*width)+": ")
    #return bombs
    return 2


"""
* printing board of width x and height y.
* printing guard cells and lines between every cell.
"""
def printBoard(width, height):
    warr = indices[:width]
    harr = indices[:height]
    topline = "    "
    midline = "    "
    for w in warr:
        topline = topline + '|' + w
        midline = midline + '|#'
    topline = topline + '|'
    midline = midline + '|'
    print("\u0332".join(topline))
    print("\u0332".join(midline))
    for h in range(height):
        rowline = " " + harr[h] + " #"
        for w in board[h]:
            if w.getFlag():
                rowline = rowline + '|' + 'F'
            elif w.getDisplay():
                rowline = rowline + '|' + str(w.getValue())
            else:
                rowline = rowline + '|' + " "
        rowline = rowline + '|'
        print("\u0332".join(rowline))


"""
* Asking user to enter x and y coordinate of the board to play the next move.
* Checks if coordinates exists withing the board or not.
* Asiking user to wheather flag or not flag that coordinate.
* returns x,y coordinate and flag or unflag.
"""
def getInput(width, height):
    wcoord = input("Enter x coordinate: ")
    while wcoord not in indices[:width]:
        print("Invalid Input !")
        wcoord = input("Enter x coordinate: ")
    hcoord = input("Enter y coordinate: ")
    while hcoord not in indices[:height]:
        print("Invalid Input !")
        hcoord = input("Enter y coordinate: ")
    f = input("Enter 'f' to flag and 'u' to unflag this box (optional). Hit [return] to open tile. Hit 'q' to surrender: ")
    while f not in ['f', 'u', 'q', '']:
        print("Invalid Input !")
        f = input("Enter 'f' to flag and 'u' to unflag this box (optional). Hit [return] to open tile. Hit 'q' to surrender: ")
    return [wcoord, hcoord, f]


"""
* do move will flag or unflag a piece depending on what was asked.
* It will tell the user if the piece is already open.
* It will tell the user if the piece is already flagged or unflagged if the same action was tried again.
* 
"""
def doMove(arr, width, height):
    x = indices.index(arr[0])
    y = indices.index(arr[1])
    flag = 'n'
    if arr[2] == 'f':
        flag = True
    elif arr[2] == 'u':
        flag = False
    elif arr[2] == 'q':
        surrender()
    p = board[y][x]
    if p.getDisplay() == False and p.getFlag():
        if flag == True:
            print("Piece already flagged!")
            return True
        elif flag == False:
            p.setFlag(False)
            return True
    elif p.getDisplay() == False and p.getFlag() == False:
        if flag == True:
            p.setFlag(True)
            return True
        elif flag == False:
            print("Piece is not flagged anyway!")
            return True
        else:
            if p.getValue() in range(1,9):
                p.setDisplay(True)
                return True
            elif p.getValue() == '*':
                youLose(width, height)
                return False
            else:
                openPiece(width, height, x, y)
                return True
    elif p.getDisplay():
        print("Piece already open!")
        return True


"""
* Check wheather the peice is open or not with all neighbours.
* if p = number , show that number on board.
* if p = * , game ends.
"""
def openPiece(width, height, x, y):
    p = board[y][x]
    if p.getDisplay():
        return
    elif p.getValue() == '*':
        return
    elif p.getValue() in range(1,9):
        p.setDisplay(True)
        return
    else:
        p.setDisplay(True)
        if y-1 in range(0, height) and x-1 in range(0, width):
            openPiece(width, height, x-1, y-1)
        if y-1 in range(0, height) and x in range(0, width):
            openPiece(width, height, x, y-1)
        if y-1 in range(0, height) and x+1 in range(0, width):
            openPiece(width, height, x+1, y-1)
        if y in range(0, height) and x-1 in range(0, width):
            openPiece(width, height, x-1, y)
        if y in range(0, height) and x+1 in range(0, width):
            openPiece(width, height, x+1, y)
        if y+1 in range(0, height) and x-1 in range(0, width):
            openPiece(width, height, x-1, y+1)
        if y+1 in range(0, height) and x in range(0, width):
            openPiece(width, height, x, y+1)
        if y+1 in range(0, height) and x+1 in range(0, width):
            openPiece(width, height, x+1, y+1)
        return
"""
Function to provide a score for every successful 
move made score is equal to time multiplied by score
"""
def score():
    pass

"""
* Asks user if they want time while playing or not.
"""

def clockTime():
    need = input("Would you like to keep time? --> Y / N? ...")
    if need.upper() == "Y":
        print("Ok, I will start the clock after we get the board setup. ")
        temp = 1
    elif need.upper() == "N":
        print("Ok, kick back and relax and enjoy the game. without the added time stress.")
        temp = 0

    return temp


"""
* When game is started, returns start time.

"""
def startClock():
    start = datetime.datetime.now().strftime("%H:%M:%S")
    print("The clock has started...")
    return start


"""
* When game is finished, returns end time.

"""
def endClock():
    end = datetime.datetime.now().strftime("%H:%M:%S")
    print("The clock has stopped...")
    return end


"""
* When user loses the game, Board is printed with bombs on it.
* User is asked again to play game or not.

"""
def youLose(width, height):
    for h in range(height):
        for w in board[h]:
            if w.getValue() == '*':
                w.setDisplay(True)
    printBoard(width, height)
    print("Oops, Looks like you opened a tile with a bomb on it, better luck next time.")
    print("Game Ended !\n")
    choice = input("Would you like to try again? ---> Y or N?...")
    if choice.upper() == "Y":
        print("Good Choice...")
        main()
    else:
        print("Good Bye!...")
        quit()
        
        
"""
* When user presses q, the game terminates.

"""
def surrender():
    print("Thanks for playing the computer has won this time, Please come again!")
    quit()

main()