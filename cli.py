# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import print_board
from logic import place_input
from logic import get_winner
from logic import other_player

board_index = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def get_player_input(player):
  print(f"Player {player}'s turn!")
  user_input = input("Please choose an empty spot by typing its corresponding number: ")

  if int(user_input) in range(1, 10):
    place_input(board, player, user_input)
  
  else:
    print("Invalid input!")
    get_player_input(player)


if __name__ == '__main__':
  # Get an empty board
  board = make_empty_board()
  winner = None
  player = 'X'  # Let's start with player X

  # Provide instructions for input
  print("This is our board:")
  print_board(board)

  print("Here's what number each spot is represented by:")
  print_board(board_index)

  while winner is None:
    # Player's turn
    get_player_input(player)

    # Update the board
    print_board(board)

    # Check if there's a winner
    winner = get_winner(board)

    # If there's a winner or a draw, break the loop
    if winner is not None:
      break

    # Switch the player for next turn
    player = other_player(player)

    # Check again for winner
    winner = get_winner(board)

  # Print winner
  if winner == "Draw":
    print(f"It's a {winner}")
  else:
    print(f"{winner} won")