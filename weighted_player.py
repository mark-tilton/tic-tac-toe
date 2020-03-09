import numpy as np
import random as rand
import torch
import torch.nn as nn
import torch.nn.functional as F
from neuralnet import Net


def normalize_board(board, player_id):
    vec = np.copy(board.cells)
    for i in range(9):
        if vec[i] == player_id + 1:
            vec[i] = 1
        if vec[i] == (1 - player_id) + 1:
            vec[i] = -1
    return vec


def make_one_hot(i):
    vec = torch.zeros(9)
    vec[i] = 1
    return vec


class WeightedPlayer:

    def __init__(self):
        self.net = Net()

    def evaluate(self, board, player_id):
        vec = torch.from_numpy(normalize_board(board, player_id)).float()
        output = self.net.forward(torch.from_numpy(vec).float())
        return output

    def take_turn(self, board, player_id):
        result_vec = self.evaluate(board, player_id)
        best_score = -1e6
        best_move = -1
        for (cell, score, i) in zip(board.cells, result_vec, range(9)):
            if cell == 0:
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def train(self, winning_moves):
        x = torch.from_numpy([normalize_board(board, action.val)
                              for board, action in winning_moves])
        y = torch.from_numpy([make_one_hot(action.pos)
                              for board, action in winning_moves])
        self.net.train(x, y)
