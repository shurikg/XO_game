from python.XO_Board import Board

def test_win_x():
    test_board = Board()

    test_board.set_point("x", 2, 2)
    test_board.set_point("o", 2, 1)
    test_board.set_point("x", 1, 1)
    test_board.set_point("o", 3, 1)
    test_board.set_point("x", 3, 3)

    assert "x" == test_board.is_winner(), "Winner is X"

def test_set_negative_point():
    test_board = Board()

    set_result = test_board.set_point("x", -2, 2)

    assert False == set_result

def test_set_occupied_point():
    test_board = Board()

    test_board.set_point("x", 2, 2)
    set_result = test_board.set_point("x", 2, 2)

    assert False == set_result
