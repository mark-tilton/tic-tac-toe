import random as rand
import numpy as np

from board import Board
from action import Action
from weighted_player import WeightedPlayer
from random_player import RandomPlayer
from human_player import HumanPlayer


print_win = False


def play_game(p1, p2):
    players = [p1, p2]
    board = Board()
    player = 0
    winner = None
    move_count = 0
    moves = []
    while winner == None:
        pos = players[player].take_turn(board, player)
        action = Action(pos, player + 1)
        board = board.make_move(Action(pos, player + 1))
        moves.append((board, action))
        player = 1 - player
        winner = board.get_winner()
        move_count += 1
        if move_count == 9:
            break
    if print_win:
        print(f'{winner} wins!')
    return winner, moves


def get_player_score(game_count, player1, player2):
    wins = 0
    ties = 0
    winning_moves = []
    for i in range(game_count):
        if i % 2 == 0:
            winner, moves = play_game(player1, player2)
            if winner == 1:
                wins += 1
        else:
            winner, moves = play_game(player2, player1)
            if winner == 2:
                wins += 1
        winning_moves += ((board, action) for (board, action) in moves if winner == action.val)
        if winner == None:
            ties += 1
    if ties == game_count:
        return None
    score = wins / (game_count - ties)
    return (score, winning_moves)

for _ in range(100):
    ai = WeightedPlayer()
    score, winning_moves = get_player_score(2, ai, HumanPlayer())
    print(score)
    ai.train(winning_moves)


score, _ = get_player_score(10000, ai, RandomPlayer())
print(score)

print_win = True
score, _ = get_player_score(4, ai, HumanPlayer())
print(score)
