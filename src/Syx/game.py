#!/usr/bin/env python3

import json
from pkg_resources import resource_string
from bwamu import world as W

"""
File used to define Game class and it's methods
"""


class Game():
    def __init__(self, player):
        self._constants = {}
        self._update_constants()
        self._world = W.World(**self._constants)
        self._map = self._world._map
        self._items = self._world._items
        self._characters = self._world._characters
        self._player = player
        self._player_loc = None
        self._update_player_loc()





    def _update_constants(self):
        d = {}
        jsontext = resource_string(__name__, 'data/game_constants.json')
        d = json.loads(jsontext.decode('utf-8'))
        self._constants = d

    def _update_player_loc(self):
        if self._player._loc is not None:
            self._player_loc = self._player._loc
        else:
            self._player_loc = self._world.START_LOC
