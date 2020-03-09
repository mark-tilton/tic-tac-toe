import numpy as np
import random as rand


class WeightedPlayer:

    def __init__(self, h, w1, w2):
        self.h = h
        self.w1 = w1
        self.w2 = w2


    @staticmethod
    def create(h):
        h = h
        w1 = np.random.randn(9, h)
        w2 = np.random.randn(h, 9)
        return WeightedPlayer(h, w1, w2)


    def take_turn(self, board, player_id):
        vec = board.get_normalized_cells(player_id)
        h = vec.dot(self.w1)
        h = np.maximum(h, 0)
        y = h.dot(self.w2) + [0, 0, 0, 0, 1e-3, 0, 0, 0, 0]
        best_score = -1e6
        best_move = -1
        for (cell, score, i) in zip(vec, y, range(9)):
            if cell == 0:
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def train(self, x, y):
        learning_rate = 1e-6
        for t in range(500):
            # Forward pass: compute predicted y
            h = x.dot(self.w1)
            h_relu = np.maximum(h, 0)
            y_pred = h_relu.dot(self.w2) + [0, 0, 0, 0, 1e-3, 0, 0, 0, 0]

            # Compute and print loss
            loss = np.square(y_pred - y).sum()
            # print(t, loss)

            # Backprop to compute gradients of w1 and w2 with respect to loss
            grad_y_pred = 2.0 * (y_pred - y)
            grad_w2 = h_relu.T.dot(grad_y_pred)
            grad_h_relu = grad_y_pred.dot(self.w2.T)
            grad_h = grad_h_relu.copy()
            grad_h[h < 0] = 0
            grad_w1 = x.T.dot(grad_h)

            # Update weights
            self.w1 -= learning_rate * grad_w1
            self.w2 -= learning_rate * grad_w2
