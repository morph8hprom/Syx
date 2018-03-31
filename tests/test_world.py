#!/usr/bin/env python3

import unittest
import os
from Syx.world import *
from Syx.item import *
from Syx.character import *
from Syx.map import *
from Syx.room import *
start_id = 1
num_of_rooms = 5
num_of_items = 3
num_of_char = 3

class WorldAttributeTestCase(unittest.TestCase):
    """
    Verifies all attributes of world instance
    """
    @classmethod
    def setUpClass(cls):
        """
        Uses build_world function to create world data
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/tests")

        cls.map = build_map(start_id, num_of_rooms)
        cls.items = item_list(start_id, num_of_items)
        cls.chars = char_list(start_id, num_of_char)
        cls.start_loc = 1
        cls.world = build_world(cls.map, cls.items, cls.chars, cls.start_loc)

    def test_world_has_map(self):
        att = hasattr(self.world, 'map')
        self.assertTrue(att)

    def test_world_has_items(self):
        att = hasattr(self.world, 'items')
        self.assertTrue(att)

    def test_world_has_chars(self):
        att = hasattr(self.world, 'chars')
        self.assertTrue(att)

    def test_world_has_start_loc(self):
        att = hasattr(self.world, 'start_loc')
        self.assertTrue(att)
