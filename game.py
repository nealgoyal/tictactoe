from __future__ import print_function

# Outputting the tic tac toe board
from IPython.display import clear_output
def display_board(board):
    clear_output()
    for element in board[::3]:
        if element < 10:
            print(" ", element, " | ", element + 1, " | ", element + 2)
        if element < 7:
            print("-----|-----|-----")

# Creating player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()

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

# Alternates between Player 1 & 2
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# User chooses position
def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):

        position = raw_input('Choose your next position: (1-9) ')
    return int(position)

def replay():

    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
