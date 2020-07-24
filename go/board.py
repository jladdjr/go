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
        >>> b = Board(19)
        >>> b[5][5]  # retrieve (5, 5), note that indexing begins with 0

        >>> b[5, 5]  # method also supports passing in a tupple of coordinates
        """
        # if we received a tuple
        if isinstance(key, tuple):
            if len(key) != 2:
                raise ValueError('Board.__getitem__ expected a tuple of two '
                                 f' elements. received: {key}')
            col, row = key
            return self.board[col][row]

        # if this is a part of double brackets (i.e. board[col][row])
        if not isinstance(key, int):
            raise ValueError('Board.__getitem__ expects either a tuple of '
                             'two elements (col, row), or an integer '
                             'representing the index of a column '
                             '(in the case of using two brackets: '
                             f'board[col][row]). received: {key}')
        if key < 0 or key >= self.size:
            raise ValueError('column index must be between 0 and '
                             f'{self.size - 1}. received {key}.')
        return self.board[key]

    def __setitem__(self, key, value):
        """Assigning a column a value is not supported.

        Only supports assigning a point a value by way of `key`
        taking the form of a tuple.
        """
        if not isinstance(key, tuple):
            raise ValueError('Board.__setitem__ expected a tuple of two '
                             f' elements. received: {key}')
        if len(key) != 2:
            raise ValueError('Board.__setitem__ expected a tuple of two '
                             f' elements. received: {key}')
        col, row = key
        current_state = self.board[col][row]
        if current_state != PointState.EMPTY:
            raise BoardStateException("Cannot set point "
                                      f"{Point(col, row)} to "
                                      f"{getattr(value, 'name')}; "
                                      'point already has value '
                                      f"{getattr(current_state, 'name')}")
        self.board[col][row] = value


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
                                      f"{getattr(value, 'name')}; "
                                      'point already has value '
                                      f"{getattr(current_state, 'name')}")
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
