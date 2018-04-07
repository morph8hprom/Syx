#!/usr/bin/env python3

import json
import textwrap
from cmd2 import Cmd
from world import *
from map import *
from room import *
from command import *


class Game():
    def __init__(self, world):
        self.world = world
        self.map = world.map



def build_game(start_id, num_rooms, start_loc):
    start_id = 1
    start_loc = 1
    map = Map(build_map(start_id, num_rooms))
    world = build_world(map, start_loc)
    game = Game(world)
    return game
