from __future__ import print_function

# Outputting the tic tac toe board
from IPython.display import clear_output
def display_board(board):
    for element in board[::3]:
        if element < 10:
            print(" ", element, " | ", element + 1, " | ", element + 2)
        if element < 7:
            print("-----|-----|-----")



board = range(1,10)
print (display_board(board))
