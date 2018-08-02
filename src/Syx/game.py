#!/usr/bin/env python3

import json
import bwamu
import gim
import upacc


class Game():
    def __init__(self, world):
        self.world = world
        self.constants = {}

    def _update_constants(self):
        d = {}
        jsontext = resource_string(__name__, 'data/game_constants.json')
        d = json.loads(jsontext.decode('utf-8'))
        self.constants = d
