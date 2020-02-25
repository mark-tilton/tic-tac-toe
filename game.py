from board import Board
from action import Action

board = Board()

print(board)

while True:
    move = input("Please enter your move: ")
    x = int(move[0])
    y = int(move[1])
    val = 1
    board = board.make_move(Action(x, y, val))
    print(board)
