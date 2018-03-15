#!/usr/bin/env python3

import unittest
import os
from Syx.world import *
from Syx.item import *
from Syx.character import *
from Syx.map import *
from Syx.room import *
id = 1
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
        Uses build_world function to check world data
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")

        cls.map = build_map()

        cls.world = build_world()
