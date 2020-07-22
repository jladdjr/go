import pytest

from go.board import (Board, PointState)

@pytest.mark.parametrize('board_size', [9, 13, 19])
def test_empty_board(board_size):
    board = Board(board_size)

    for x in range(board_size):
        for y in range(board_size):
            assert board.board[x][y] == PointState.EMPTY
