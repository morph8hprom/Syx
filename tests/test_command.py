#!/usr/bin/env python3

import unittest
import os
from cmd2 import Cmd
from Syx.command import *
from Syx.world import *
from Syx.map import *
from Syx.room import *
from Syx.item import *
from Syx.character import *

start_id = 1
num_of_rooms = 5
num_of_items = 3
num_of_char = 3

class CommandAttributesTestCase(unittest.TestCase):
    """
    Verifies all attrbiutes of command instance
    """
    @classmethod
    def setUpClass(cls):
        """
        Creates a temporary cmd instance for testing purposes
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")
        cls.map = build_map(start_id, num_of_rooms)
        cls.items = item_list(start_id, num_of_items)
        cls.chars = char_list(start_id, num_of_char)
        cls.start_loc = 1
        cls.world = build_world(cls.map, cls.items, cls.chars, cls.start_loc)
        cls.cli = Command(cls.world)

    def test_cli_has_world(self):
        att = hasattr(self.cli, 'world')
        self.assertTrue(att)

    def test_cli_has_player_loc(self):
        att = hasattr(self.cli, 'player_loc')
        self.assertTrue(att)

class CommandFunctionsTestCase(unittest.TestCase):
    """
    Verifies that cli functions are working properly
    """
    @classmethod
    def setUpClass(cls):
        """
        Creates a temporary cmd instance for testing purposes
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/Syx")
        cls.map = build_map(start_id, num_of_rooms)
        cls.items = item_list(start_id, num_of_items)
        cls.chars = char_list(start_id, num_of_chars)
        cls.start_loc = 1
        cls.world = build_world(cls.map, cls.items, cls.chars, cls.start_loc)
        cls.cli = Command(cls.world)
