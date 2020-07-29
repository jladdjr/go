import pytest

from go.board import (Board, PointState)
from go.board_analysis import BoardAnalysis  # NOQA

B = PointState.BLACK
W = PointState.WHITE
EMPTY = PointState.EMPTY


class TestSimpleEyeDetection(object):
    @pytest.mark.parametrize('points_in_eye', [[(0, 1), (1, 1), (1, 0)],
                                               [(3, 4), (3, 3), (4, 3)],
                                               [(0, 3), (1, 3), (1, 4)],
                                               [(0, 3), (1, 3), (1, 4)],
                                               [(1, 1), (2, 1), (3, 1),
                                                (3, 2), (3, 3), (2, 3),
                                                (1, 3), (1, 2)]],
                             ids=['bottom_left_corner_eye',
                                  'top_right_corner_eye',
                                  'top_left_corner_eye',
                                  'bottom_right_corner_eye',
                                  'middle_of_board'])
    def test_simple_eyes(self, points_in_eye):
        b = Board(5)
        points_in_eye = set(points_in_eye)
        for point in points_in_eye:
            b[point] = B

        eyes = BoardAnalysis.find_eyes(b, B)
        assert len(eyes) == 1
        assert set(points_in_eye) == set(eyes[0])
