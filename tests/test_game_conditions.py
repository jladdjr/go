import pytest
from mock import Mock

from go.game_conditions import GameConditions


@pytest.mark.parametrize('board_size', [-5, -1, 0, 1, 4, 25, 100])
def test_bad_board_size(board_size):
    players = [Mock(), Mock()]
    with pytest.raises(ValueError) as err:
        GameConditions(players, board_size)

@pytest.mark.parametrize('board_size', [9, 13, 19])
def test_valid_board_size(board_size):
    players = [Mock(), Mock()]
    GameConditions(players, board_size)

def test_invalid_starting_player():
    invalid_player = Mock()
    players = [Mock(), Mock()]

    with pytest.raises(ValueError) as err:
        GameConditions(players, starting_player=invalid_player)
    assert str(err.value) == 'starting_player must be included in list of players'

@pytest.mark.parametrize('custom_komi', [-5, -1])
def test_bad_komi(custom_komi):
    players = [Mock(), Mock()]
    with pytest.raises(ValueError) as err:
        GameConditions(players, custom_komi=custom_komi)

