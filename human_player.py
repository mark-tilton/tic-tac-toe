class HumanPlayer:

    def take_turn(self, board, id):
        print()
        print(board)
        move = input("Please enter your move: ")
        x = int(move[0])
        y = int(move[1])
        return y * 3 + x
