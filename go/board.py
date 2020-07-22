#!/usr/bin/env python

from enum import Enum


class PointState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Board(object):

    def __init__(self, size):
        self.size = size

        self.board = [[PointState.EMPTY for _ in range(size)]
                      for _ in range(size)]
