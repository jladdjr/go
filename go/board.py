#!/usr/bin/env python

from enum import Enum


class PointState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class BoardStateException(Exception):
    pass


class Board(object):
    """Go board. Indexed by (col, row), where (0, 0)
    represents the bottom-left corner from Black's view."""

    def __init__(self, size):
        self.size = size

        self.board = [Column(index, size) for index in range(size)]

    def __getitem__(self, key):
        """Supports indexing a board.

        More specifically:
        - Returns a `Column` object
        - .. which, in turn, also supports indexing
             so that it is possible to retrieve a given point using:

        >>> b = Board(19)
        >>> b[5][5]  # retrieve (5, 5), note that indexing begins with 0
        """
        if key < 0 or key >= self.size:
            raise ValueError('column index must be between 0 and '
                             f'{self.size - 1}. received {key}.')
        return self.board[key]

    def __setitem__(self, key, value):
        """Assigning a column a value is not supported.

        This method does not play a role in assigning a board position
        a value. That happens by:

        1. Accessing a column (using Board.__getitem__)
        2. Assigning a value to a row (using Column.__setitem__)
        """
        raise NotImplementedError('Board columns cannot be assigned a value')

    def get_point(self, col, row):
        return self.board[col][row]


class Column(object):
    """A single column of a board. Intermediate object that assists in
    indexing a board."""

    def __init__(self, column_index, size):
        self.size = size
        # so that column can know its position on the board
        # (in order to have context when printing error / debug statements
        self.column_index = column_index
        self.column = [PointState.EMPTY for _ in range(size)]

    def __getitem__(self, key):
        """Implements indexing for a board column."""
        if key < 0 or key >= self.size:
            raise ValueError('row index must be between 0 and '
                             f'{self.size - 1}. received {key}.')
        return self.column[key]

    def __setitem__(self, key, value):
        current_state = self.column[key]
        if current_state != PointState.EMPTY:
            raise BoardStateException("Cannot set point "
                                      f"{Point(self.column_index, key)} to "
                                      f"{getattr(value, 'name')}.")
        self.column[key] = value


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
