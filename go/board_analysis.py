#!/usr/bin/env python

from go.board import PointState

B = PointState.BLACK
W = PointState.WHITE
EMPTY = PointState.EMPTY


class BoardAnalysis(object):

    @classmethod
    def _find_eye_at_point(cls, board, stone_color, col, row):
        """if eye is centered about given point,
        lists stones that form eye. otherwise, returns None"""
        # center must be empty for this to be an eye
        if board[col, row] != EMPTY:
            return None

        def is_players_stone(state):
            return state is stone_color

        def is_corner(i, j):
            return i in (col - 1, col + 1) and j in (row - 1, row + 1)

        uses_edge = col in (0, board.size - 1) or row in (0, board.size - 1)
        points_in_eye = []
        missing_corner = False
        for i in range(col - 1, col + 2):
            for j in range(row - 1, row + 2):
                # skip any edges that use the wall
                if i < 0 or j < 0 or i >= board.size or j >= board.size:
                    continue

                # skip center
                if (i, j) == (col, row):
                    continue

                state = board[i, j]

                # if we're beside a wall, all points must be owned by player
                if uses_edge and not is_players_stone(state):
                    return None

                # missing more than one corner is a no-no
                if is_corner(i, j) and not is_players_stone(state):
                    if missing_corner:
                        # eye cannot miss more than one corner
                        return None
                    missing_corner = True

                # missing any side is a no-no
                if not is_corner(i, j) and not is_players_stone(state):
                    return None

                # record point
                if is_players_stone(state):
                    points_in_eye.append((i, j))

        return points_in_eye

    @classmethod
    def find_eyes(cls, board, stone_color):
        """Returns a list of 'eyes'. Each eye is represented
        by a list of tuples. Each tuple represents a stone
        that is part of the eye."""
        eyes = []

        # scan each point in the board
        for i in range(0, board.size):
            for j in range(0, board.size):

                points_in_eye = cls._find_eye_at_point(board,
                                                       stone_color,
                                                       i, j)
                if points_in_eye:
                    eyes.append(points_in_eye)
        return eyes
