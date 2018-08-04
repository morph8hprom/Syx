#!/usr/bin/env python3

import json
from pkg_resources import resource_string
from bwamu import world as W

"""
File used to define Game class and it's methods
"""


class Game():
    def __init__(self, player):
        self.constants = {}
        self._update_constants()
        self.world = W.World(**self.constants)
        self.map = self.world.map
        self.items = self.world.items
        self.characters = self.world.characters
        self.player = player
        self.player_loc = None
        self._update_player_loc()





    def _update_constants(self):
        d = {}
        jsontext = resource_string(__name__, 'data/game_constants.json')
        d = json.loads(jsontext.decode('utf-8'))
        self.constants = d

    def _update_player_loc(self):
        if self.player.loc is not None:
            self.player_loc = self.player.loc
        else:
            self.player_loc = self.world.START_LOC
