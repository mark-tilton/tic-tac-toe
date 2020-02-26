from board import Board
from action import Action

board = Board()

print(board)

player = 0
while True:
    move = input("Please enter your move: ")
    x = int(move[0])
    y = int(move[1])
    board = board.make_move(Action(x, y, player + 1))
    print(board)
    winner = board.get_winner()
    if winner != None:
        print(f'{Board.get_player_name(winner)} wins!')
        break
    player = 1 - player

