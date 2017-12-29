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
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Implementing 'X' and 'O' on board from user player_input
def place_marker(board, marker, position):
    board[position] = marker

# Checking if there is a winner!
def win_check(board,mark):
            # horizontal
    return  ((board[7] == mark and board[8] == mark and board[9] == mark)
            or (board[4] == mark and board[5] == mark and board[6] == mark)
            or (board[1] == mark and board[2] == mark and board[3] == mark)
            # vertical
            or (board[7] == mark and board[4] == mark and board[1] == mark)
            or (board[8] == mark and board[5] == mark and board[2] == mark)
            or (board[9] == mark and board[6] == mark and board[3] == mark)
            # diagonal
            or (board[7] == mark and board[5] == mark and board[3] == mark)
            or (board[9] == mark and board[5] == mark and board[1] == mark))

# Accounts for edge case: space on the board
def space_check(board, position):
    return board[position] == ' '

# Checks if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

board = range(1,10)
print (display_board(board))
currPos = player_input()
place_marker(board, 'X', currPos)
print (display_board(board))
