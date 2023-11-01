def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner(board):
    winner = None

    # Check if any row has a winner
    for r in range(3):
      if board[r][0] == board[r][1] == board[r][2] and board[r][0] != None:
        winner = True

    # Check if any column has a winner
      elif board[0][r] == board[1][r] == board[2][r] and board[0][r] != None:
        winner = True

    # Check if any diagonal has a winner
      elif board[1][1] != None and board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        winner = True

    # If no one wins, it's a draw
    if winner is False:
      print('It's a draw')

    return winner

def place_input(player, user_input):
  if int(user_input) == 1 and board[0][0] == None:
    board[0][0] = player
  elif int(user_input) == 2 and board[0][1] == None:
    board[0][1] = player
  elif int(user_input) == 3 and board[0][2] == None:
    board[0][2] = player
  elif int(user_input) == 4 and board[1][0] == None:
    board[1][0] = player
  elif int(user_input) == 5 and board[1][1] == None:
    board[1][1] = player
  elif int(user_input) == 6 and board[1][2] == None:
    board[1][2] = player
  elif int(user_input) == 7 and board[2][0] == None:
    board[2][0] = player
  elif int(user_input) == 8 and board[2][1] == None:
    board[2][1] = player
  elif int(user_input) == 9 and board[2][2] == None:
    board[2][2] = player
