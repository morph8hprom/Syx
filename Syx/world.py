#!/usr/bin/env python3

import json

"""
Defines a world class and a functon used to create an instance of the world class
"""

class World():
    def __init__(self,
        map,
        items,
        chars):
        self.map = map
        self.items = items
        self.chars = chars

def build_world(map, items, chars):
    print("Building world")
    world = World(map, items, chars)

    return world
