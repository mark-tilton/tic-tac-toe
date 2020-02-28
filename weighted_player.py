import numpy as np
import random as rand


class WeightedPlayer:

    def __init__(self, h, w1, w2, b1, b2):
        self.h = h
        self.w1 = w1
        self.w2 = w2
        self.b1 = b1
        self.b2 = b2


    @staticmethod
    def create(h):
        h = h
        w1 = np.random.randn(9, h)
        w2 = np.random.randn(h, 9)
        b1 = np.random.randn(9)
        b2 = np.random.randn(9)
        return WeightedPlayer(h, w1, w2, b1, b2)


    def mutate(self, rate):
        w1g = np.random.randn(9, self.h) * rate
        w2g = np.random.randn(self.h, 9) * rate
        b1g = np.random.randn(9) * rate
        b2g = np.random.randn(9) * rate
        new_player = WeightedPlayer(
            self.h,
            self.w1 + w1g,
            self.w2 + w2g, 
            self.b1 + b1g, 
            self.b2 + b2g)
        new_player.w1g = w1g
        new_player.w2g = w2g
        new_player.b1g = b1g
        new_player.b2g = b2g
        return new_player

    def take_turn(self, board, player_id):
        vec = np.copy(board.cells)
        for i in range(9):
            if vec[i] == player_id + 1:
                vec[i] = 1
            if vec[i] == (1 - player_id) + 1:
                vec[i] = -1
        h = vec.dot(self.w1)
        h = np.maximum(h, 0) + self.b1
        y = h.dot(self.w2) + self.b2
        best_score = -1e6
        best_move = -1
        for (cell, score, i) in zip(vec, y, range(9)):
            if cell == 0:
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move
