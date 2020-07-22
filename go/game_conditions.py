#!/usr/bin/env python

class GameConditions(object):

    TRADITIONAL_BOARD_SIZES = (9, 13, 19)

    def __init__(self, players, board_size=19, starting_player=None,
                 custom_komi=None, description='', start_date=None):
        if not isinstance(players, list):
            raise ValueError('players must be list of players')
        if len(players) != 2:
            raise ValueError('players must be list of two players')
        self.players = players

        if board_size not in GameConditions.TRADITIONAL_BOARD_SIZES:
            raise ValueError("Board state must be one of "
                             "f{','.join(TRADITIONAL_BOARD_SIZES}. "
                             "Received f{board_size}")
        self.board_size = board_size

        if starting_player is not None and starting_player not in players:
            raise ValueError('starting_player must be included in '
                             'list of players')
        self.starting_player = starting_player

        if isinstance(custom_komi, (int, float)) and custom_komi < 0:
            raise ValueError('komi must be non-negative number')
        self.custom_komi = custom_komi
        self.description = description
        self.start_date = start_date
