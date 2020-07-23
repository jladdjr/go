#!/usr/bin/env python

from enum import Enum


class PointState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class BoardStateException(Exception):
    pass


class Board(object):

    def __init__(self, size):
        self.size = size

        self.board = [[PointState.EMPTY for _ in range(size)]
                      for _ in range(size)]

    def set_point(self, col, row, state):
        current_state = self.get_point(col, row)
        if current_state != PointState.EMPTY:
            raise BoardStateException(f"Cannot set point {Point(col, row)} to "
                                      f"{getattr(state, 'name')}.")
        self.board[col][row] = state

    def get_point(self, col, row):
        return self.board[col][row]


class Point(object):

    def __init__(self, col, row):
        if col < 0 or col > 18:
            raise ValueError('column must be in [0, 18]. '
                             f'received: {col}')
        if row < 0 or row > 18:
            raise ValueError('row must be in [0, 18]. '
                             f'received: {row}')
        self.col = col
        self.row = row

    def __str__(self):
        # A1 Style
        # https://senseis.xmp.net/?Coordinates
        # I is skipped to avoid confusion with J
        columns = 'ABCDEFGHJKLMNOPQRST'
        col_letter = columns[self.col]
        row_number = str(self.row + 1)

        return f'{col_letter}{row_number}'
