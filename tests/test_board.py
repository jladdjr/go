import pytest

from go.board import (Board,
                      BoardStateException,
                      PointState,
                      Point)


class TestBoard(object):
    @pytest.mark.parametrize('board_size', [9, 13, 19])
    def test_empty_board(self, board_size):
        board = Board(board_size)

        for x in range(board_size):
            for y in range(board_size):
                assert board.board[x][y] == PointState.EMPTY

    @pytest.mark.parametrize('col, row, color', [(3, 5, PointState.BLACK),
                                                 (2, 8, PointState.WHITE)])
    def test_setting_empty_space(self, col, row, color):
        board = Board(9)
        board.set_point(col, row, color)

    @pytest.mark.parametrize('color', [PointState.BLACK,
                                       PointState.WHITE])
    def test_setting_non_empty_space(self, color):
        board = Board(9)
        board.set_point(5, 5, color)
        with pytest.raises(BoardStateException):
            board.set_point(5, 5, color)


class TestPoint(object):
    @pytest.mark.parametrize('col, row', [(0, 0),
                                          (1, 1),
                                          (0, 5),
                                          (0, 18),
                                          (5, 9),
                                          (9, 5),
                                          (18, 18),
                                          (18, 0)])
    def test_valid_point(self, col, row):
        Point(col, row)

    @pytest.mark.parametrize('col, row', [(-1, 0),
                                          (0, -1),
                                          (-1, -1),
                                          (19, 19),
                                          (100, 100)])
    def test_invalid_point(self, col, row):
        with pytest.raises(ValueError):
            Point(col, row)

    @pytest.mark.parametrize('col, row, expected_str',
                             [(0, 0, 'A1'),
                              (1, 1, 'B2'),
                              (5, 5, 'F6'),
                              (8, 9, 'J10'),  # Columns skip I
                              (18, 18, 'T19'),
                              (4, 15, 'E16')])
    def test_str(self, col, row, expected_str):
        assert str(Point(col, row)) == expected_str
