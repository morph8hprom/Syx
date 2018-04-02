#!/usr/bin/env python3

import json

"""
Defines a world class and a functon used to create an instance of the world class
"""

class World():
    def __init__(self,
        map,
        items,
        chars,
        start_loc):
        self.map = map
        self.items = items
        self.chars = chars
        self.start_loc = start_loc

def build_world(map, items, chars, start_loc):
    print("Building world")
    world = World(map, items, chars, start_loc)

    return world
