def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
  for row in board:
    print(row)

def get_winner(board):
    for r in range(3):
        # Check if any row has a winner
        if board[r][0] is not None and (board[r][0] == board[r][1] == board[r][2]):
            return board[r][0]
            
        # Check if any column has a winner
        elif board[0][r] is not None and (board[0][r] == board[1][r] == board[2][r]):
            return board[0][r]

    # Check if any diagonal has a winner
    if board[1][1] is not None and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]

    # If no one wins and board is full, it's a draw
    flat_board = [item for row in board for item in row]
    if None not in flat_board:
        return "Draw"

    # If the board isn't full and no one has won yet
    return None


def place_input(board, player, user_input):
  if int(user_input) == 1 and board[0][0] is None:
    board[0][0] = player
  elif int(user_input) == 2 and board[0][1] is None:
    board[0][1] = player
  elif int(user_input) == 3 and board[0][2] is None:
    board[0][2] = player
  elif int(user_input) == 4 and board[1][0] is None:
    board[1][0] = player
  elif int(user_input) == 5 and board[1][1] is None:
    board[1][1] = player
  elif int(user_input) == 6 and board[1][2] is None:
    board[1][2] = player
  elif int(user_input) == 7 and board[2][0] is None:
    board[2][0] = player
  elif int(user_input) == 8 and board[2][1] is None:
    board[2][1] = player
  elif int(user_input) == 9 and board[2][2] is None:
    board[2][2] = player

def other_player(player = ''):
  if player == 'X':
    player = 'O'
  
  else:
    player = 'X'
  
  return player