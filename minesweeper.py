import random as r
import sys
import re

gameState = 1 #sets the gamestate to active, win, or loss
bomb = 0 #counts number of bombs flagged

#dimension of board and number of bombs
width = int(sys.argv[1])
height = int(sys.argv[2])
b = int(sys.argv[3])

#shows the board specified (grid or sol)
def show(board):
    for i in range(1, height + 1):
        print(*board[i][1:width + 1])
    print()


#asks user to select point and to clear or flag that point, then executes the appropriate series of events
def coord():
    global bomb
    pos = input("Enter a position by using the 'x y function' format, where x is the x coordinate, y is the y value, and function is either 'c' for clear and 'f' for flag: \n")
    num = list(map(int, re.findall(r'\d+', pos)))
    if "c" in pos:
        if sol[num[1]][num[0]] != "*":
            print("You've cleared " + str(num[0]) + ", " + str(num[1]) + ".\n")
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if sol[num[1]][num[0]] == 0:
                        grid[num[1] + i][num[0] + j] = sol[num[1] + i][num[0] + j]
            for i in range(1, height + 1):
                for j in range(1, width + 1):
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if grid[i][j] == 0:
                                grid[i + x][j + y] = sol[i + x][j + y]
        else:
            global gameState
            gameState = 2
        show(grid)
    elif "f" in pos:
        global b
        print("You've flagged " + str(num[0]) + ", " + str(num[1]) + ".\n")
        grid[num[1]][num[0]] = "f"
        if sol[num[1]][num[0]] == "*":
            global bomb
            bomb += 1
        if bomb == b:
            gameState = 3
        show(grid)

    else:
        print("Please use the correct format.")

try:
    #creates the board
    sol = []
    for i in range(height + 2):
        sol.append([0] * (width + 2))

    #places bombs
    for i in range(b):
        x = r.randint(1, width)
        y = r.randint(1, height)
        if sol[x][y] != "*":
            sol[x][y] = '*'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if sol[x + i][y + j] != "*":
                        sol[x + i][y + j] += 1

    grid = []
    for i in range(height + 2):
        grid.append(["x"] * (width + 2))

    show(grid)

except ValueError:
    print("Please input 3 integers to determine the board dimensions and number of bombs.")
    print("Ex. 'minesweeper.py 5 5 3' would give a board of dimension 5x5 with 3 bombs.")

while gameState == 1:
    try:
        coord()
    except IndexError:
        print("Please input a coordinate that is on the board.")

if gameState == 3:
    print("Congratulations! You've found all the bombs!\n")
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝")
    print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗")
    print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝")
    print("")

if gameState == 2:
    print("Sorry! You hit a bomb.")
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗██╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝██║")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ██║")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ╚═╝")
    print("   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗██╗")
    print("   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝")
    print("")
