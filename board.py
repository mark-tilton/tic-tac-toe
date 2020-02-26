import numpy as np

char_map = {
    0: ' ',
    1: 'X',
    2: 'O'
}

class Board:

    def __init__(self):
        self.cells = np.zeros((3, 3))
    

    def clone(self):
        clone = Board()
        clone.cells = np.copy(self.cells)
        return clone


    def make_move(self, action):
        new_board = self.clone()
        # Treat cells as row-major to make repr easier
        new_board.cells[action.y, action.x] = action.val
        return new_board


    def get_winner(self):
        # Check rows / columns
        for i in range(3):
            val = self.cells[i, i]
            if val == 0:
                continue
            if self.cells[(i + 1) % 3, i] == val and self.cells[(i + 2) % 3, i] == val:
                return val
            if self.cells[i, (i + 1) % 3] == val and self.cells[i, (i + 2) % 3] == val:
                return val
        # Check diagonals
        center_val = self.cells[1, 1]
        if center_val != 0:
            if self.cells[0, 0] == center_val and self.cells[2, 2] == center_val:
                return center_val
            if self.cells[0, 2] == center_val and self.cells[2, 0] == center_val:
                return center_val
        return None


    @staticmethod
    def get_player_name(player):
        return char_map[player]


    @staticmethod
    def repr_row(row):
        result = ''
        result += Board.get_player_name(row[0])
        for cell in row[1:]:
            result += '|'
            result += Board.get_player_name(cell)
        return result


    def __repr__(self):
        result = ''
        result += '  0 1 2\n0 '
        result += Board.repr_row(self.cells[0])
        row_num = 1
        for row in self.cells[1:]:
            result += f'\n  -----\n{row_num} '
            row_num += 1
            result += Board.repr_row(row)
        return result