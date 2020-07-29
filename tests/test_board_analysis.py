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
                                                (1, 3), (1, 2)],
                                               [(1, 1), (2, 1), (3, 1),
                                                (3, 2), (2, 3),
                                                (1, 3), (1, 2)]],
                             ids=['bottom_left_corner_eye',
                                  'top_right_corner_eye',
                                  'top_left_corner_eye',
                                  'bottom_right_corner_eye',
                                  'middle_of_board',
                                  'eye_missing_corner'])
    def test_simple_eyes(self, points_in_eye):
        b = Board(5)
        points_in_eye = set(points_in_eye)
        for point in points_in_eye:
            b[point] = B

        eyes = BoardAnalysis.find_eyes(b, B)
        assert len(eyes) == 1
        assert set(points_in_eye) == set(eyes[0])

    @pytest.mark.parametrize('points_in_false_eye', [[(1, 1)],
                                                     [(0, 3)],
                                                     [(0, 0)],
                                                     [(1, 0), (1, 1)],
                                                     [(1, 0), (0, 1)],
                                                     [(1, 1), (3, 1),
                                                      (3, 2), (3, 3), (2, 3),
                                                      (1, 3), (1, 2)],
                                                     [(1, 1), (3, 1), (3, 3),
                                                      (1, 3)],
                                                     [(1, 1), (2, 1), (3, 1)],
                                                     [(1, 1), (2, 1), (3, 1),
                                                      (1, 2), (2, 2), (3, 2),
                                                      (1, 3), (2, 3), (3, 3)]],
                             ids=['single_point',
                                  'single_point_along_wall',
                                  'single_point_in_corner',
                                  'incomplete_eye_in_corner',
                                  'anothere_incomplete_eye_in_corner',
                                  'u_shaped_false_eye',
                                  'four_corners_of_square',
                                  'three_stones_in_a_row',
                                  'filled_in_square'])
    def test_false_eyes(self, points_in_false_eye):

        b = Board(5)
        points_in_false_eye = set(points_in_false_eye)
        for point in points_in_false_eye:
            b[point] = B

        eyes = BoardAnalysis.find_eyes(b, B)
        assert len(eyes) == 0
