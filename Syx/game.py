#!/usr/bin/env python3

import os
import sys
import json
import textwrap
from cmd2 import Cmd
from Syx.world import *
from Syx.map import *
from Syx.room import *
from Syx.item import *
from Syx.character import *
from Syx.command import *


class Game():
    def __init__(self, world):
        self.world = world
        self.map = world.map
        self.items = world.items
        self.chars = world.chars


def build_game(world):
    room_start_id = 1
    num_of_rooms = 5
    item_start_id = 1
    num_of_items = 3
    char_start_id = 1
    num_of_chars = 3
    start_loc = 1
    map = Map(build_map(room_start_id, num_of_rooms))
    items = item_list(item_start_id, num_of_items)
    chars = char_list(char_start_id, num_of_chars)
    world = build_world(map, items, chars, start_loc)
    game = Game(world)
    return game
