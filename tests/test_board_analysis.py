from go.board import (Board, PointState)
from go.board_analysis import BoardAnalysis  # NOQA

B = PointState.BLACK
W = PointState.WHITE
EMPTY = PointState.EMPTY


class TestSimpleEyeDetection(object):
    def test_corner_eye(self):
        b = Board(5)
        points_in_eye = set([(0, 1),
                             (1, 1),
                             (1, 0)])
        for point in points_in_eye:
            b[point] = B

        eyes = BoardAnalysis.find_eyes(b, B)
        assert len(eyes) == 1
        assert set(points_in_eye) == set(eyes[0])
