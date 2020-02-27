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
    while winner == None:
        (x, y) = players[player].take_turn(board, player)
        board = board.make_move(Action(y * 3 + x, player + 1))
        player = 1 - player
        winner = board.get_winner()
        move_count += 1
        if move_count == 9:
            break
    if print_win:
        print(f'{winner} wins!')
    return winner


def get_player_score(game_count, player1, player2):
    wins = 0
    ties = 0
    for i in range(game_count):
        if i % 2 == 0:
            winner = play_game(player1, player2)
            if winner == 1:
                wins += 1
        else:
            winner = play_game(player2, player1)
            if winner == 2:
                wins += 1
        if winner == None:
            ties += 1
    if ties == game_count:
        return None
    score = wins / (game_count - ties)
    return score


training_steps = 1000
player = WeightedPlayer(np.zeros((9, 9)))
batch_size = 10
for i in range(training_steps):
    gradients = []
    score = get_player_score(500, player, RandomPlayer())
    for _ in range(batch_size):
        new_player = player.mutate(0.1)
        new_score = get_player_score(50, new_player, RandomPlayer())
        gradients.append(new_player.gradient * (new_score - score))
    print(score)
    player = WeightedPlayer(player.weights + sum(gradients) / batch_size)

print(get_player_score(10000, player, RandomPlayer()))

print_win = True
print(get_player_score(4, player, HumanPlayer()))
