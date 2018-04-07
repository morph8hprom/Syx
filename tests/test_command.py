#!/usr/bin/env python3

import unittest
import os
from cmd2 import Cmd
from src.command import *
from src.world import *
from src.map import *
from src.room import *

from src.game import *

start_id = 1
num_of_rooms = 5
start_loc = 1

class CommandAttributesTestCase(unittest.TestCase):
    """
    Verifies all attrbiutes of command instance
    """
    @classmethod
    def setUpClass(cls):
        """
        Creates a temporary cmd instance for testing purposes
        """
        os.chdir("/home/noved/Projects/HardWay/Syx/tests")


        cls.game = build_game(start_id, num_of_rooms, start_loc)
        cls.map = cls.game.map
        cls.cli = Command(cls.game)

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
        os.chdir("/home/noved/Projects/HardWay/Syx/tests")

        cls.game = build_game(start_id, num_of_rooms, start_loc)
        cls.map = cls.game.map
        cls.cli = Command(cls.game)

    def test_move_north_changes_player_loc(self):
        player_loc_1 = self.cli.player_loc
        self.cli.move('north')
        player_loc_2 = self.cli.player_loc
        self.assertNotEqual(player_loc_1, player_loc_2)

    def test_move_east_changes_player_loc(self):
        player_loc_1 = self.cli.player_loc
        self.cli.move('south')
        player_loc_2 = self.cli.player_loc
        self.assertNotEqual(player_loc_1, player_loc_2)

    def test_move_south_changes_player_loc(self):
        player_loc_1 = self.cli.player_loc
        self.cli.move('east')
        player_loc_2 = self.cli.player_loc
        self.assertNotEqual(player_loc_1, player_loc_2)

    def test_move_west_changes_player_loc(self):
        player_loc_1 = self.cli.player_loc
        self.cli.move('west')
        player_loc_2 = self.cli.player_loc
        self.assertNotEqual(player_loc_1, player_loc_2)

    def test_move_nonsense_does_not_change_loc(self):
        player_loc_1 = self.cli.player_loc
        self.cli.move('nonsense')
        player_loc_2 = self.cli.player_loc
        self.assertEqual(player_loc_1, player_loc_2)
