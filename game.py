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
    moves = [[],[]]
    while winner == None:
        pos = players[player].take_turn(board, player)
        action = Action(pos, player + 1)
        one_hot_action = np.zeros(9)
        one_hot_action[action.pos] = 1
        moves[player].append((board.get_normalized_cells(player), one_hot_action))
        board = board.make_move(action)
        winner = board.get_winner()
        move_count += 1
        if move_count == 9:
            break
        player = 1 - player
    if print_win:
        print(f'{winner} wins!')
    if winner == None:
        return None, moves[0] + moves[1]
    return winner, moves[int(winner - 1)]


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
        if winner == None:
            ties += 1
        winning_moves += moves
    if ties == game_count:
        return None, winning_moves
    score = wins / (game_count - ties)
    return score, winning_moves


training_steps = 10000
player = WeightedPlayer.create(18)
for i in range(training_steps):
    score, winning_moves = get_player_score(50, player, RandomPlayer())
    x = np.array([x for x, _ in winning_moves])
    y = np.array([y for _, y in winning_moves])
    player.train(x, y)
    if i % 100 == 99:
        print(f'{round(i / training_steps * 10000) / 100}%: {round(score * 100) / 100}')

score, _ = get_player_score(10000, player, RandomPlayer())
print(score)

print_win = True
score, _ = get_player_score(4, player, HumanPlayer())
print(score)
