from logic import make_empty_board, print_board, get_winner
from operator import *
import random
import time
import os

def record_winner(text, filename, directory):
  file_path = os.path.join(directory, filename)

  with open(file_path, 'a') as f:
    f.write(text + '\n' + '\n')

def dict_to_csv(data):
  return '\n'.join([f'{key}: {value}' for key, value in data.items()])

game_data = {}

class Game:
    def __init__(self, playerX, playerO):
        self._init_board = make_empty_board()
        self._board = make_empty_board()
        self._boardIndex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = playerX
        self._winner = None
        self._game_id = time.time()

    def switch_players(self):
        if self._current_player == self._playerO:
            self._current_player = self._playerX
        else:
            self._current_player = self._playerO

    def run(self):
        print("This is our board:")
        print_board(self._board)

        print("Here's what number each spot is represented by:")
        print_board(self._boardIndex)

        game_start_time = time.time()

        while self._winner is None:
            # Player's turn
            if isinstance(self._current_player, Human):
                self._current_player.get_player_input(self._board)

            elif isinstance(self._current_player, Bot):
                print("Bot's turn!")
                i, j = self._current_player.get_bot_input(self._board)
                if (i, j) is not None:
                    self._board[i][j] = self._current_player.symbol

            # Update the board
            print_board(self._board)

            # Check if there's a winner
            self._winner = get_winner(self._board)

            # If there's a winner or a draw, break the loop
            if self._winner is not None:
                game_end_time = time.time()
                break

            # Switch the player for the next turn
            self.switch_players()

        # Print the winner
        if self._winner == "Draw":
            print(f"It's a {self._winner}")
        else:
            print(f"{self._winner} won")

        # Record game data
        game_data['game_id'] = self._game_id
        game_data['game_duration'] = game_end_time - game_start_time

        # Record rounds
        flat_board_rounds = [item for row in self._board for item in row]
        x_times = countOf(flat_board_rounds, 'X')/2
        o_times = countOf(flat_board_rounds, 'O')/2

        game_data['rounds'] = x_times + o_times

        # Record winner and check if winner is first player
        if self._winner == 'X':
            game_data['winner'] = 'Human (Player X)'
            game_data['winner is first player'] = True
        elif self._winner == 'O':
            game_data['winner'] = 'Bot (Player O)'
            game_data['winner is first player'] = False
        else:
            game_data['winner'] = 'None'
            game_data['winner is first player'] = None


class Human:
    def __init__(self, symbol):
        self.symbol = symbol
        self._init_valid_input = 1
        self._valid_input = 1

    def place_input(self, board, symbol, user_input):
        if int(user_input) == 1 and board[0][0] is None:
            board[0][0] = symbol
        elif int(user_input) == 2 and board[0][1] is None:
            board[0][1] = symbol
        elif int(user_input) == 3 and board[0][2] is None:
            board[0][2] = symbol
        elif int(user_input) == 4 and board[1][0] is None:
            board[1][0] = symbol
        elif int(user_input) == 5 and board[1][1] is None:
            board[1][1] = symbol
        elif int(user_input) == 6 and board[1][2] is None:
            board[1][2] = symbol
        elif int(user_input) == 7 and board[2][0] is None:
            board[2][0] = symbol
        elif int(user_input) == 8 and board[2][1] is None:
            board[2][1] = symbol
        elif int(user_input) == 9 and board[2][2] is None:
            board[2][2] = symbol

    def get_player_input(self, board):
        flat_board = [item for row in board for item in row]
        player_input_order = []
        print(f"Player's turn!")
        user_input = input("Please choose an empty spot by typing its corresponding number: ")


        if int(user_input) in range(1, 10) and flat_board[int(user_input)-1] is None:
            self.place_input(board, self.symbol, user_input)
            player_input_order.append(user_input)
        else:
            print("Invalid input!")
            self._valid_input -= 1
            self.get_player_input(board)

        # Record first move
        game_data['first_move'] = player_input_order[0]

        return self._valid_input


class Bot:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_bot_input(self, board):
        empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]
        if empty_spots:
            return random.choice(empty_spots)
        else:
            return None

# Start game with Human and Bot players
game = Game(Human('X'), Bot('O'))
game.run()
csv_player_data = dict_to_csv(game_data)
record_winner(csv_player_data, "database2", "logs")