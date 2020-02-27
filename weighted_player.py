import numpy as np
import random as rand
import torch
import torch.nn as nn
import torch.nn.functional as F
from neuralnet import Net


class WeightedPlayer:

    def __init__(self):
        self.net = Net().double()


    def evaluate(self, board, player_id):
        vec = np.copy(board.cells)
        for i in range(9):
            if vec[i] == player_id + 1:
                vec[i] = 1
            if vec[i] == (1 - player_id) + 1:
                vec[i] = -1
        vec = torch.from_numpy(vec).double()
        output = self.net(vec)
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
        for board, action in winning_moves:
            target = torch.zeros(9).double()
            target[action.pos] = 1
            output = self.evaluate(board, action.val)
            criterion = nn.MSELoss()
            loss = criterion(output, target)
            self.net.zero_grad()
            loss.backward()