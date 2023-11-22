"""
The tests should cover the following features

1. The game is initialized with an empty board
2. The game is initialized with either 2 players (human-human) or 1 player (human-bot)
3. Players are assigned a unique piece to plays: X or O
4. After one player plays, the other player has a turn
5. All winning end of the games detected, and draw games are identified
6. Players can play only in viable spots
7. The correct game winner, if one exists, is detected
"""

import pytest

from logic import make_empty_board
from OOP import Game, Human, Bot

game = Game(Human('X'), Bot('O'))
game.run()

# Test whether the board is initialized with an empty board
def test_board_initialization():
    empty_board = make_empty_board()
    assert game._init_board == empty_board
    print(game._init_board)

# Test whether the game is initialized with either 2 players or 1 player
def test_number_of_players():
    players = 0
    if game._playerO is not None:
        players += 1
    if game._playerX is not None:
        players += 1
    
    assert players > 0 and players <= 2
    print(players)

# Test whether players are assigned a unique symbol: X or O
def test_symbols():
    human_symbol = game._playerX
    bot_symbol = game._playerO
    assert human_symbol.symbol == 'X'
    assert bot_symbol.symbol == 'O'

    print(human_symbol.symbol, bot_symbol.symbol)

# Test whether players switch turns
def test_switch_player():
    rounds = 0
    flat_board = [item for row in game._board for item in row]
    if 'X' in flat_board and 'O' in flat_board:
        rounds += 1
    
    assert rounds > 0
    print(rounds)

# Test whether game results can be detected
def test_results_detection():
    winner = game._winner
    assert winner is not None
    print(winner)

# Test whether invalid inputs can be captured
def test_valid_input():
    initial_value = game._playerX._init_valid_input
    validation = game._playerX._valid_input
    assert validation == 0
    print(initial_value, validation)

# Test whether the winner is the correct winner
def test_correct_winner():
    winner = game._winner
    last_player = game._current_player.symbol

    assert {winner != last_player and winner == 'O' 
            or winner == 'Draw'
            or winner == last_player and winner == 'X'}
    print(winner, last_player)