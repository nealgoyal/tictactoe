from __future__ import print_function

# Outputting the tic tac toe board
from IPython.display import clear_output
def display_board(board):
    for element in board[::3]:
        if element < 10:
            print(" ", element, " | ", element + 1, " | ", element + 2)
        if element < 7:
            print("-----|-----|-----")

# Creating player input
def player_input():
    pos = input("Enter position: ")
    while pos not in board:
        pos = input("Enter position: ")

    return pos

# Implementing 'X' and 'O' on board from user player_input
def place_marker(board, marker, position):
    board[position] = marker


board = range(1,10)
print (display_board(board))
currPos = player_input()
place_marker(board, 'X', currPos)
print (display_board(board))
