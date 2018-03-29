#!/usr/bin/env python3

class Game():
    def __init__(self, world):
        self.world = world
        self.map = world.map
        self.items = world.items
        self.chars = world.chars
        #Add character select
