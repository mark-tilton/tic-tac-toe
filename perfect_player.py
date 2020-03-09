from action import Action
from board import Board


def evaluate(board, player_id):
    valid_moves = board.get_valid_moves(player_id)
    if len(valid_moves) == 0:
        # Game is a tie
        return 0, 0
    max_score = -1
    max_action = -1
    for turn in valid_moves:
        new_board = board.make_move(Action(turn, player_id + 1))
        if new_board.get_winner() == player_id + 1:
            return turn, 1
        _, score = evaluate(new_board, 1 - player_id)
        score = -score
        if score > max_score:
            max_score = score
            max_action = turn
    return max_action, max_score


class PerfectPlayer:

    def take_turn(self, board, player_id):
        action, score = evaluate(board, player_id)
        print(f'My score: {score}')
        return action


board = Board()
board.cells = [1, 0, 0, 0, 2, 0, 0, 0, 0]
blah = evaluate(board, 0)
