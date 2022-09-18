from XO_Board import Board

my_board = Board()
my_board.print_board()

while my_board.is_winner() == None:
    my_board.user_go()
    my_board.print_board()

    if my_board.is_winner() == None:
        next_move = my_board.find_best_move("o")
        my_board.set_point("o",next_move["x"],next_move["y"])
        my_board.print_board()

print(f"the winner is {my_board.is_winner()}")
