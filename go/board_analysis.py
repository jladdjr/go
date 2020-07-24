#!/usr/bin/env python

from go.board import PointState

B = PointState.BLACK
W = PointState.WHITE
EMPTY = PointState.EMPTY


class BoardAnalysis(object):

    @classmethod
    def _collect_states_of_potential_eye(cls, board, stone_color, col, row):
        """lists the states of stones
        centered about a given point"""
        uses_edge = False
        states = []
        points_in_eye = []
        for i in range(col - 1, col + 2):
            for j in range(row - 1, row + 2):
                if i == col and j == row:
                    # skip center point
                    continue
                if i < 0 or j < 0 or i >= board.size or j >= board.size:
                    uses_edge = True
                    continue
                state = board[i, j]
                states.append(state)
                if state is stone_color:
                    points_in_eye.append((i, j))
        return uses_edge, states, points_in_eye

    @classmethod
    def find_eyes(cls, board, stone_color):
        """Returns a list of 'eyes'. Each eye is represented
        by a list of tuples. Each tuple represents a stone
        that is part of the eye."""
        eyes = []

        def is_players_stone(state):
            return state is stone_color

        # scan each point in the board
        for i in range(0, board.size):
            for j in range(0, board.size):
                # center must be empty for this to be an eye
                if board[i, j] != EMPTY:
                    continue

                uses_edge, states, points_in_eye = \
                    cls._collect_states_of_potential_eye(board,
                                                         stone_color,
                                                         i, j)
                # if potential eye boarders a wall, then all points must be
                # occupied by stones of `stone_color`
                if uses_edge and all(map(is_players_stone, states)):
                    eyes.append(points_in_eye)
                # .. otherwise, all but one spot in the potential eye must be
                # occupied by stones of `stone_color`
                elif not uses_edge and \
                        len([filter(is_players_stone, states)]) >= 7:
                    eyes.append(points_in_eye)
        return eyes
