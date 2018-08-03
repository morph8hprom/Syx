#!/usr/bin/env python3

import json
from pkg_resources import resource_string
from bwamu import world as W



class Game():
    def __init__(self):
        self.constants = {}
        self._update_constants()
        self.world = W.World(**self.constants)
        self.map = self.world.map
        self.items = self.world.items
        self.characters = self.world.characters




    def _update_constants(self):
        d = {}
        jsontext = resource_string(__name__, 'data/game_constants.json')
        d = json.loads(jsontext.decode('utf-8'))
        self.constants = d
