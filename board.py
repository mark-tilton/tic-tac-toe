import numpy as np

class Board:

    def __init__(self):
        self.cells = np.zeros((3, 3))
    

    def clone(self):
        clone = Board()
        clone.cells = np.copy(self.cells)
        return clone


    def make_move(self, action):
        new_board = self.clone()
        new_board.cells[action.y, action.x] = action.val
        return new_board


    @staticmethod
    def repr_column(column):
        char_map = {
            0: ' ',
            1: 'X',
            2: 'O'
        }
        result = ''
        result += char_map[column[0]]
        for row in column[1:]:
            result += '|'
            result += char_map[row]
        return result


    def __repr__(self):
        result = ''
        result += Board.repr_column(self.cells[0])
        for column in self.cells[1:]:
            result += '\n-----\n'
            result += Board.repr_column(column)
        return result