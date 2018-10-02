import random as r
import sys

#dimension of board and number of bombs
width = int(sys.argv[1])
height = int(sys.argv[2])
b = int(sys.argv[3])

#creates the board
board = []
for i in range(height + 2):
    board.append([0.0] * (width + 2))

#places bombs
for i in range(b):
    x = r.randint(0, width - 1)
    y = r.randint(0, height - 1)
    board[x][y] = 0.1

for i in range(width):
    x = 0
    y = 0
    if board[x][y] == 0.1:
        if board[x + 1][y] or board[x - 1][y] or board[x + 1][y + 1] or board[x + 1][y - 1] or board[x][y + 1] or board[x][y - 1] != 0.1:
            if board[x - 1][y + 1] or board[x - 1][y - 1] != 0.1:
                board[x + 1][y] += 1
                board[x - 1][y] += 1
                board[x][y + 1] += 1
                board[x][y - 1] += 1
                board[x + 1][y + 1] += 1
                board[x + 1][y - 1] += 1
                board[x - 1][y + 1] += 1
                board[x - 1][y - 1] += 1
        x += 1

#prints board
for row in board:
    print(row)
