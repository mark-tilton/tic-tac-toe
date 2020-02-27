import random as rand


class RandomPlayer:

    def take_turn(self, board, id):
        possible_moves = [i for (v, i) in zip(board.cells, range(9)) if v == 0]
        move = possible_moves[rand.randint(0, len(possible_moves) - 1)]
        return (move % 3, int(move / 3))
