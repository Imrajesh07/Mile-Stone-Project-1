'''
Created on 04-Mar-2018

@author: imraj
'''


import random
from docutils.utils.math.math2html import Position


def clear_output():
    print("\n" * 100)
    
    
def display_board(board):
    # clear_output()
    print(f"   |   |   \n {board[1]} | {board[2]} | {board[3]} \n   |   |   ")
    print('---|---|---')
    print(f"   |   |   \n {board[4]} | {board[5]} | {board[6]} \n   |   |   ")
    print('---|---|---')
    print(f"   |   |   \n {board[7]} | {board[8]} | {board[9]} \n   |   |   ")
    
    
def player_input():
    marker = ""
    
    while not (marker == "O" or marker == "X"):
        marker = input("Select marker for player 1: ").upper()
        print(marker)
    
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')
    
    
def place_marker(board, marker, position):
    board[position] = marker
    
    
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
   
def choose_first():
    player = random.randint(1, 2)
    if player == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    
    
def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == " ":
            return False
    else:
        return True
    
    
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Enter your next position: "))
    else:
        return position
    
    
def replay():
    return input("Do you want to replay.\n1. Yes\n2. No\n").lower().startswith('y')
   
    
print("Welcome to Tic Toc Toe")

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will play first")
    
    while not full_board_check(board):
        
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board, player1_marker):
                print("Player 1 wins")
                break
            else:
                turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board, player2_marker):
                print("Player 2 wins")        
                break
            else:
                turn = "Player 1"
    else:
        print("Game is tied")
        
    if not replay():
        break
