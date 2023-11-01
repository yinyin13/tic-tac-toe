# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import place_input
from logic import get_winner
from logic import other_player

board_index = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

if __name__ == '__main__':
    board = make_empty_board()
    winner = None

    print("This is our board:")
    for row in board:
      print(row)
    print("Here's what number each spot is represented by.")
    for r in board_index:
      print(r)

    while winner == None:
      # Player X goes first
        print("TODO: Player X's turn!")
        player = 'X'
        user_input = input("Please choose an empty spot by typing its corresponding number: ")
        place_input(player, user_input)

      # Update the board
        for row in board:
          print(row)

        # Player O goes next
        print("TODO: Player O's turn!")
        player = 'O'
        user_input = input("Please choose an empty spot by typing its corresponding number: ")
        place_input(player, user_input)

      # Update the board
        for row in board:
            print(row)

        winner = get_winner(board)
