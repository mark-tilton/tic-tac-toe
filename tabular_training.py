from board import Board
import numpy as np
from action import Action

model = {}


def get_board_id(board, player_id):
    vec = board.cells
    id = ''
    for i in range(9):
        if vec[i] == player_id + 1:
            id += '1'
        elif vec[i] == (1 - player_id) + 1:
            id += '2'
        else:
            id += '0'
    return id


def take_random_turn(board):
    valid_actions = board.get_valid_moves()
    return np.random.choice(valid_actions)


def take_model_turn(board, id):
    valid_actions = board.get_valid_moves()
    boards = (board.make_move(Action(action, id + 1))
              for action in valid_actions)
    scores = []
    for board in boards:
        if board in model:
            scores.append(model[board])
        else:
            winner = board.get_winner()
            if winner == None:
                new_score = 0.5
            if winner == id + 1:
                new_score == 1
            if winner == (1 - id) + 1:
                new_score == 0
            model[board] = new_score
            scores.append(new_score)


player = 0
total_games = 10
for g in range(total_games):
    # Start game
    player = g % 1
    board = Board()
    for _ in range(9):
        if player == 0:
            action = take_model_turn(board, 0)
        else:
            action = take_random_turn(board)
        board = board.make_move(action)
        player = 1 - player
