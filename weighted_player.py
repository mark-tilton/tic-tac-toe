import numpy as np
import random as rand

class WeightedPlayer:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias


    def mutate(self, rate):
        gradient = np.zeros((9, 9))
        bgrad = np.zeros(9)
        for x in range(9):
            bgrad[x] = (2 * rand.random() - 1) * rate
            for y in range(9):
                gradient[x, y] = (2 * rand.random() - 1) * rate
        new_player = WeightedPlayer(self.weights + gradient, self.bias + bgrad)
        new_player.gradient = gradient
        new_player.bgrad = bgrad
        return new_player
        
    
    def take_turn(self, board, player_id):
        vec = board.cells.flatten()
        for i in range(9):
            if vec[i] == player_id + 1:
                vec[i] = 1
            if vec[i] == (1 - player_id) + 1:
                vec[i] = -1
        result_vec = [sum(r) for r in self.weights * vec] + self.bias
        best_score = -1e6
        best_move = -1
        for (cell, score, i) in zip(vec, result_vec, range(9)):
            if cell == 0:
                if score > best_score:
                    best_score = score
                    best_move = i
        return (best_move % 3, int(best_move / 3))

