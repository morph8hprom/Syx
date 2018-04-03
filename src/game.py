#!/usr/bin/env python3

import os
import sys
import json
import textwrap
from cmd2 import Cmd
from src.world import *
from src.map import *
from src.room import *
from src.item import *
from src.character import *
from src.command import *


class Game():
    def __init__(self, world):
        self.world = world
        self.map = world.map
        self.items = world.items
        self.chars = world.chars


def build_game(start_id, num_rooms, num_items, num_chars, start_loc, world):
    start_id = 1
    start_loc = 1
    map = Map(build_map(start_id, num_rooms))
    items = item_list(start_id, num_items)
    chars = char_list(start_id, num_chars)
    world = build_world(map, items, chars, start_loc)
    game = Game(world)
    return game
