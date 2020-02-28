import numpy as np
import random as rand


class WeightedPlayer:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def mutate(self, rate):
        w1gradient = np.random.randn(9, 9) * rate
        bgradient = np.random.randn(9) * rate
        new_player = WeightedPlayer(self.weights + w1gradient, self.bias + bgradient)
        new_player.w1gradient = w1gradient
        new_player.bgradient = bgradient
        return new_player

    def take_turn(self, board, player_id):
        vec = np.copy(board.cells)
        for i in range(9):
            if vec[i] == player_id + 1:
                vec[i] = 1
            if vec[i] == (1 - player_id) + 1:
                vec[i] = -1
        result_vec = vec.dot(self.weights) + self.bias
        best_score = -1e6
        best_move = -1
        for (cell, score, i) in zip(vec, result_vec, range(9)):
            if cell == 0:
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move
